import segment
import elasticSearch
import pageRank
from gensim.models import Word2Vec
from numpy import *

def disambiguation():
    words = segment.inputfile('input.txt')
    es1 = elasticSearch.Elastic("redirect", ip="127.0.0.1")
    es2 = elasticSearch.Elastic("diasmbiguation", ip="127.0.0.1")
    es3 = elasticSearch.Elastic("page", ip="127.0.0.1")

    entities = []
    vertices = []

    # 候选实体集
    for word in words:
        entities1 = set(es1.search_data(word))
        entities2 = set(es2.search_data(word))
        entities3 = set(es3.search_data(word))
        entities_union = list(entities1 | entities2 | entities3)
        vertices += entities_union
        entities.append(entities_union)

    loaded_model = Word2Vec.load('word2vec.model')  # 加载模型

    while True:
        # 实体关系图构建
        edge = [[0] * len(vertices)] * len(vertices)

        start = 0
        end = 0
        # 对应于同一单词的多个候选实体
        for i in entities:
            start = end
            end = start + len(i)
            for x in range(start, end):
                # 辅助边
                edge[x][x] = 0.15
                sumup = 0
                # 计算与其他单词对应候选实体的关联度 作为边的权值（双向）
                for y in range(0, len(vertices)):
                    if y < start or y >= end:
                        temp = loaded_model.wv.similarity(vertices[x], vertices[y])
                        edge[x][y] = temp
                        sumup += temp
                # 归一化
                for y in range(0, len(vertices)):
                    if y < start or y >= end:
                        edge[x][y] = edge[x][y] / sumup
                        edge[y][x] = edge[x][y]
        a = array(transpose(edge), dtype=float)  # dtype指定为float
        M = pageRank.graphMove(a)
        pr = pageRank.firstPr(M)
        p = 0.85  # 引入浏览当前网页的概率为p,假设p=0.85
        result = pageRank.pagerank(p, M, pr)  # 计算pr值

        while True:
            if max(result) == 0:
                return entities
            max_pagerank = result.index(max(result))

            start = 0
            end = 0
            for i in range(0, len(entities)):
                start = end
                end = start + len(entities[i])
                if max_pagerank >= start and max_pagerank < end:
                    break

            if len(entities[i]) > 1:
                entities[i] = []
                entities[i].append(vertices[max_pagerank])
                for x in range(start, end):
                    if x != max_pagerank:
                        del vertices[x]
                break
            else:
                result[max_pagerank] = 0


from gensim.models import word2vec
from gensim.models import Word2Vec
import logging

# 主程序
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus(u"entity.txt")  # 加载语料
# 模型初始化
model = word2vec.Word2Vec(sentences, size=500, window=5, sg=1, negative=25, iter=10)
model.wv.save_word2vec_format("word2vec.model", binary=False)
# loaded_model = Word2Vec.load('word2vec.model')  # 加载模型
# y = loaded_model.wv.similarity(u"xxx", u"yyy")

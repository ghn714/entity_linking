from elasticsearch import Elasticsearch


class Elastic:
    def __init__(self, index_name, ip="127.0.0.1"):

        self.index_name = index_name
        self.es = Elasticsearch([ip],
                                http_auth=('elastic',
                                           'password'),
                                port=9200)

    def create_index(self):
        # 创建索引
        _index_mappings = {
            "mappings": {
                "properties": {
                    "title": {
                        "type": "text",
                        "index": True,
                    },
                    "category":{
                        "type": "text",
                        "index": True,
                     },
                    "infobox": {
                        "type": "text",
                        "index": True,
                    },
                    "abstruct": {
                        "type": "text",
                        "index": True,
                    }
                    }
            }
        }
        if self.es.indices.exists \
                    (index=self.index_name) is not True:
            res = self.es.indices.create \
                (index=self.index_name, body=_index_mappings)
            print(res)

    def insert_data(self, title, category, infobox, abstruct):

         action = {
            "title": title,
            "category": category,
             "infobox": infobox,
             "abstruct": abstruct
         }

         self.es.index(index=self.index_name,
                       body=action)

    def search_data(self, input_text):
        # doc = {'query': {'match_all': {}}}
        # start_time = time()
        doc = {
            "query": {
                "match": {
                    "title":  input_text
                }
            }
        }
        _searched = self.es.search(
            index=self.index_name,
            body=doc)

        entities = []
        for hit in _searched['hits']['hits']:
            #print(hit['_source'])
            entities.append(hit['_source']['title'])

        return entitys

if __name__ == '__main__':
    es = Elastic("test1", ip="127.0.0.1")
    es.create_index()
    es.insert_data("china", "a", "a", "a")
    es.insert_data("chinese people", "a", "a", "a")
    es.insert_data("china panda", "a", "a", "a")
    es.insert_data("nothing", "china has many people.", "a", "a")
    es.search_data("china")


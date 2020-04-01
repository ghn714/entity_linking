import rdflib
from rdflib import Graph
g = Graph()
g.parse("kglol.rdf", format=rdflib.util.guess_format("kglol.rdf"))
v = set()
for s, p, o in g:
    v.add(str(s))
    v.add(str(o))
# print(v)
vList = list(v)

# 去除url
# content = re.sub(
#            r'(?:(?:http|ftp)s?://)?' # http:// or https://
#            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
#            r'localhost|' #localhost...
#            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
#            r'(?::\d+)?' # optional port
#            r'(?:\S*)', "", content, flags=re.MULTILINE | re.IGNORECASE)
# print(vList)
# print(vList[1])

d = 2
vivmap = {}
eiemap = {}
for i in vList:
    vivmap[i] = {}
    eiemap[i] = {}
for i in vList:
    searchFront = [i]
    for j in range(d-1, 0, -1):
        newSearchFront = []
        for r in searchFront:
            triples = [];
            for s, p, o in g:
                if str(s) == r:
                    triples.append((str(s), str(p), str(o)))
            for triple in triples:
                newSearchFront.append(triple[2])
                if triple[2] not in vivmap[i]:
                    vivmap[i][triple[2]] = j
                if triple not in eiemap[i]:
                    eiemap[i][triple] = j
        searchFront = newSearchFront
print(vivmap)
print(eiemap)


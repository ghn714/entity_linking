import rdflib
from rdflib import Graph
g = Graph()
g.parse("kglol.rdf", format=rdflib.util.guess_format("kglol.rdf"))
v = set()
for s, p, o in g:
    v.add(str(s))
    v.add(str(o))
print(v)
vList = list(v)
print(vList)
print(vList[1])

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


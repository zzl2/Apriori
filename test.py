import apriori
mushDatSet=[line.split() for line in open('mushroom.dat').readlines()]





L,supportData=apriori.apriori(mushDatSet,0.4)

rule=apriori.generateRules(L,supportData,minConf=0.5)
for item in L[3]:
    if item.intersection('2'):
        print(item)

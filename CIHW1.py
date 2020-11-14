import random
import time
from matplotlib import pyplot as plt
from numpy.random import choice
#################### Get Input ####################
with open('input.txt', 'r') as f:
    capacityOfBag = int(f.readline())
    NumberOfGoods = int(f.readline())
    GoodsAndPrices = []
    for i in range(0,NumberOfGoods):
        x = (f.readline()).split(" ")
        GoodsAndPrices.append([int(x[0]), int(x[1])])
#################### Get Input ####################
    # print(GoodsAndPrices)
    # print("---------------------- Inputs ----------------------")
######## Make the random first population #########
    PrimaryPopulationNumber = int(f.readline())
    PrimaryPopulation = []
f.close()
start_time = time.time()
GoodsAndPricesCopy = []
for i in range(0, NumberOfGoods):
    GoodsAndPricesCopy.append(GoodsAndPrices[i])
for i in range(0, PrimaryPopulationNumber):
    PrimaryPopulation.append([])
    sum = 0
    while sum <= capacityOfBag:
        k = random.choice(GoodsAndPricesCopy)
        if sum + k[0] >capacityOfBag:
            break
        PrimaryPopulation[i].append(k)
        GoodsAndPricesCopy.remove(k)
        sum = sum + k[0]
    for i in range(0, NumberOfGoods):
        GoodsAndPricesCopy.append(GoodsAndPrices[i])
######## Make the random first population #########
# print(PrimaryPopulation)
# print("---------------- Primary Population ----------------")
################# 0 & 1 Converter #################
def Converter(NTCTFL):
    out = []
    for i in range(0, NumberOfGoods):
        out.append(0)
    for i in range(0, len(NTCTFL)):
        for j in range(0, NumberOfGoods):
            if NTCTFL[i] == GoodsAndPrices[j]:
                out[j] = 1
    return out
################# 0 & 1 Converter #################
################# Convert it back #################
def ConvertBack(NTCTFL):
    out = []
    for i in range(0, NumberOfGoods):
        if NTCTFL[i] == 1:
            out.append(GoodsAndPrices[i])
    return out
################# Convert it back #################
############### Evaluation Function ###############
def Evaluation(good):
    price = 0
    sum = 0
    for i in range(0, len(good)):
        price = price + good[i][1]
        sum = sum + good[i][0]
        if sum > capacityOfBag:
            price = 0
            break
    return price
def EvaluationAll(goods):
    values = []
    for i in range(0, len(goods)):
        values.append(Evaluation(goods[i]))
    return values
def Repeat(good):
    _size = len(good)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if good[i] == good[j] and good[i] not in repeated:
                repeated.append(good[i])
    return repeated
def DeleteRP(goods):
    i=0
    k2=len(goods)
    while i < k2:
        if len(Repeat(goods[i])) > 0:
            kk=goods[i]
            goods.remove(kk)
            k2=k2-1
            i=i-1
        i = i + 1
    return goods
############### Evaluation Function ###############
# print(PrimaryPopulation[0])
# print(Converter(PrimaryPopulation[0]))
##################### Mating ######################
def Mating(Mom, Dad):
    ml = []
    Mom2 = Converter(Mom)
    Dad2 = Converter(Dad)
    for i in range(0, NumberOfGoods):
        ml.append(i)
    k1 = random.choice(ml)
    ml.remove(k1)
    k2 = random.choice(ml)
    ml.clear()
    if k1 > k2:
        m = k1
        k1 = k2
        k2 = m
    ml.append(k1)
    ml.append(k2)
    p1 = []
    p2 = []
    for i in range(0, k1 + 1):
        p1.append(Mom2[i])
        p2.append(Dad2[i])
    for i in range(k1 + 1, k2 + 1):
        p1.append(Dad2[i])
        p2.append(Mom2[i])
    for i in range(k2 + 1, NumberOfGoods):
        p1.append(Mom2[i])
        p2.append(Dad2[i])
    l = []
    l.append(ConvertBack(p1))
    l.append(ConvertBack(p2))
    return l
################ Genetic mutation #################
def Mutation(Children):
    for i in range(0, len(Children)):
        k = random.uniform(0, 10)
        child = Converter(Children[i])
        if k < 3:
            m = random.randint(0, 9)
            if child[m] == 0:
                child[m] == 1
                sum = 0
                for j in range(0, NumberOfGoods):
                    if child[j] == 1:
                        sum = sum + GoodsAndPrices[j][0]
                if sum > capacityOfBag:
                    child[m] = 0
            else:
                child[m] == 0
        Children[i] = ConvertBack(child)
    return Children
################ Genetic mutation #################
##################### average #####################
def average(x):
    x2 = EvaluationAll(x)
    sum = 0
    for i in range(0, len(x2)):
        sum = sum + x2[i]
    return sum/len(x2)
##################### average #####################
##################### Mating ######################
sum = 0.0
ChoosingParents = []
ChoosingParentss = []
poss=[]
Children = []
NumberToDelete = 0
Avr = []
mx = []
for z in range(0, 1000):
    sum = 0
    poss.clear()
    Children.clear()
    ChoosingParents.clear()
    # evaluate
    values = EvaluationAll(PrimaryPopulation)
    # print(PrimaryPopulation)
    # print(values)
    for i in range(0, len(values)):
        sum = sum + values[i]
    # print(sum)
    for i in range(0, len(values)):
        poss.append((values[i]) / sum)
    q = []
    for j in range(0, len(PrimaryPopulation)):
        q.append(j)
    for i in range(0, PrimaryPopulationNumber):
        draw = choice(q, 1, p=poss)
        ChoosingParents.append(PrimaryPopulation[draw[0]])
    # choose parents
    # mating
    i = 0
    # print(len(ChoosingParents))
    while i < len(ChoosingParents):
        TwoChildren = Mating(ChoosingParents[i], ChoosingParents[i + 1])
        Children.append(TwoChildren[0])
        Children.append(TwoChildren[1])
        TwoChildren.clear()
        i = i + 2
    i = 0
    # mating
    # Genetic mutation
    Children2 = Mutation(Children)
    # Children.clear()
    # for ii in range(0, len(Children)):
    #     Children.append(Children2[ii])
    # Genetic mutation
    # add to primary population
    for i in range(0, len(Children2)):
        PrimaryPopulation.append(Children2[i])
    Children2.clear()
    # add to primary population
    # delete the old generation
    if z >= 1:
        PNT = len(PrimaryPopulation)
        while PNT > PrimaryPopulationNumber:
            PrimaryPopulation.pop(0)
            PNT = len(PrimaryPopulation)
    # delete the old generation
    print("--------------------------------")
    print(max(EvaluationAll(PrimaryPopulation)))
    print("--- %s seconds ---" % (time.time() - start_time))
    k = max(EvaluationAll(PrimaryPopulation))
    x=0
    for b in range(0, len(PrimaryPopulation)):
        if Evaluation(PrimaryPopulation[b]) == k:
            x=b
            break
    print(PrimaryPopulation[x])
    print(Converter(PrimaryPopulation[x]))
    print(average(PrimaryPopulation))
    Avr.append(average(PrimaryPopulation))
    print("--------------------------------")
plt.plot(Avr)
plt.show()
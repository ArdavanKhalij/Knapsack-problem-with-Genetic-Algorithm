import random
import time
from matplotlib import pyplot as plt
from numpy.random import choice
from tkinter import *
from tkinter import ttk
###################################################
root = Tk()
root.title("تمرین اوّل هوش محاسباتی")
space = Label(root, text=" ")
space1 = Label(root, text=" ")
space2 = Label(root, text=" ")
space3 = Label(root, text=" ")
space4 = Label(root, text=" ")
space5 = Label(root, text=" ")
space6 = Label(root, text=" ")
title = Label(root, text="تمرین اوّل هوش محاسباتی اردوان خلیج", font=('IRANYekan', '22'))
z1 = "ظرفیت کوله پشتی: "
g1 = "تعداد تکرار نسل: "
#################### Get Input ####################
with open('input.txt', 'r') as f:
    capacityOfBag = int(f.readline())
    zarfiat = Label(root, text=z1 + str(capacityOfBag), font=('IRANYekan', '20'))
    NumberOfGoods = int(f.readline())
    Generation = int(f.readline())
    Genera = Label(root, text=g1 + str(Generation), font=('IRANYekan', '20'))
    GoodsAndPrices = []
    for i in range(0,NumberOfGoods):
        x = (f.readline()).split(" ")
        GoodsAndPrices.append([int(x[0]), int(x[1])])
#################### Get Input ####################
######## Make the random first population #########
    PrimaryPopulationNumber = int(f.readline())
    PrimaryPopulation = []
f.close()
p1 = "تعداد جمعیت اوّلیه: "
pp = Label(root, text=p1 + str(PrimaryPopulationNumber), font=('IRANYekan', '20'))
l1 = "ورودی: "
ll = Label(root, text=l1 + str(GoodsAndPrices), font=('IRANYekan', '20'))
start_time = time.time()
GoodsAndPricesCopy = []
for i in range(0, NumberOfGoods):
    GoodsAndPricesCopy.append(GoodsAndPrices[i])
for i in range(0, PrimaryPopulationNumber):
    PrimaryPopulation.append([])
    Sum = 0
    while Sum <= capacityOfBag:
        k = random.choice(GoodsAndPricesCopy)
        if Sum + k[0] >capacityOfBag:
            break
        PrimaryPopulation[i].append(k)
        GoodsAndPricesCopy.remove(k)
        Sum = Sum + k[0]
    for i in range(0, NumberOfGoods):
        GoodsAndPricesCopy.append(GoodsAndPrices[i])
######## Make the random first population #########
################# 0 & 1 Converter #################
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
def Converter(NTCTFL):
    out = zerolistmaker(NumberOfGoods)
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
    Sum = 0
    for i in range(0, len(good)):
        price = price + good[i][1]
        Sum = Sum + good[i][0]
        if Sum > capacityOfBag:
            price = 0
            break
    return price
def EvaluationAll(goods):
    values = []
    for i in range(0, len(goods)):
        values.append(Evaluation(goods[i]))
    return values
############### Evaluation Function ###############
# print(PrimaryPopulation[0])
# print(Converter(PrimaryPopulation[0]))
##################### Mating ######################
def Mating(Mom, Dad):
    # ml = []
    Mom2 = Converter(Mom)
    Dad2 = Converter(Dad)
    # for i in range(0, NumberOfGoods):
    #     ml.append(i)
    ml = list(range(0, NumberOfGoods))
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
                Sum = 0
                for j in range(0, NumberOfGoods):
                    if child[j] == 1:
                        Sum = Sum + GoodsAndPrices[j][0]
                if Sum > capacityOfBag:
                    child[m] = 0
            else:
                child[m] == 0
        Children[i] = ConvertBack(child)
    return Children
################ Genetic mutation #################
##################### average #####################
def average(x):
    Sum = 0
    for i in range(0, len(x)):
        Sum = Sum + x[i]
    return Sum/len(x)
##################### average #####################
##################### Mating ######################
Sum = 0.0
ChoosingParents = []
ChoosingParentss = []
poss=[]
Children = []
NumberToDelete = 0
Avr = []
mx = []
for z in range(0, Generation):
    Sum = 0
    poss.clear()
    Children.clear()
    ChoosingParents.clear()
    # evaluate
    values = EvaluationAll(PrimaryPopulation)
    Avr.append(average(values))
    for i in range(0, len(values)):
        Sum = Sum + values[i]
    # print(Sum)
    for i in range(0, len(values)):
        poss.append((values[i]) / Sum)
    q = list(range(0, len(PrimaryPopulation)))
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
    # add to primary population
    for i in range(0, len(Children2)):
        PrimaryPopulation.append(Children2[i])
    Children2.clear()
    # add to primary population
    # delete the old generation
    if z >= 1:
        PNT = len(PrimaryPopulation)
        while PNT > 2*PrimaryPopulationNumber:
            PrimaryPopulation.pop(0)
            PNT = len(PrimaryPopulation)
    # delete the old generation
    # print("--------------------------------")
    # print(max(EvaluationAll(PrimaryPopulation)))
    # print("--- %s seconds ---" % (time.time() - start_time))
    # k = max(EvaluationAll(PrimaryPopulation))
    # x=0
    # for b in range(0, len(PrimaryPopulation)):
    #     if Evaluation(PrimaryPopulation[b]) == k:
    #         x=b
    #         break
    # print(PrimaryPopulation[x])
    # print(Converter(PrimaryPopulation[x]))
    # print(average(PrimaryPopulation))
    # Avr.append(average(PrimaryPopulation))
    # print("--------------------------------")
EndTime = (time.time() - start_time)
k = max(EvaluationAll(PrimaryPopulation))
x=0
for b in range(0, len(PrimaryPopulation)):
    if Evaluation(PrimaryPopulation[b]) == k:
        x=b
        break
end1 = Label(root, text="__________________________________________________________", font=('IRANYekan', '20'))
ans1 = Label(root, text="Answer: "+str(PrimaryPopulation[x]), font=('IRANYekan', '20'))
ans2 = Label(root, text="Answer: "+str(Converter(PrimaryPopulation[x])), font=('IRANYekan', '20'))
ans3 = Label(root, text="Maximum Value: "+str(Evaluation(PrimaryPopulation[x])), font=('IRANYekan', '20'))
ans4 = Label(root, text="Average: "+str(average(values)), font=('IRANYekan', '20'))
ans5 = Label(root, text="Time: "+str(EndTime)+" Seconds", font=('IRANYekan', '20'))
end2 = Label(root, text="__________________________________________________________", font=('IRANYekan', '20'))
plt.plot(Avr)
space.pack()
title.pack()
space1.pack()
space2.pack()
zarfiat.pack()
space3.pack()
Genera.pack()
space4.pack()
pp.pack()
space5.pack()
ll.pack()
space6.pack()
end1.pack()
ans1.pack()
ans2.pack()
ans3.pack()
ans4.pack()
ans5.pack()
end2.pack()
root.mainloop()
plt.show()

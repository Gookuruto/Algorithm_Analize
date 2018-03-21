import random
import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sbr


def random_choice(val1, val2, probability_of_val1):
    return val1 if random.random() < probability_of_val1 else val2


def El_vat(data):
    sum = 0
    for i in data:
        sum += i
    avg = sum / len(data)
    sum = 0
    for i in data:
        sum += (i - avg) ** 2
    var = (sum / (len(data)))
    return avg, var


def Election_p(p, n=0):
    slot = 0
    number_of_slots = 0
    round = 1
    k=0

   #if(len(p)==10):
    #   for k in p:
   #        print(k)

    if (n == 0):
        n = len(p)
    while (slot != 1):
        slot = 0
        number_of_slots = number_of_slots + 1
        for i in range(n):
            if (k >= len(p)):
                k = 0
                round += 1
            slot = slot + random_choice(1, 0, p[k])
            #print("prawdopodobienstwo= "+str(p[k]))
            #k += 1
            #if i==10:
             #   break
        k += 1

    return number_of_slots, round
def probability_round_one(data_round):
     sum=0
     for i in data_round:
         if i==1:
             sum+=1
     res=sum/len(data_round)
     return res


j = 0
p = []
p2 = []
while (j < 1000):
    p.append(0.001)
    j = j + 1

for i in range(int(math.ceil(np.log2(1000)))):
        p2.append(1 / (2 ** (i+1)))

j = 0
# listy dla danych o numerze slotu
data = []
data2 = []
data3 = []
data4 = []
#dane dla scenariusza 1
while (j < 1000):
    data.append(Election_p(p,1000)[0])
    j += 1
# listy dla danych w której rundzie znaleziono lidera
data_round = []
data_round = []
data_round3 = []
data_round4 = []
# Uzupelnianie list z danymi
j = 0
#dane dla scenariusza n=2
while (j < 1000):
    data2.append(Election_p(p2, 2)[0])
    if (data2[j] % len(p2) > 0):
        data_round.append(int((data2[j] / len(p2)) + 1))
    else:
        data_round.append(data2[j] / len(p2))
    j += 1
j = 0
#n=u/2
while (j < 1000):
    data3.append(Election_p(p2, 500)[0])
    if ((data3[j] % len(p2)) > 0):
        data_round3.append(int((data3[j] / len(p2)) + 1))
    else:
        data_round3.append(data3[j] / len(p2))
    j += 1
j = 0
#n=u
while (j < 1000):
    data4.append(Election_p(p2, 1000)[0])
    if (data4[j] % len(p2) > 0):
        data_round4.append(int((data4[j] / len(p2)) + 1))
    else:
        data_round4.append(data4[j] / len(p2))
    j += 1

# Wyliczenie wartosci oczekiwanej i wariancji
avg_s1, var_s1 = El_vat(data)
avg_s2_n2, var_s2_n2 = El_vat(data2)
avg_s2_n_div2, var_s2_n_div2 = El_vat(data3)
avg_s2_n, var_s2_n = El_vat(data4)

# Wyswietlenie wartości srednie i wariancji
print("średnia dla scenartiusza 1 " + str(avg_s1) + " wariancja " + str(var_s1))
print("średnia dla scenartiusza 2 przy n=2 " + str(avg_s2_n2) + " wariancja " + str(var_s2_n2))
print("średnia dla scenartiusza 2 przy n=u/2  " + str(avg_s2_n_div2) + " wariancja " + str(var_s2_n_div2))
print("średnia dla scenartiusza 2 przy n=u  " + str(avg_s2_n) + " wariancja " + str(var_s2_n))

print("prob for 2 = "+str(probability_round_one(data_round)))
print("prob for u/2= "+str(probability_round_one(data_round3)))
print("prob for u= "+str(probability_round_one(data_round4)))

# wytworzenie histogramów w osobnych figure



data.sort()
data2.sort()
data3.sort()
data4.sort()
print(data)
print(data2)
print(data3)
print(data4)
round=[]
round.append(probability_round_one(data_round))
round.append(probability_round_one(data_round3))
round.append(probability_round_one(data_round4))
data_y=[]
data_x=[]
how_much=0
first=1
for i in data:
    if i !=first:
        data_x.append(first)
        first=i;
        data_y.append(how_much)
        how_much=1
    else:
        how_much+=1

data_x2=[]
data_y2=[]
first=data2[0]
for i in data2:
    if i !=first:
        first=i;
        data_x2.append(i-1)
        if how_much>0:
            data_y2.append(how_much)
        how_much=1
    else:
        how_much+=1



data_x3=[]
data_y3=[]
first=data3[0]
for i in data3:
    if i !=first:
        first=i;
        data_x3.append(i-1)
        if how_much>0:
            data_y3.append(how_much)
        how_much=1
    else:
        how_much+=1



data_x4=[]
data_y4=[]
first=data4[0]
for i in data4:
    if i !=first:
        data_x4.append(first)
        first=i
        data_y4.append(how_much)
        how_much=1
    else:
        how_much+=1
print(data_x4)
print(data_y4)


#sbr.figure(1)
#sbr.barplot(data_x,data_y)
plt.bar(data_x,data_y)
plt.xticks(range(min(data_x), max(data_x)+1, 1))
#ax=plt.gca()
#plt.hist(data,align="mid",rwidth=0.5)
plt.title("scenario 1")

plt.figure(2)
plt.bar(data_x2,data_y2)
plt.xticks(range(min(data_x2), max(data_x2)+1, 1))
#plt.hist(data2,align="mid",rwidth=0.5)
plt.title("scenario 2 n=2")
plt.figure(3)
plt.bar(data_x3,data_y3)
plt.xticks(range(min(data_x3), max(data_x3)+1, 1))
#plt.hist(data3,align="mid",rwidth=0.5)
plt.title("scenario 2 n=u/2")
plt.figure(4)
plt.bar(data_x4,data_y4)
plt.xticks(range(min(data_x4), max(data_x4)+1, 1))
#plt.hist(data4,align="left",rwidth=0.5)
plt.title("scenario 2 n=u")
plt.figure(5)
plt.plot(round)

#plt.show()
plt.show()

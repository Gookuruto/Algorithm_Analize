import random
import matplotlib.pyplot as plt
import numpy as np
import math


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
    if (n == 0):
        n = len(p)
    while (slot != 1):
        slot = 0
        number_of_slots = number_of_slots + 1
        if(k>=len(p)):
            k=0
            round+=1
        for i in range(n):
            slot = slot + random_choice(1, 0, p[k])
            if (k >= len(p)):
                k = 0
                round += 1
        k+=1

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

for i in range(int(math.ceil(np.log2(1024)))):
        p2.append(1 / (2 ** (i+1)))

j = 0
# listy dla danych o numerze slotu
data = []
data2 = []
data3 = []
data4 = []
#dane dla scenariusza 1
while (j < 1000):
    data.append(Election_p(p)[0])
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
#n=2
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
y=[]
x=[]
for i in range(1024):
    if i>=2:
        x.append(i)
ele_round=[]
for i in range(1024):
    if i>=2:
        for j in range(1000):
            ele_round.append(Election_p(p2,i)[1])

        y.append(probability_round_one(ele_round))

print(y)
plt.plot(y)
'''
x=[]
for i in range(20):
    x.append(i)
plt.figure(1)
plt.hist(data,rwidth=0.2)
plt.title("scenario 1")

plt.figure(2)
plt.hist(data2,rwidth=0.2)
plt.title("scenario 2 n=2")
plt.xticks(x)
plt.figure(3)
plt.hist(data3,rwidth=0.2)
plt.xticks(x)
plt.title("scenario 2 n=u/2")
plt.figure(4)
plt.hist(data4,rwidth=0.2)
plt.xticks(x)
plt.title("scenario 2 n=u")
'''
plt.show()

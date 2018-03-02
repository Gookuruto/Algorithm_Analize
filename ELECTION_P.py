import random
import matplotlib.pyplot as plt
import numpy as np


def random_choice(val1, val2, probability_of_val1):
    return val1 if random.random() < probability_of_val1 else val2

def El_vat(data):
    sum = 0
    for i in data:
        sum += i
    avg = sum / len(data2)
    sum = 0
    for i in data:
        sum += (i - avg) ** 2
    var = np.sqrt((sum / len(data2)))
    return avg,var

def Election_p(p, n=0):
    slot = 0
    number_of_slots = 0
    round = 1
    j = 0
    if (n == 0):
        n = len(p)
    while (slot != 1):
        slot = 0
        number_of_slots = number_of_slots + 1
        for i in range(n):
            slot = slot + random_choice(1, 0, p[j])
            j += 1
            if (j >= len(p)):
                j = 0
                round += 1

    return number_of_slots, round


j = 0
p = []
p2=[]
while (j < 100):
    p.append(0.01)
    j = j + 1

for i in range(201):
    if i>=1:
        p2.append(1/(2**i))


j = 0
data = []
data2 = []
while (j < 1000):
    data.append(Election_p(p)[0])
    j += 1

data_round =[]
data_round =[]
data_round3 =[]
data_round4 =[]
data3=[]
data4=[]
j=0
while (j < 1000):
    data2.append(Election_p(p2,2)[0])
    if(data2[j]%len(p2)>0):
        data_round.append(int((data2[j]/len(p2))+1))
    else:
        data_round.append(data2[j]/len(p2))
    j += 1
j=0
while (j < 1000):
    data3.append(Election_p(p2,int(len(p2)/2))[0])
    if(data3[j]%len(p2)>0):
        data_round3.append(int((data3[j]/len(p2))+1))
    else:
        data_round3.append(data3[j]/len(p2))
    j += 1
j=0
while (j < 1000):
    data4.append(Election_p(p2,int(len(p2)))[0])
    if(data4[j]%len(p2)>0):
        data_round4.append(int((data4[j]/len(p2))+1))
    else:
        data_round4.append(data4[j]/len(p2))
    j += 1

avg_s1,var_s1=El_vat(data)
avg_s2_n2,var_s2_n2=El_vat(data2)
avg_s2_n_div2,var_s2_n_div2=El_vat(data3)
avg_s2_n,var_s2_n=El_vat(data4)

print("średnia dla scenartiusza 1 "+str(avg_s1)+" variancja "+str(var_s1))
print("średnia dla scenartiusza 2 przy n=2 "+str(avg_s2_n2)+" variancja "+str(var_s2_n2))
print("średnia dla scenartiusza 2 przy n=u/2  "+str(avg_s2_n_div2)+" variancja "+str(var_s2_n_div2))
print("średnia dla scenartiusza 2 przy n=u  "+str(avg_s2_n)+" variancja "+str(var_s2_n))



plt.hist(data)
plt.hist(data2)
plt.hist(data3)
plt.hist(data4)


plt.show()

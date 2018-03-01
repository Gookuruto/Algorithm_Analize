import random
import matplotlib.pyplot as plt
import numpy as np


def random_choice(val1, val2, probability_of_val1):
    return val1 if random.random() < probability_of_val1 else val2

def Election_p(p):
    slot=0
    number_of_slots=0
    while(slot!=1):
        slot = 0
        number_of_slots = number_of_slots+1
        for i in range(len(p)):
                slot=slot+random_choice(1, 0, p[i])
    return number_of_slots



j=0
p=[]
while(j<100):
    p.append(0.01)
    j=j+1

j=0
data=[]
while(j<1000):
    data.append(Election_p(p))
    j+=1


plt.hist(data)
plt.xlim(0, 30)

plt.show()
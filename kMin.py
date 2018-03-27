import zlib
import hashlib
import matplotlib.pyplot as plt
import multiprocessing as mp
import itertools as it
def zero_one_flt_sha256(a):
    y=a/2**256
    return y
def zero_one_float(a,bits):
    y = a/2**bits
    return y


def generate_M(n, shift):
    x = [None] * n
    for i in range(n):
        x[i] = i + shift
    return x


def kMin(k, h, M,bits):
    Arr = [1] * k
    temp = 1
    counter = 0
    for i in range(len(M)):
        temp = zero_one_float(abs(int(h(M[i].to_bytes(100, 'little')).hexdigest(), 16)),bits)
        if temp < Arr[-1] and not (temp in Arr):
            Arr[-1] = temp
            Arr.sort()
            #print(Arr[-1])
            counter += 1
    if Arr[-1] == 1:
        return counter
    else:
        # print(Arr[-1])
        return (k - 1) / Arr[-1]


def generate_many_M(how_many):
    x = []
    for i in range(how_many):
        if i == 0:
            x.append(generate_M(i + 1, 1))
        else:
            x.append(generate_M(i + 1, x[-1][-1] + 1))
    return x


def main():
    #pool=mp.Pool(mp.cpu_count())
    x = generate_many_M(1000)
    nn = [None] * len(x)
    xx = [None] * len(x)
    nn2 = [None] * len(x)
    nn3 = [None] * len(x)
    nn4 = [None] * len(x)
    nn5 = [None] * len(x)
    nn6 = [0.0] * len(x)
    #nn=pool.map(kMin,(2,hashlib.sha1,x))

    for j in range(len(x)):
        xx[j] = (len(x[j]))
        nn[j] = (kMin(2, hashlib.sha256, x[j],256) / len(x[j]))

    for j in range(len(x)):
        nn2[j] = (kMin(3, hashlib.sha256, x[j],256) / len(x[j]))
    for j in range(len(x)):
        nn3[j] = (kMin(10, hashlib.sha256, x[j],256) / len(x[j]))
    for j in range(len(x)):
        nn4[j] = (kMin(100, hashlib.sha256, x[j],256 )/ len(x[j]))
    for j in range(len(x)):
        nn5[j] = (kMin(400, hashlib.sha256, x[j],256) / len(x[j]))
    for j in range(len(x)):
        nn6[j] = (kMin(351, hashlib.sha256, x[j],256) / len(x[j]))
    succes = 0

    for u in range(1, 1000,10):
        for z in range(len(x)):
            #print(z)
            nn6[z] = (kMin(u, hashlib.sha256, x[z],256) / len(x[z]))
            if 0.9 <= nn6[z] <= 1.1:
                succes += 1
        if succes / len(nn6) >= 0.95:
            print("k dla ktorego 95% przypadkow zawiera sie w +- 10% " + str(u))  # sha1 k==751 sha256 k==391
            break
        else:
            succes = 0


    
    plt.figure(1)
    plt.plot(xx, nn, 'ro')
    plt.figure(2)
    plt.plot(xx, nn2, 'ro')
    plt.figure(3)
    plt.plot(xx, nn3, 'ro')
    plt.figure(4)
    plt.plot(xx, nn4, 'ro')
    plt.figure(5)
    plt.plot(xx, nn5, 'ro')

    plt.figure(6)
    plt.plot(xx,nn6,'ro')
    plt.show()
'''
x = generate_many_M(1000)
xx=[None]*len(x)
nn=[None]*len(x)
nn2=[None]*len(x)
for j in range(len(x)):
    xx[j] = (len(x[j]))
    nn[j] = (kMin(2, hashlib.sha512, x[j],512) / len(x[j]))

for j in range(len(x)):
    nn2[j] = (kMin(3, hashlib.sha1, x[j],160) / len(x[j]))

plt.plot(xx,nn,'ro')
plt.show()
'''
main()
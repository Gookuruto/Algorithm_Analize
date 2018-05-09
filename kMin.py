import zlib
import hashlib
import matplotlib.pyplot as plt
from math import log
import multiprocessing as mp
import itertools as it
import crc16
import crc8

def hash(hashfunc,x):
    h = int(hashfunc(x.to_bytes(100,'little')).hexdigest(),16)
    #hex_ = h.hexdigest()
    return h

def rightmost_binary_1_position(num):
  """The (number of trailing zeroes in the binary representation of num) + 1"""
  i = 0
  while (num >> i) & 1 == 0:
      i += 1
  return i + 1

def hyperloglog(numbers, bits_for_bucket_index=10):
    """Estimate the number of unique elements in `numbers`.
    4 <= bits_for_bucket_index <= 16
    http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf
    http://www.mathcs.emory.edu/~cheung/papers/StreamDB/Probab/1985-Flajolet-Probabilistic-counting.pdf
    """
    bucket_count = 2 ** bits_for_bucket_index
    buckets = [0] * bucket_count

    # Set up the data for "stochastic averaging"
    for v in numbers:
        hash_integer = hash(hashlib.sha1,v)
        i = hash_integer & (bucket_count - 1)
        w = hash_integer >> bits_for_bucket_index
        buckets[i] = max(buckets[i], rightmost_binary_1_position(w))

    a_m = .7213 / (1 + 1.079 / bucket_count)
    # Do the stochastic averaging.
    E = a_m * bucket_count ** 2 * sum(2 ** (-Mj) for Mj in buckets) ** (-1)
    # Small-range correction
    if E < (5 / 2.0 * bucket_count):
        V = len([b for b in buckets if b == 0])
        if V:
            E = bucket_count * log(bucket_count / float(V))
    # Large-range correction
    elif E > (1 / 30.0) * 2 ** 32:
        E = -(2 ** 32) * log(1 - (E / 2 ** 32))
    return E
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

def experiment(k,a,n):
    x=generate_many_M(n)
    succes=0
    nn5=[None]*n
    upper=0
    lower=0
    for i in range(len(x)):
        nn5[i] = (kMin(k, hashlib.sha1, x[i], 160) / len(x[i]))
    while True:
        succes=0
        for i in range(len(nn5)):
            if nn5[i]<=1+upper and nn5[i]>=1+lower:
                succes+=1
        if (succes/n)>=(1-(a/100)):
            break
        else:
            upper+=0.001
            lower-=0.001
    return lower,upper

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
        xx[j] = (len(x[j]))
        nn4[j] = (hyperloglog(x[j],4) / len(x[j]))
    '''
    for j in range(len(x)):
        nn2[j] = (kMin(3, hashlib.sha256, x[j],256) / len(x[j]))
    for j in range(len(x)):
        nn3[j] = (kMin(10, hashlib.sha256, x[j],256) / len(x[j]))
    for j in range(len(x)):
        nn4[j] = (kMin(100, hashlib.sha256, x[j],256 )/ len(x[j]))
    for j in range(len(x)):
        nn5[j] = (kMin(400, hashlib.sha256, x[j],256) / len(x[j]))
        '''
    for j in range(len(x)):
        nn5[j] = (kMin(int(2**10/32), hashlib.sha1, x[j],160) / len(x[j]))
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


    '''
    plt.figure(11)
    plt.plot(xx, nn, 'ro')
    plt.figure(12)
    plt.plot(xx, nn2, 'ro')
    plt.figure(13)
    plt.plot(xx, nn3, 'ro')
    plt.figure(14)
    plt.plot(xx, nn4, 'ro')
    plt.figure(15)
    plt.plot(xx, nn5, 'ro')
    '''
    plt.figure(15)
    plt.plot(xx,nn5,'ro')
    plt.figure(15)
    plt.plot(xx,nn4,'go')
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

def Chernoff(k,a,n):
    '''
    x=generate_many_M(n)
    nn=[None]*n

    for i in range(len(x)):
        nn[i]=(kMin(k,hashlib.sha1,x[i],160)/len(x[i]))
    '''
    return None,None

def Chebyshev(k,a,n):
    '''    x=generate_many_M(n)
    for i in range(len(x)):
        nn[i] = (kMin(k, hashlib.sha1, x[i], 160) / len(x[i]))
    '''
    return None,None

#print(experiment(400,5,1000))
main()
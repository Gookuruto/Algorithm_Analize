import zlib
import hashlib

def zero_one_float(a):
    y = "0." + str(a)
    y = float(y)
    return y

def generate_M(n,shift):
    x=[None]*n
    for i in range(n):
        x[i]=i+shift
    return x


def kMin(k,h,M):
    Arr=[1]*k
    temp=1
    counter=0
    for i in range(len(M)):
        temp=zero_one_float(abs(h(bytes(M[i]))))
        if Arr[-1]==1 and temp<Arr[-1]:
            Arr[-1]=temp
            Arr.sort()
            counter+=1
    if Arr[-1]==1:
        return counter
    else:
        print(Arr[-1])
        return (k-1)/Arr[-1]

def generate_many_M(how_many):
    x = []
    for i in range(how_many):
        if i == 0:
            x.append(generate_M(i + 1, 1))
        else:
            x.append(generate_M(i + 1, x[-1][-1] + 1))
    return x

def main():
    x=generate_many_M(10000)
    n=kMin(10,zlib.crc32,x[12])

    print(n)


main()
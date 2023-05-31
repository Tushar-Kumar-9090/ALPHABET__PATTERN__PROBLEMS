
#!-------------------------------------------------------------------------------------------------------------------------------------
#%                                                     Alphabet pattern
#!-------------------------------------------------------------------------------------------------------------------------------------
## Example-1
#%  A A A A A 
#%  B B B B 
#%  C C C 
#%  D D 
#%  E 
'''
n = int(input("Enter n Value: "))
dummy=65
num=n
for i in range(n):
    for j in range(num):
        print(chr(dummy),end=' ')
    dummy+=1
    num-=1
    print()
'''





## Example-2
#%  A A A A A
#%    B B B B
#%      C C C
#%        D D
#%          E
'''
n = int(input("Enter n Value: "))
dummy=65
num=n
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
    dummy+=1
    num-=1
    sp+=1
    print()
'''





## Example-3
#%  A
#%  B B
#%  C C C
#%  D D D D
#%  E E E E E
'''
n = int(input("Enter n Value: "))
dummy=65
num=1
for i in range(n):
    for j in range(num):
        print(chr(dummy),end=' ')
    dummy+=1
    num+=1
    print()
'''





## Example-4
#%          A
#%        B B
#%      C C C
#%    D D D D
#%  E E E E E
'''
n = int(input("Enter n Value: "))
dummy=65
num=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
    dummy+=1
    num+=1
    sp-=1
    print()
'''





## Example-5
#%  A B C D E
#%  F G H I
#%  J K L
#%  M N
#%  O
'''
n = int(input("Enter n Value: "))
dummy=65
num=n
for i in range(n):
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num-=1
    print()
'''




## Example-6
#%  A B C D E
#%    F G H I
#%      J K L
#%        M N
#%          O
'''
n = int(input("Enter n Value: "))
dummy=65
num=n
sp=0
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num-=1
    sp+=1
    print()
'''





## Example-7
#%  A
#%  B C
#%  D E F
#%  G H I J
#%  K L M N O  
'''
n = int(input("Enter n Value: "))
dummy=65
num=1
for i in range(n):
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num+=1
    print()
'''





## Example-8
#%         A
#%        B C
#%      D E F
#%    G H I J
#%  K L M N O
'''
n = int(input("Enter n Value: "))
dummy=65
num=1
sp=n-1
for i in range(n):
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num+=1
    sp-=1
    print()
'''






## Example-9
#%  A B C D E
#%  A B C D
#%  A B C
#%  A B
#%  A
'''
n = int(input("Enter n Value: "))
num=n
for i in range(n):
    dummy=65
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num-=1
    print()
'''





## Example-10
#%  A B C D E
#%    A B C D
#%      A B C
#%        A B
#%          A
'''
n = int(input("Enter n Value: "))
num=n
sp=0
for i in range(n):
    dummy=65
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num-=1
    sp+=1
    print()
'''





## Example-11
#%  A
#%  A B
#%  A B C
#%  A B C D
#%  A B C D E
'''
n = int(input("Enter n Value: "))
num=1
for i in range(n):
    dummy=65
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num+=1
    print()
'''





## Example-12
#%          A
#%        A B
#%      A B C
#%    A B C D
#%  A B C D E
'''
n = int(input("Enter n Value: "))
num=1
sp=n-1
for i in range(n):
    dummy=65
    for s in range(sp):
        print(' ',end=' ')
    for j in range(num):
        print(chr(dummy),end=' ')
        dummy+=1
    num+=1
    sp-=1
    print()
'''





## Example-13
#%          A 
#%        B A B
#%      C B A B C
#%    D C B A B C D
#%  E D C B A B C D E
'''
n = int(input("Enter n value: "))
sp=n-1
dummy=1
for i in range(n):
    num=i+65
    for i in range(sp):
        print(' ',end=' ')
    for j in range(dummy):
        print(chr(num),end=' ')
        if j<dummy//2:
            num-=1
        else:
            num+=1
    sp-=1
    dummy+=2
    print()
'''
A, B, C, D = [int(en) for en in input().split()]
n = 0
for i in range(A, C, A):
    if(i % B != 0 and C % i == 0 and D%i !=0):
        n = i
        break
print(n)

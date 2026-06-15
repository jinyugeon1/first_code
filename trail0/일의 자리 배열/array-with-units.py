A,B=map(int,input().split())
print(A,end=' ')
print(B,end=' ')
for i in range(8):
    print((A+B)%10,end=' ')
    A,B=B,(A+B)%10
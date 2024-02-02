N = int(input())
vet = []


for i in range (N-1):
    num = int(input())
    vet.append(num) 

vet.sort()
print(vet)
for i in range (N-1):
    if(i + 1 != vet[i]):
        print("faltando:",i+1)
        break
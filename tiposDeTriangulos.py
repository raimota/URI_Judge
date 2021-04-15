def quickSort(vet, inicio, fim):    
  if inicio < fim:
    posPivo =  separar(vet, inicio, fim)       
    quickSort(vet, inicio, posPivo - 1)
    quickSort(vet, posPivo + 1, fim)    
def separar(vet, inicio, fim):
  pivo = vet[fim]
  i = fim - 1
  f = inicio
  while i >= f:
    if vet[i] <= pivo:
      i-=1
    else:
      if pivo < vet[f]:
        f+=1
      else:
        troca = vet[i]
        vet[i] = vet[f]
        vet[f] = troca
        i-=1
        f+=1
  vet[fim] = vet[f]
  vet[f] = pivo
  return f
A, B, C = [float(x) for x in input().split(" ")]
if A < B + C and B < C + A and C < A + B:
  vet = [A, B, C]  
  quickSort(vet, 0, len(vet)-1)
  A = vet[0]
  B = vet[1]
  C = vet[2]   
  condTri ={
  "TRIANGULO RETANGULO": A*A == B*B+C*C,
  "TRIANGULO OBTUSANGULO": A*A > B*B + C*C,
  "TRIANGULO ACUTANGULO": A*A < B*B + C*C,
  "TRIANGULO EQUILATERO": A==B==C,
  "TRIANGULO ISOSCELES": (A==B or A==C or B==C) and not(A==B==C)   
  }
  for i, k in condTri.items():
    if k == True:
      print(i)
else:
  print("NAO FORMA TRIANGULO")
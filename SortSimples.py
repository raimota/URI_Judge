def quickSort(vet, inicio, fim):
  if inicio < fim:
    posPivo = separar(vet, inicio, fim)
    quickSort(vet, inicio, posPivo - 1)
    quickSort(vet, posPivo + 1, fim)
def separar(vet, inicio, fim):
  pivo = vet[inicio]
  i = inicio + 1
  f = fim
  while i <= f:
    if vet[i] <= pivo:
        i += 1
    else:
      if pivo < vet[f]:
          f -= 1
      else:
          troca = vet[i]
          vet[i] = vet[f]
          vet[f] = troca
          i += 1
          f -= 1
  vet[inicio] = vet[f]
  vet[f] = pivo
  return f
A, B, C = [int(x) for x in input().split(" ")]
vet = [A, B, C]
quickSort(vet, 0, len(vet) - 1)
for i in range(0, 3):
    print(vet[i])
print()
print(A)
print(B)
print(C)
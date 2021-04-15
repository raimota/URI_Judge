DDD = (
  "Brasilia", 61,
  "Salvador", 71,
  "Sao Paulo", 11,
  "Rio de Janeiro", 21,
  "Juiz de Fora", 32,
  "Campinas", 19,
  "Vitoria", 27,
  "Belo Horizonte", 31
)
N = int(input())
nulo = False
for pos in range(0, len(DDD)):
  if DDD[pos] == N:
    print(DDD[pos - 1])
    nulo = False
    break
  else:
    nulo = True
if nulo == True:
  print("DDD nao cadastrado")           
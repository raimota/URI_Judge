X = int(input())
Y = int(input())
if X < 0:
  X = X*(-1)
if Y <0:
  Y = Y*(-1)
if X <= Y:
  pass
else:
  aux = X
  X = Y
  Y = aux      
for i in range(X+1,Y):
  if i % 5 == 2 or i % 5 == 3:
    print(i)
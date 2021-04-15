A, B, C = [int(x) for x in input().split(" ")]
maiorAB = (A+B+abs(A-B))/2
if maiorAB > C:
  print(f"{int(maiorAB)} eh o maior")
else:
  print(f"{int(C)} eh o maior")

 

  



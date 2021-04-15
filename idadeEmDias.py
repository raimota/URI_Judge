contaAno = 0
contaMes = 0
contaDias = 0
nDias = int(input())
while True:
  if nDias >= 365:
    nDias-=365
    contaAno +=1
  elif nDias >= 30:
    nDias -= 30
    contaMes +=1
  elif nDias > 0:
    nDias -= 1
    contaDias +=1
  else:
    break  
print(f"{contaAno} ano(s)")
print(f"{contaMes} mes(es)")
print(f"{contaDias} dia(s)")        

 

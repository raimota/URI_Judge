N = int(input())
total = N
céd = 100
totcéd = 0
print(N)
while True:
    if total >= céd:
        total -= céd
        totcéd += 1        
    else:
        print(f'{totcéd} nota(s) de R$ {céd:.2f}'.replace(".", ","))       
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        elif céd == 1:
          céd = 0         
        totcéd = 0
        if céd == 0:
          break
                                  
        
         
                        
        
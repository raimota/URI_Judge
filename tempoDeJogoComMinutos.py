hi, mi, hf, mf = [int(x) for x in input().split(" ")]
hI = hi * 60 + mi
hF = hf * 60 + mf
tf = 0
if(hi <= hf):
  tf = hF - hI
  if(tf == 0):
    m = tf%60
    h = 24
  else:
    h = (tf - tf%60)/60
    m = tf%60     
else:
  tf = (1440 - hI)+hF
  h = (tf - tf % 60)/60
  m = tf % 60
if h < 0:
  h += 24  
print(f"O JOGO DUROU {int(h)} HORA(S) E {int(m)} MINUTO(S)")
print(tf)     
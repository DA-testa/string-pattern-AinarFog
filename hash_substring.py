# python3
def rInput():
  q1=str(input())
  if "I" in q1:
    q2=str(input()).rstrip()
    q3=str(input()).rstrip()
    return q2 ,q3
    
  elif "R" in q1:
    e="tests/06" 
    with open(e) as t:
      q2=t.readline().rstrip()
      q3=t.readline().rstrip()
    return q2, q3
    
def DaSplits(tupperware):
  protons=[]
  q0=len(tupperware[0])
  q1=hash(tupperware[0])
  q2=tupperware[1]
  for i in range(len(tupperware[1])-q0):
    q3=hash(q2[i:(i+q0)])
    if (q1==q3):
      protons.append(i)
  return protons
  
def Dave(richard):
  ron=""
  for i in range(len(richard)):
    ron=ron+str(richard[i])
    if(i<len(richard)):
      ron=ron+" "
  print(ron)
  
if (__name__ == '__main__'):
  Dave(DaSplits(rInput()))

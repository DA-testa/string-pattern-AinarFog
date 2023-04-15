# python3

def rInput():
  q1=str(input())
  if (q1.upper()=="I"):
    q2=str(input())
    q3=str(input())
    return q2 ,q3
  elif (q1.upper()=="R"):
    q0=str(input())
    e="test/"+q0
    with open(e) as t:
      q2=t.readline()
      q2=q2.replace("\n","")
      q3=t.readline()
    return q2, q3
def DaSplits(tupperware):
  protons=[]
  qu=tupperware[0]
  q0=len(qu)
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

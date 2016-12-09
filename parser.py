 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 03:59:50 2016

@author: R16

"""

import numpy as np
"""
rule 

<nonterminal> := <expr>
<expr> := <expr><op><expr> |
          (<expr><op><expr>) |
          <funct>(<expr>) |
          <terminal>
          
<terminal> := <numberlist>|<var>
<numberlist> := <number>|<number><numberlist> // belum dipakai
<var> := x1|x2|x3|.....|xn>
<number> := 0|1|2|3|....|9
<op> := +|-|*|/
<funct> := log|exp|abs|sqrt


"""
#token_map = {'+':'op','-':'op','*':'op','/':'op'}
#numberlist={'number'='<number>','numlist'}
#expr={'expr1':'<expr><op><expr>','expr2':(<expr><op><expr>)}
terminal={'number':'<number>','var':'<var>'}
number=[i for i in range(10)]
op=['+','-','*','/']
var=["x"+str(i+1) for i in range(15)]
funct=['log','abs','sqrt','exp']
#mapping rule
rules={'e': {'e1': ['e', 'o', 'e'], 'e2': ['(','e','o','e',')'], 'e3': 't'},
       't': {'t1': 'v','t2': 'n'}, 
       'o': {'o1':'+','o2':'-','o3':'*','o4':'/'},
       'v': {'v1':'x1','v2':'x2','v3':'x3'},
       'n': {'n0':'0','n1':'1','n2':'2','n3':'3','n4':'4','n5':'5','n6':'6','n7':'8','n9':'9'},
       'f': {'f1':'log','f2':'exp'}
       }
def stopping(aryfunct):
  for i in aryfunct:
    if i == 'e' or i == 't' or i == 'n' or i == 'v':
      return True
      break
    else:
      continue
  return False

def duplicate(bitstring):
  np.random.shuffle(bitstring)
  return bitstring
def prune(bitstring,nbitcut):
  return bitstring[0:len(bitstring)-nbitcut]
  
def run(kromosom):
  aryfunct=['e']
  fkrom=kromosom
  temp=kromosom
  while True:
    
    for i in range(len(temp)):#iterasi setiap bit kromosom
      aryfunct=evalpar(aryfunct,temp[i])#evaluasi string fungsi hasil berdasarkan input gen

    if len(aryfunct)>20:#berhenti ketika panjang string fungsi >20
      print(fkrom,"".join(np.hstack(aryfunct)))
      break
    
    else:
      
      if  stopping(aryfunct):
        temp = duplicate(kromosom)#duplikasi kromosom jika fungsi belum terbentuk sempurna
        fkrom=fkrom+temp
        
      else :#
        print(fkrom,"".join(np.hstack(aryfunct)))
        print(eval("".join(np.hstack(aryfunct))))      
        break
    

def evalpar(s,val):
  
  for i in range (len(s)):
    
    if s[i] in rules:
      
      s=s[:i+1]+np.hstack([list(rules.get(s[i]).get(list(rules.get(s[i]))[np.mod(val,len(list(rules.get(s[i]))))]))]).tolist()+s[i+1:]      
      s.pop(i)      
      break
    
    else: 
      
      continue
    
  s=np.hstack(np.array(s)).tolist()

  return s
  
if __name__ == "__main__":
  run([11,28])  
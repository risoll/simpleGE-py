# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 03:59:50 2016

@author: R16

"""

import numpy as np
from math import log,sqrt,exp
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
terminal={'number':'<number>','var':'<var>'}
number=[i for i in range(10)]
op=['+','-','*','/']
var=["x"+str(i+1) for i in range(15)]
funct=['log','abs','sqrt','exp']
#mapping rule
#rules={'e': {'e1': ['e', 'o', 'e'], 'e2': ['(','e','o','e',')'], 'e3': 't', 'e4': ['f','(','e',')']},
#       't': {'t1': 'v','t2': 'n'}, 
#       'o': {'o1':'+','o2':'-','o3':'*','o4':'/'},
#       'v': {'v1':'x1','v2':'x2','v3':'x3'},
#       'n': {'n0':'0','n1':'1','n2':'2','n3':'3','n4':'4','n5':'5','n6':'6','n7':'8','n9':'9'},
#       'f': {'f1':'log','f2':'exp','f3':'sqrt'}
#       }
       
rules={'e': {'e1': ['e', 'o', 'e'], 'e2': ['(','e','o','e',')'], 'e3': 'v','e4': ['(','e','o','e',')','p','(','e','o','e',')']}, 
       'o': {'o1':'>','o2':'<'},
       'p': {'op1' :'and','op2' :'or'},
       'v': {'v1':'x1[i]','v2':'x2[i]','v3':'x3[i]','v4':'x4[i]','v5':'x5[i]','v6':'x6[i]','v7':'x7[i]','v8':'x8[i]','v9':'x9[i]','x10':'x10[i]','x11':'x11[i]'},
       'n': {'n0':'0','n1':'1','n2':'2','n3':'3','n4':'4','n5':'5','n6':'6','n7':'8','n9':'9'},
#       'f': {'f1':'log','f2':'exp','f3':'sqrt'}
       }

def stopping(aryfunct):
  for i in aryfunct:
    if i == 'e' or i == 't' or i == 'n' or i == 'o' or i =='v' or i =='f' or i=='p'  :
      return True
      break
    else:
      continue
  return False

#fungsi duplikasi kromosom ketika saat mentok string yang terbentuk belum valid
def duplicate(bitstring):
  np.random.shuffle(bitstring)
  return bitstring
def prune(bitstring,nbitcut):
  return bitstring[0:len(bitstring)-nbitcut]
  
def run(kromosom):
  stackvar=[]#stack agar xn tidak duplikat
  aryfunct=['e']
  fkrom=kromosom
  temp=kromosom
  while True:
    
    for i in range(len(temp)):#iterasi setiap bit kromosom
      aryfunct=evalpar(aryfunct,temp[i],stackvar)[0]#evaluasi string fungsi hasil berdasarkan input gen
      stackvar=evalpar(aryfunct,temp[i],stackvar)[1]
#      print(stackvar)
#      stackvar=stackvar+evalpar(aryfunct,temp[i])[1]
#    if aryfunct[-1] == stackver[-1]:
#      aryfunct.pop()
    if len(aryfunct)>100:#berhenti ketika panjang string fungsi >30
#      print(fkrom,"".join(np.hstack(aryfunct)))
      break
    
    else:
      
      if  stopping(aryfunct):
        temp = duplicate(kromosom)#duplikasi kromosom jika fungsi belum terbentuk sempurna
        fkrom=fkrom+temp
        continue
      else :#
#        return(fkrom,"".join(np.hstack(aryfunct)))
        # print(eval("".join(np.hstack(aryfunct))))  
        return ''.join(np.hstack(aryfunct))
        # return temp[i]    
        break
    

def evalpar(s,val,stackvar):
  
  for i in range (len(s)):
    
    if s[i] in rules:
      
      #simpan target dari dict bnf
      ext=np.hstack([rules.get(s[i]).get(list(rules.get(s[i]))[np.mod(val,len(list(rules.get(s[i]))))])]).tolist()
      #jika karakter nya sama dengan akrakter terakir di stack maka break      
      if len(stackvar)>0 and stackvar[-1]==ext:

        break
      #jika karakter berbeda maka keluarkan elemen terakir dari stack
      elif len(stackvar)>0  and stackvar[-1]!=ext and ext[0] == 'x':
#        print(stackvar[-1])
        stackvar.pop(-1)
      #gabungkan karakter yang di generate ke string hasil bnf sebelumnya  
      s=s[:i+1]+ext+s[i+1:]      
      #karena masih ada karakter predecessornya ketika digabung maka char pred tersebut
      #dipop
      s.pop(i)
      #jika char 1 pada string terminal variabel(x1..xn) terbaca
      # maka dimasukkkan ke dalam stack
      if ext[0][0] == 'x':
#        print('pass')
        stackvar=stackvar+ext
      break
    
    #jika yang terbaca adalah karakter terminal maka bergerak ke karakter selanjutnya
    else: 
      
      continue
  s=np.hstack(np.array(s)).tolist()
#  print(np.array(stackvar)[0][0])
  return s,stackvar

    
if __name__ == "__main__":
  it =0
 #testing
  while it <1:
    s=run([np.random.randint(100) for i  in range(10)]) 
    if  stopping(str(s)):
      continue 
    else: 
      print(it+1," - ",s)
      it+=1
#      print(x,"-",run([np.random.randint(100) for i  in range(10)]) )
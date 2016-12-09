# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 00:58:53 2016

@author: R16
"""

import numpy as np
import operator_ as op
import parser_ as prs



def runit(kromosom):
  it=0
  kromosom=np.array(kromosom)

  intkromosom=op.decodebintoint(''.join(str(i) for  i in kromosom),4)#dekode
  s=prs.run(intkromosom)
  # print(s)
  while it<1:
    if prs.stopping(str(s)):
      # print(kromosom)
      kromosom_=np.random.randint(2,size=32)
      intkromosom=op.decodebintoint(''.join(str(i) for  i in kromosom_),4)
      s=prs.run(intkromosom)
    else:
      it+=1
  return s
  
def loadtoarray(filepath):
  mat= np.loadtxt(filepath,delimiter=',')
  mat=mat.T
  return mat
  
  
def fitness(mat,l,kromosom,nRow):
  n=0#nilai fitness dari nilai kebenaran ekspresi
  nx=1#nilai fitness dari jumlah  variabel di dalam ekspresi
  fit=0
  k=['x'+str(i+1) for i in range(l)]#list variabel
  i=0

  for i in range(l):
    locals()['x'+str(i+1)] = mat[i]#instansiansi variabel x1..xn buat diujikan ke ekpsresi hasil GE
  s=runit(kromosom)
  # s=("x3[i]<x2[i]") #uncommend juga ingin cek nilai fitness dari ekspresi ini
  # print ''.join((str, s))
  # for i in s:
  #       print("i",i)
#  print("s", eval(s))
  for i in range(nRow):
    #jika nilai ekpsresi true
    if eval(s)==True :
      # fitness ++
      n+=1
      
#    else: 
#      #lanjutkan ke baris data selanjutnya
#      continue
#    #untuk setiap variabel yang ada
#    for a in k:
#     #di cek ke setiap char di ekspresi
#     for b in s:
#               
#        if b==a:
#          
#          nx+=100#ketemu fitness +++
#          break# lanjut ke variabel x.. selanjutnya
#        else:
#          continue#lanjut ke char berikutnya
        
        
    fit=n/nRow * 100
     
  return fit
    
if __name__ == "__main__":
  #test
  mat=loadtoarray('./data/datasetfix.csv')
  krom = np.random.randint(2,size=32)
  r=13
  l=15
  print(fitness(mat,l,krom,r))
  
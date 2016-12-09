# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:22:52 2016

@author: R16
"""

import fitness as fitn
import numpy as np
import operator_ as op
import parser_ as ps
  
if __name__ == "__main__":
  limit=8
  cInt=8
  ep=0
  pc=0.85
  pm=0.15
  pC=limit*cInt
  jPop = 30
  epo = 100
  #inisiasi populasi
  pop=np.random.randint(2,size=(jPop,pC))
  m1=fitn.loadtoarray('./data/datasetfix.csv')
  nRow=13
  while(ep< epo):
    print("generasi",ep+1)
    #evaluasi fitness
    popfit=[fitn.fitness(m1,15,pop[i],nRow) for i in range(jPop)]
    #seleksi ortu
    matpool=op.rwheel(pop,popfit,jPop)
#    print(matpool)
    #elitism
    idx=np.array(popfit).argsort()[-2:][::-1]
    elite=np.array([matpool[idx[0]],matpool[idx[1]]])
#    saves=pop
    pop=np.zeros((1,pC),dtype='int')
    #crossover
    for c in range(int(jPop/2)):
        childs=op.crossover(matpool[2*c],matpool[2*c+1],pc)
        for c in childs:
            c=c.reshape(1,pC)
            pop=np.append(pop,c,axis=0)
#    print("k -",pop)
    pop = np.delete(pop,0,axis=0)
    
    #mutasi
#    for i in pop:
#        i=op.binarymutation(i,pm)
#    print('w = ',pop[0])
    #evalfit untuk survivor
#    print(op.decodebintoint(''.join(pop[0]),4))
#    save=pop
    popfit= [fitn.fitness(m1,15,pop[i],nRow) for i in range(jPop)]
    idx= np.array(popfit).argsort()[:2][::-1]
    pop = np.delete(pop,idx,axis=0)
    for e in elite:
        e=e.reshape(1,pC)    
        pop = np.append(pop,e,axis=0)
    
    bestchrom =elite[0]
    print('kromosom terbaik - ',bestchrom)
    print('fitnessnya - ',fitn.fitness(m1,15,bestchrom,nRow))
    print('ekspresinya - ',ps.run(op.decodebintoint(bestchrom,4)))

    ep+=1

#  print([x[0] for x in popfit])
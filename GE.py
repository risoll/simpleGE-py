# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:22:52 2016

@author: R16
"""

import fitness as fitn

  
limit=8
cInt=8
pC=limit*cInt
jPop = 50
epo = 100
#inisiasi populasi
pop=[np.random.randint(2,size=pC) for i in range(jPop)]
m1=loadtoarray('G:/ec/datasetfix.csv')
nRow=13
while(c < epo):
  
  popfit=[fitn.fitness(m1,15,pop[i],nRow) for i in range(jPop)]
  #hitungfitness
  
  #seleksiortu

  #crossover

  #mutasi

  #seleksisurvivor
  c+=1
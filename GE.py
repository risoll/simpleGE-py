# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:22:52 2016

@author: R16
"""

import fitness as fitn
import numpy as np
import operator_ as op
  
if __name__ == "__main__":
  limit=8
  cInt=8
  c=0
  pC=limit*cInt
  jPop = 20
  epo = 100
  #inisiasi populasi
  pop=[np.random.randint(2,size=pC) for i in range(jPop)]
  m1=fitn.loadtoarray('./data/datasetfix.csv')
  nRow=13
  while(c < epo):
    popfit=[fitn.fitness(m1,15,pop[i],nRow) for i in range(jPop)]
    for fit in popfit:
      print(c, fit[0])
    #hitungfitness
    

    #seleksiortu

    #crossover


    #mutasi

    #seleksisurvivor
    c+=1


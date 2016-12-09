# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 02:13:50 2016

@author: R16
"""
import random as rd
import numpy as np


def decodebintoint(chrom,lim):
  nChrom=[]
  y=0
  for nGen in range(int(len(chrom)/lim)):
    x=int(str(chrom[y:y+lim]),2)
    y+=lim
#    print(x)
    nChrom+=[x]
    
  return nChrom
    
  
def crossover(p1,p2,pc):
  if(rd.random()<=pc):
    tipot = rd.randint(1,len(p1)-1)  
    c1=np.append(p1[tipot:],p2[:tipot])
    c2=np.append(p1[:tipot]+p2[tipot:])
    return c1,c2
  else:
    return p1,p2
  
def binarymutation(kromosom,pm):
  for gen in range(len(kromosom)):
    if(rd.random()<=pm):
      if(kromosom[gen]==0):
        kromosom[gen]=1
      else:
        kromosom[gen]=0
    
    return kromosom

def rwheel(pop, fit, num):
#    print(fit)
    total_fitness = float(sum(fit))
    rel_fitness = [f/total_fitness for f in fit]
    #generate probabilitas kemunculan tiap individu
    probs = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    # populasi baru
    new_pop = []
    for n in range(num):
        r = np.random.rand()
        for (i, individual) in enumerate(pop):
            if r <= probs[i]:
                new_pop.append(individual)
                break
#    print(len(new_pop))
    return new_pop
    
def duplicate(bitstring):
  return bitstring+np.random.shuffle(bitstring)
def prune(bitstring,nbitcut):
  return bitstring[0:len(bitstring)-nbitcut]
  
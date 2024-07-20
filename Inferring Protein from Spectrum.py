# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:29:19 2024

@author: gbulb
"""
class find_protein_by_spectrum:
    def obtain_protein(list_,dict_):
        PROTEIN_STRING=''
        for i in range(len(list_)-1):
            for key in dict_.keys():
                if round(list_[i+1]-list_[i],3)==round(dict_[key],3) or round(list_[i+1]-list_[i],2)==round(dict_[key],3):
                   PROTEIN_STRING+=key
        return PROTEIN_STRING
if __name__=="__main__":     
  dict_={}
  dict_['A']= 71.03711
  dict_['C']= 103.00919
  dict_['D']= 115.02694
  dict_['E']= 129.04259
  dict_['F']= 147.06841
  dict_['G']= 57.02146
  dict_['H']= 137.05891
  dict_['I']= 113.08406
  dict_['K']= 128.09496
  dict_['L']= 113.08406
  dict_['M']= 131.04049
  dict_['N']= 114.04293
  dict_['P']= 97.05276
  dict_['Q']= 128.05858
  dict_['R']= 156.10111
  dict_['S']= 87.03203
  dict_['T']= 101.04768
  dict_['V']= 99.06841
  dict_['W']= 186.07931
  dict_['Y']= 163.06333     
  list_=[3524.8542,3710.9335,3841.974,3970.0326,4057.0646]
  print(find_protein_by_spectrum.obtain_protein(list_,dict_))
import pandas as pd
import numpy as np
import get_disease
import re

def stop_loop(new_sym,poss_d):
    first=get_disease.data_clean[poss_d[0]]["sym"]
    
    for i in poss_d:
    
        if first != get_disease.data_clean[i]["sym"]:
            return True
    
    return False

def chat(symptom_i,diseases=[]):
    k=2
    
    for i in get_disease.data_clean.keys():            
        if symptom_i in get_disease.data_clean[i]["sym"]:
            diseases.append(i)

    new_sym=get_disease.get_diseases(diseases)
    
    while(stop_loop(new_sym,diseases)):
        
        poss_d=diseases
        
        if get_disease.sym_id[new_sym]=="dont know":
            ans=0
        
        else:
            print('Are you suffering from ' + get_disease.sym_id[new_sym] + '?')
            ans=input()
            ans=int(ans)
        
        diseases=[]
        
        if ans==1:
            for i in poss_d:
                if new_sym in get_disease.data_clean[i]["sym"]:
                    diseases.append(i)
        else:
            for i in poss_d:
                if new_sym not in get_disease.data_clean[i]["sym"]:
                    diseases.append(i)
        
        if new_sym==-1:
            return [get_disease.disease_id[i] for i in diseases]
        
        new_sym=get_disease.get_diseases(diseases)

    return [get_disease.disease_id[i] for i in diseases]


symp = input()
diseases = chat(get_disease.id_sym[symp])
diseases = re.split('[\x01-\x1f\x7f]+', diseases[0])

print(diseases)
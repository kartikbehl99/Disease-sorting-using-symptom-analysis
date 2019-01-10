import pandas as pd
import numpy as np
import get_disease

def stop_loop(new_sym,poss_d):
    first=get_disease.data_clean[poss_d[0]]["sym"]
    for i in poss_d:
        if first != get_disease.data_clean[i]["sym"]:
            return True
    return False

def first_time(symptom_i):
    diseases=[]
    for i in get_disease.data_clean.keys():            
        if symptom_i in get_disease.data_clean[i]["sym"]:
#                 print(get_disease.data_clean[i]["sym"])
            diseases.append(i)
#     return [get_disease.disease_id[i] for i in diseases]    
#     print(len([get_disease.disease_id[i] for i in diseases]))
#     print(len(diseases))
    new_sym=get_disease.get_diseases(diseases)
    return new_sym,diseases

def next_sym(new_sym,diseases,ans):
#     while(stop_loop(new_sym,diseases)):
    poss_d=diseases
    if get_disease.sym_id[new_sym]=="dont know":
        ans=0
#         else:

#             yield(get_disease.sym_id[new_sym])
#             ans=int(input())
    diseases=[]
    if ans==1:
        for i in poss_d:
            if new_sym in get_disease.data_clean[i]["sym"]:
                diseases.append(i)
    else:
        for i in poss_d:
            if new_sym not in get_disease.data_clean[i]["sym"]:
                diseases.append(i)
#         print(len([get_disease.disease_id[i] for i in diseases]))
    if ans==-1:
        return new_sym,diseases
    new_sym=get_disease.get_diseases(diseases)
      
    return new_sym,diseases

inp = input()
new_sym=int(input())
# diseases=[int(i) for i in input().split()]

if inp != 0 and inp !=1:
    new_sym,diseases=first_time(get_disease.id_sym[inp])
    print(get_disease.sym_id[new_sym],new_sym,diseases)

if stop_loop(new_sym,diseases)==False:
    print(get_disease.sym_id[new_sym],new_sym,diseases)

new_sym,diseases=next_sym(new_sym,diseases,ans=inp)
print(get_disease.sym_id[new_sym],new_sym,diseases)

def chat(symptom_i,diseases=[]):
    k=2
    for i in get_disease.data_clean.keys():            
        if symptom_i in get_disease.data_clean[i]["sym"]:
#                 print(get_disease.data_clean[i]["sym"])
            diseases.append(i)
#     return [get_disease.disease_id[i] for i in diseases]    
#     print(len([get_disease.disease_id[i] for i in diseases]))
    print(len(diseases))
    new_sym=get_disease.get_diseases(diseases,k)
    k+=1
    
    while(stop_loop(new_sym,diseases)):
        poss_d=diseases
        if get_disease.sym_id[new_sym]=="dont know":
            ans=0
        else:
            print(get_disease.sym_id[new_sym])
            ans=int(input())
        diseases=[]
        if ans==1:
            for i in poss_d:
                if new_sym in get_disease.data_clean[i]["sym"]:
                    diseases.append(i)
        else:
            for i in poss_d:
                if new_sym not in get_disease.data_clean[i]["sym"]:
                    diseases.append(i)
        print(len([get_disease.disease_id[i] for i in diseases]))
        if new_sym==-1:
            return [get_disease.disease_id[i] for i in diseases]
        new_sym=get_disease.get_diseases(diseases)
        k+=1
    return [get_disease.disease_id[i] for i in diseases]

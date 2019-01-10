import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

data=pd.read_csv("./diffsydiw.csv")
dia_t=pd.read_csv("./dia_t.csv")
disease_id={}
id_disease={}

for i in range(dia_t.shape[0]):

    if pd.isna(dia_t.iloc[i].did):
        continue
    
    disease_id[dia_t.iloc[i].did]=dia_t.iloc[i].diagnose
    id_disease[dia_t.iloc[i].diagnose]=dia_t.iloc[i].did

sym_t=pd.read_csv("./sym_t.csv")
sym_id={}
id_sym={}

for i in range(sym_t.shape[0]):
    if pd.isna(sym_t.iloc[i].symptom):
        sym_id[sym_t.iloc[i].syd]="Drooling"
        continue
    sym_id[sym_t.iloc[i].syd]=sym_t.iloc[i].symptom
    id_sym[sym_t.iloc[i].symptom]=sym_t.iloc[i].syd

data_clean={}
for i in range(data.shape[0]):
    if pd.isna(data.iloc[i].did) or pd.isna(data.iloc[i].syd) :
        continue
    if data.iloc[i].did not in data_clean.keys():
        data_clean[data.iloc[i].did]={}
        data_clean[data.iloc[i].did]["sym"]=[]
        data_clean[data.iloc[i].did]["sym"].append(data.iloc[i].syd)
    else:
        data_clean[data.iloc[i].did]["sym"].append(data.iloc[i].syd)

len(disease_id),len(sym_id),len(data_clean)

dim=max(sym_id.keys())+1
def one_hot(diseases):
    data=[]
    disease_id=[]
    for i in diseases:
        arr=np.zeros(dim)
        for j in data_clean[i]["sym"]:
            arr[int(j)]=1
        data.append(arr)
        disease_id.append(i)
    return np.array(data),disease_id            

# symptom_i=163

def get_diseases(diseases,k=2):
    print(diseases)
    data,ids=one_hot(diseases)
    Dtree=RandomForestClassifier(max_depth=1,criterion='entropy')
    # print(data.shape)
    Dtree.fit(data,ids)

    return np.argmax(Dtree.feature_importances_)
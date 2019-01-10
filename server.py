import pandas as pd
import numpy as np
import get_disease
import re
from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

global nsym,d
nsym = ''
d = []
CORS(app, resources={r"/*": {"origins": "*"}})

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
            diseases.append(i)
    print(diseases)
    new_sym=get_disease.get_diseases(diseases)
    return new_sym,diseases

def next_sym(new_sym,diseases,ans):
    poss_d=diseases
    if new_sym == 0:
        ans = 0
    elif get_disease.sym_id[new_sym]=="dont know":
        ans=0

    diseases=[]
    
    if ans==1:
        for i in poss_d:
            if new_sym in get_disease.data_clean[i]["sym"]:
                diseases.append(i)
    
    else:
        for i in poss_d:
            if new_sym not in get_disease.data_clean[i]["sym"]:
                diseases.append(i)

    if ans==-1:
        return new_sym,diseases

    new_sym=get_disease.get_diseases(diseases)
      
    return new_sym,diseases

def chat(symptom_i,diseases=[]):
    k=2

    for i in get_disease.data_clean.keys():            
        
        if symptom_i in get_disease.data_clean[i]["sym"]:
            diseases.append(i)

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


@app.route('/message', methods=['POST'])
def start():
    global nsym,d
    print('i ran')
    print(request.form)
    sym = request.form['msg']
    print(sym)
    nsym,d = first_time(get_disease.id_sym[sym])
    print('i ran 2')
    print(get_disease.sym_id[nsym])

    # if get_disease.sym_id[nsym] == "don't know":
    #     print('dont know')
    #     start2()
    #     return

    return 'Are you suffering from ' + get_disease.sym_id[nsym] + '?'

@app.route('/message_new', methods=['POST'])
def start2():
    global nsym,d
    print('i ran')
    print(request.form)
    sym = request.form['msg']
    print(sym)
    ans = 0
    if sym=='Yes'or sym=='yes':
        ans = 1
    n2sym,d2 = next_sym(nsym,d,ans)
    nsym = n2sym
    d = d2
    if stop_loop(nsym,d)==True:
        return 'Are you suffering from ' + get_disease.sym_id[nsym] + '?'
    else:
        dis = [get_disease.disease_id[i] for i in d][0]
        dis = re.split('[\x01-\x1f\x7f]+', dis)
        if(len(dis) > 1):
            return "You might be suffering from "+ dis[0] + ' or ' + dis[1]
        
        return "You might be suffering from "+ dis

app.run('0.0.0.0', 5000)
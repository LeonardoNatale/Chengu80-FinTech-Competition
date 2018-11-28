import pickle
import pandas as pd
import numpy as np

data = pd.read_csv("../data/Average credit card spending across factors.csv")

pdf_edu = {};
pdf_mar = {};
pdf_kids = {};
pdf_ten = {};

for i in [0]+list(range(10,17)):
    dum = []
    dum1 = []
    dum.append(0);
    for j in range(20,81,5):
        dum.append(len(data.index[(data['education_level'] == i) & (data['age'] < j)]))
    for j in range(1,len(dum)):
        dum1.append(dum[j]-dum[j-1])
    pdf_edu[i] = dum1;

for i in list(range(1,6)):
    dum = []
    dum1 = []
    dum.append(0)
    for j in range(20,81,5):
        dum.append(len(data.index[(data['marital_status'] == i) & (data['age'] < j)]))
    for j in range(1,len(dum)):
        dum1.append(dum[j]-dum[j-1])
    pdf_mar[i] = dum1;

for i in list(range(0,15)):
    dum = []
    dum1 = []
    dum.append(0)
    for j in range(20,81,5):
        dum.append(len(data.index[(data['number_of_kids'] == i) & (data['age'] < j)]))
    for j in range(1,len(dum)):
        dum1.append(dum[j]-dum[j-1])
    pdf_kids[i] = dum1;

for i in [1,2,4,5,6]:
    dum = []
    dum1 = []
    dum.append(0)
    for j in range(20,81,5):
        dum.append(len(data.index[(data['house_tenure'] == i) & (data['age'] < j)]))
    for j in range(1,len(dum)):
        dum1.append(dum[j]-dum[j-1])
    pdf_ten[i] = dum1;


print(pdf_edu)
print(pdf_mar) 
print(pdf_kids)
print(pdf_ten)

with open ('../data/pdf_mar', 'wb') as f:
    pdf_mar = pickle.dump(pdf_mar,f);     

with open ('../data/pdf_edu', 'wb') as f:
    pdf_edu = pickle.dump(pdf_edu,f);     

with open ('../data/pdf_ten', 'wb') as f:
    pdf_ten = pickle.dump(pdf_ten,f);     

with open ('../data/pdf_kids', 'wb') as f:
    pdf_kids = pickle.dump(pdf_kids,f);     


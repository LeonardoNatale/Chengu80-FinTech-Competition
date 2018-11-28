import csv
import pickle
import pandas as pd
from math import pow


num_clusters = 8;
def growth_rate_matrix(var):
    growth = []
    for i in range(0,num_clusters):
        stri = "../data/df_x_inc";
        stri = stri + str(i) + ".csv";
        data = pd.read_csv(stri);
        avg_income = [];
        dum = []
        for age in range(0,14):
            ind = data.index[(data['age'] >= (15 + age*5)) & (data['age'] < 20 + age*5)]
            avg_income.append(data[var][ind.values].mean())
    
        for i in range(len(avg_income)-1):
            if(avg_income[i] == 0 or avg_income[i+1] == 0):
                dum.append(0.05);
            if(avg_income[i] == 0 or avg_income[i+1] == 0):
                dum.append(0);
                continue;
            dum.append(pow(avg_income[i+1]/avg_income[i], 1/5)-1)     
        growth.append(dum);
    return(growth);


def future_values(Y, cluster):

    cols = ['age','marital_status','sex','number_of_kids','house_tenure','occupation','education_level']
    Y = Y[cols].astype(float)
    X = Y.iloc[0][1:].as_matrix().reshape(1,-1);
    cl = cluster.predict(X)[0];
    for i in range(len(Y.index)-1):
        age = Y['age'][i];
        i_g = income_growth_rate[cl][int((age-15)/5)]
        k_g = kids_growth_rate[cl][int((age-15)/5)]
        e_g = education_growth_rate[cl][int((age-15)/5)]
        h_g = house_growth_rate[cl][int((age-15)/5)]
        m_g = mar_growth_rate[cl][int((age-15)/5)]
    	
        Y['age'][i+1] = Y['age'][i]+1
        #Y['income_past12months'][i+1] = Y['income_past12months']*(1+i_g)
        Y['number_of_kids'][i+1] = (Y['number_of_kids'][i]*(1+k_g))
        Y['education_level'][i+1] = (Y['education_level'][i]*(1+e_g))
        Y['house_tenure'][i+1] = (Y['house_tenure'][i]*(1+h_g))
        Y['marital_status'][i+1] = (Y['marital_status'][i]*(1+h_g))
    return Y



income_growth_rate = growth_rate_matrix('income_past12months');
kids_growth_rate = growth_rate_matrix('number_of_kids');
education_growth_rate = growth_rate_matrix('education_level');
house_growth_rate = growth_rate_matrix('house_tenure');
mar_growth_rate = growth_rate_matrix('marital_status');

with open ('../data/model', 'rb') as f:
    cluster = pickle.load(f);     

with open ('../data/df', 'rb') as f:
    data1 = pickle.load(f);     
X = data1.drop(columns = ['date'])
X['education_level'][0] = 12
X = future_values(X,cluster)
print(X)

#with open ('../data/growth_pred', 'wb') as f:
#    pickle.dump([income_g,kids_g,edu_g,house_g,mar_g],f);     

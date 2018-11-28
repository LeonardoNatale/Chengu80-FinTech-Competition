
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE
import math

if __name__ =='__main__':
    df_x_inc =  pd.read_csv('Average credit card spending across factors.csv', header=0, index_col=0)
    # pd.read_csv('Data dictionary personal IPO.csv', header=0, index_col=0)
    #factorRefTable = pd.read_csv('Factors reference table.csv', header=0, index_col=0)
    #issueDetails = pd.read_csv('Issue details.csv', header=0, index_col=0)
    #df_issuer_profile = pd.read_csv('Issuer profile.csv', header=0, index_col=0)
    # print(df_x_inc.columns.tolist())

    df_x_inc = df_x_inc[df_x_inc['age'] >= 18]
    df_x_inc = df_x_inc[df_x_inc['age'] < 60]
    df_x_inc = df_x_inc.dropna(axis=0)
    df_x_inc['income_past12months'] = np.where(df_x_inc['income_past12months'] <= 0, 1, df_x_inc['income_past12months'])

    #df_x_inc['income_past12months'] = np.log(df_x_inc['income_past12months'])
    df_x_inc['age'] = df_x_inc['age'] - 18
    df_x_inc['is_male'] = np.where(df_x_inc['sex'] == 1, 1, 0)
    df_x_inc['is_ms_married'] = np.where(df_x_inc['marital_status'] == 1, 1, 0)
    df_x_inc['is_ms_widowed'] = np.where(df_x_inc['marital_status'] == 2, 1, 0)
    df_x_inc['is_ms_divorced'] = np.where(df_x_inc['marital_status'] == 3, 1, 0)
    df_x_inc['is_ms_seperated'] = np.where(df_x_inc['marital_status'] == 4, 1, 0)
    df_x_inc['is_ms_never'] = np.where(df_x_inc['marital_status'] == 5, 1, 0)
    df_x_inc['is_oc_admin'] = np.where(df_x_inc['occupation'] == 1, 1, 0)
    df_x_inc['is_oc_teach'] = np.where(df_x_inc['occupation'] == 2, 1, 0)
    df_x_inc['is_oc_pro'] = np.where(df_x_inc['occupation'] == 3, 1, 0)
    df_x_inc['is_oc_adsup'] = np.where(df_x_inc['occupation'] == 4, 1, 0)
    df_x_inc['is_oc_sale_ret'] = np.where(df_x_inc['occupation'] == 5, 1, 0)
    df_x_inc['is_oc_sale_bus'] = np.where(df_x_inc['occupation'] == 6, 1, 0)
    df_x_inc['is_oc_tech'] = np.where(df_x_inc['occupation'] == 7, 1, 0)
    df_x_inc['is_oc_prot'] = np.where(df_x_inc['occupation'] == 8, 1, 0)
    df_x_inc['is_oc_phs'] = np.where(df_x_inc['occupation'] == 9, 1, 0)
    df_x_inc['is_oc_other'] = np.where(df_x_inc['occupation'] == 10, 1, 0)
    df_x_inc['is_oc_mach'] = np.where(df_x_inc['occupation'] == 11, 1, 0)
    df_x_inc['is_oc_trans'] = np.where(df_x_inc['occupation'] == 12, 1, 0)
    df_x_inc['is_oc_hand'] = np.where(df_x_inc['occupation'] == 13, 1, 0)
    df_x_inc['is_oc_mech'] = np.where(df_x_inc['occupation'] == 14, 1, 0)
    df_x_inc['is_oc_cons'] = np.where(df_x_inc['occupation'] == 15, 1, 0)
    df_x_inc['is_edu_f'] = np.where(df_x_inc['education_level'] == 10, 1, 0)
    df_x_inc['is_edu_n'] = np.where(df_x_inc['education_level'] == 11, 1, 0)
    df_x_inc['is_edu_hs'] = np.where(df_x_inc['education_level'] == 12, 1, 0)
    df_x_inc['is_edu_sc'] = np.where(df_x_inc['education_level'] == 13, 1, 0)
    df_x_inc['is_edu_as'] = np.where(df_x_inc['education_level'] == 14, 1, 0)
    df_x_inc['is_edu_bs'] = np.where(df_x_inc['education_level'] == 15, 1, 0)
    df_x_inc['is_edu_ms'] = np.where(df_x_inc['education_level'] == 16, 1, 0)
    #default never attand school
    df_x_inc['is_house_with_mort'] = np.where(df_x_inc['house_tenure'] == 1, 1, 0)
    df_x_inc['is_house_without_mort'] = np.where(df_x_inc['house_tenure'] == 2, 1, 0)
    df_x_inc['is_rented'] = np.where(df_x_inc['house_tenure'] == 4, 1, 0)
    df_x_inc['is_occupied'] = np.where(df_x_inc['house_tenure'] == 5, 1, 0)
    df_x_inc['const'] = 1
    #default student housing
    df_x_inc = df_x_inc.drop(columns=['sex', 'avg_credit_card_spending_semi_annual', 'house_tenure', 'education_level', 'occupation', 'sex', 'marital_status'])


    #two factor testing
    df_x_inc['age*kids'] = df_x_inc['age']*df_x_inc['number_of_kids']
    df_x_inc['age*edu_hs'] = df_x_inc['age']*df_x_inc['is_edu_hs']
    df_x_inc['age*edu_sc'] = df_x_inc['age']*df_x_inc['is_edu_sc']
    df_x_inc['age*edu_as'] = df_x_inc['age']*df_x_inc['is_edu_as']
    df_x_inc['age*edu_bs'] = df_x_inc['age']*df_x_inc['is_edu_bs']
    df_x_inc['age*edu_ms'] = df_x_inc['age']*df_x_inc['is_edu_ms']
    df_x_inc['age*ms_married'] = df_x_inc['age']*df_x_inc['is_ms_married']
    df_x_inc['age*ms_never'] = df_x_inc['age']*df_x_inc['is_ms_never']
    '''
    df_x_inc['age*oc_admin'] = df_x_inc['age']*df_x_inc['is_oc_admin']
    df_x_inc['age*oc_pro'] = df_x_inc['age']*df_x_inc['is_oc_pro']
    df_x_inc['age*oc_teach'] = df_x_inc['age']*df_x_inc['is_oc_teach']
    df_x_inc['age*oc_adsup'] = df_x_inc['age']*df_x_inc['is_oc_adsup']
    df_x_inc['age*oc_sale_ret'] = df_x_inc['age']*df_x_inc['is_oc_sale_ret']
    df_x_inc['age*oc_sale_bus'] = df_x_inc['age']*df_x_inc['is_oc_sale_bus']
    df_x_inc['age*oc_tech'] = df_x_inc['age']*df_x_inc['is_oc_tech']
    df_x_inc['age*oc_prot'] = df_x_inc['age']*df_x_inc['is_oc_prot']
    df_x_inc['age*oc_phs'] = df_x_inc['age']*df_x_inc['is_oc_phs']
    df_x_inc['age*oc_other'] = df_x_inc['age']*df_x_inc['is_oc_other']
    df_x_inc['age*oc_mach'] = df_x_inc['age']*df_x_inc['is_oc_mach']
    df_x_inc['age*oc_trans'] = df_x_inc['age']*df_x_inc['is_oc_trans']
    df_x_inc['age*oc_hand'] = df_x_inc['age']*df_x_inc['is_oc_hand']
    df_x_inc['age*oc_mech'] = df_x_inc['age']*df_x_inc['is_oc_mech']
    df_x_inc['age*oc_cons'] = df_x_inc['age']*df_x_inc['is_oc_cons']
    '''

    #df_x_inc['age*ms_divorced'] = df_x_inc['age'] * df_x_inc['is_ms_divorced']
    est = sm.OLS(df_x_inc['income_past12months'], df_x_inc.drop(columns=['income_past12months'])).fit()
    print(est.summary())

    y = df_x_inc[['income_past12months']]
    x = df_x_inc.drop(columns=['income_past12months'])
    #x = df_x_inc[['age']]
    ten_fold = RepeatedKFold(n_splits=10, n_repeats=1)
    mse_ols = []
    for train_index, test_index in ten_fold.split(x):
        x_train = x.iloc[train_index]
        x_test = x.iloc[test_index]
        y_train = y.iloc[train_index]
        y_test = y.iloc[test_index]
        est = sm.OLS(y_train, x_train).fit()
        y_test_predict = est.predict(x_test)
        mse_ols.append(MSE(y_test, y_test_predict))

    mse_ols_avg = math.sqrt(np.average(mse_ols))
    print(mse_ols_avg)
    df_x_inc.to_csv('data.csv')








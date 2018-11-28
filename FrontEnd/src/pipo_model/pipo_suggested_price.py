import pandas as pd
import numpy as np

def suggestedPrice(age_o, sex_o, ms_o, nk_o, oc_o, ed_o, ho_o, inc_o):
    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    df_issue = pd.DataFrame(data=date, columns=['date'])
    df_issue['age'] = age_o
    df_issue['sex'] = sex_o
    df_issue['marital_status'] = ms_o
    df_issue['number_of_kids'] = nk_o
    df_issue['occupation'] = oc_o
    df_issue['education_level'] = ed_o
    df_issue['house_tenure'] = ho_o

    df_issuer = pd.DataFrame(data=date, columns=['date'])
    df_issuer['age'] = age_o
    df_issuer['sex'] = sex_o
    df_issuer['marital_status'] = ms_o
    df_issuer['number_of_kids'] = nk_o
    df_issuer['occupation'] = oc_o
    df_issuer['education_level'] = ed_o
    df_issuer['house_tenure'] = ho_o
    #df_issuer['income_past12months'] = inc_o
    
    df_issuer['age'] = df_issuer['age'] - 18
    df_issuer['is_male'] = np.where(df_issuer['sex'] == 1, 1, 0)
    df_issuer['is_ms_married'] = np.where(df_issuer['marital_status'] == 1, 1, 0)
    df_issuer['is_ms_widowed'] = np.where(df_issuer['marital_status'] == 2, 1, 0)
    df_issuer['is_ms_divorced'] = np.where(df_issuer['marital_status'] == 3, 1, 0)
    df_issuer['is_ms_seperated'] = np.where(df_issuer['marital_status'] == 4, 1, 0)
    df_issuer['is_ms_never'] = np.where(df_issuer['marital_status'] == 5, 1, 0)
    df_issuer['is_oc_admin'] = np.where(df_issuer['occupation'] == 1, 1, 0)
    df_issuer['is_oc_teach'] = np.where(df_issuer['occupation'] == 2, 1, 0)
    df_issuer['is_oc_pro'] = np.where(df_issuer['occupation'] == 3, 1, 0)
    df_issuer['is_oc_adsup'] = np.where(df_issuer['occupation'] == 4, 1, 0)
    df_issuer['is_oc_sale_ret'] = np.where(df_issuer['occupation'] == 5, 1, 0)
    df_issuer['is_oc_sale_bus'] = np.where(df_issuer['occupation'] == 6, 1, 0)
    df_issuer['is_oc_tech'] = np.where(df_issuer['occupation'] == 7, 1, 0)
    df_issuer['is_oc_prot'] = np.where(df_issuer['occupation'] == 8, 1, 0)
    df_issuer['is_oc_phs'] = np.where(df_issuer['occupation'] == 9, 1, 0)
    df_issuer['is_oc_other'] = np.where(df_issuer['occupation'] == 10, 1, 0)
    df_issuer['is_oc_mach'] = np.where(df_issuer['occupation'] == 11, 1, 0)
    df_issuer['is_oc_trans'] = np.where(df_issuer['occupation'] == 12, 1, 0)
    df_issuer['is_oc_hand'] = np.where(df_issuer['occupation'] == 13, 1, 0)
    df_issuer['is_oc_mech'] = np.where(df_issuer['occupation'] == 14, 1, 0)
    df_issuer['is_oc_cons'] = np.where(df_issuer['occupation'] == 15, 1, 0)
    df_issuer['is_edu_f'] = np.where(df_issuer['education_level'] == 10, 1, 0)
    df_issuer['is_edu_n'] = np.where(df_issuer['education_level'] == 11, 1, 0)
    df_issuer['is_edu_hs'] = np.where(df_issuer['education_level'] == 12, 1, 0)
    df_issuer['is_edu_sc'] = np.where(df_issuer['education_level'] == 13, 1, 0)
    df_issuer['is_edu_as'] = np.where(df_issuer['education_level'] == 14, 1, 0)
    df_issuer['is_edu_bs'] = np.where(df_issuer['education_level'] == 15, 1, 0)
    df_issuer['is_edu_ms'] = np.where(df_issuer['education_level'] == 16, 1, 0)
    #default never attand school
    df_issuer['is_house_with_mort'] = np.where(df_issuer['house_tenure'] == 1, 1, 0)
    df_issuer['is_house_without_mort'] = np.where(df_issuer['house_tenure'] == 2, 1, 0)
    df_issuer['is_rented'] = np.where(df_issuer['house_tenure'] == 4, 1, 0)
    df_issuer['is_occupied'] = np.where(df_issuer['house_tenure'] == 5, 1, 0)
    df_issuer['const'] = 1
    #default student housing
    df_issuer = df_issuer.drop(columns=['sex', 'house_tenure', 'education_level', 'occupation', 'sex', 'marital_status'])

    #two factor testing
    df_issuer['age*kids'] = df_issuer['age']*df_issuer['number_of_kids']
    df_issuer['age*edu_hs'] = df_issuer['age']*df_issuer['is_edu_hs']
    df_issuer['age*edu_sc'] = df_issuer['age']*df_issuer['is_edu_sc']
    df_issuer['age*edu_as'] = df_issuer['age']*df_issuer['is_edu_as']
    df_issuer['age*edu_bs'] = df_issuer['age']*df_issuer['is_edu_bs']
    df_issuer['age*edu_ms'] = df_issuer['age']*df_issuer['is_edu_ms']
    df_issuer['age*ms_married'] = df_issuer['age']*df_issuer['is_ms_married']
    df_issuer['age*ms_never'] = df_issuer['age']*df_issuer['is_ms_never']

    '''
    get model
    '''

    df_forecast = pd.DataFrame(data=date, columns=['date'])
    # change next line with model result
    df_forecast['forecast'] = df_issuer['age']
    return(df_issue)

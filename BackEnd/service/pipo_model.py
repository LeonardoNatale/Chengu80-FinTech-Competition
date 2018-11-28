from service.pipo_model import pipo_forecast as forecast
from service.pipo_model import pipo_pricing_functions as functions
from service.pipo_model import pipo_suggested_price as suggested_price

def forecastWrap(dictx):
    oc = dictx['intended_occupation']
    inc = dictx['income_past12months']
    sex = dictx['sex']
    age = dictx['age']
    ms = dictx['marital_status']
    nk = dictx['number_of_kids']
    ed = dictx['education_level']
    ho = dictx['house_tenure']
    student_flag = (dictx['occupation'] == 10)
    pv = suggested_price.suggestedPrice(age, sex, ms, nk, oc, ed, ho, inc, student_flag, data_full, ols)
    print(pv[0])
    suggested_price.suggestedPrice(34, 1, 5, 9, 1, 13, 4, 84300, 0, data_full, ols)
    forecast.estVarianceT10(data_full, 30, 12)
    return pv

    data_full = forecast.readData()


    ols = forecast.forecast(data_full)
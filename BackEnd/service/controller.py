from service.pipo_model import pipo_forecast as forecast
from service.pipo_model import pipo_suggested_price as suggested_price
from service.pipo_model import pipo_pricing_functions

class Controller(object):
    def __init__(self):
        self.data_full = forecast.readData()
        self.ols = None

    def train(self):
        self.ols = forecast.forecast(self.data_full)


    def forecastWrap(self, d1, d2):
        oc = d1['intended_occupation']
        inc = d1['income_past12months']
        sex = d1['sex']
        age = d1['age']
        ms = d1['marital_status']
        nk = d1['number_of_kids']
        ed = d1['education_level']
        ho = d1['house_tenure']
        student_flag = (d1['occupation'] == 10)
        pv = suggested_price.suggestedPrice(age, sex, ms, nk, oc, ed, ho, inc, student_flag, self.data_full, self.ols)
        pv[1] = pv[1]*d2['credit_card_percentage']/d2['shares_offering']
        pv[0] = pv[0]*d2['credit_card_percentage']/d2['shares_offering']
        sigma = forecast.estVarianceT10(self.data_full, age, ed)
        K_call = round(d2['call_option']*pv[1], 2)
        K_put = round(d2['put_option']*pv[1])
        C = 0
        if K_call > 0:
            C = pipo_pricing_functions.blackScholesCall(sigma, 10, K_call, 0.03, pv[0])
        P = 0
        npv = pv[0] - C
        # print(npv, pv[0])
        # print(d2['call_option'])

        return {"share_price": round(npv,2), "K_call": K_call, "K_put": 0}
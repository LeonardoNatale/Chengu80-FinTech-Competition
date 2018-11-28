import requests
import json

r = requests.post('http://127.0.0.1:5000/register/issuer', data = {"age":47, "marital_status":5, "sex":2, "number_of_kids":0, "occupation":15, "education_level":15,
                                                   "house_tenure":4, "income_past12months": 125456.68, "avg_credit_card_spending_semi_annual":6839.04})


url = 'http://127.0.0.1:5000/register/issuer'
payload =  {"age":47,
            "marital_status":5,
            "sex":2,
            "number_of_kids":0,
            "occupation":15,
            "education_level":15,
            "house_tenure":4,
            "income_past12months": 125456.68,
            "avg_credit_card_spending_semi_annual":6839.04}

headers = {'Content-Type': "application/json"}

r = requests.post(url, json={'json_payload': payload})

print(r)
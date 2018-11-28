import pandas as pd
import numpy as np
import pickle
from pipo_model import pipo_forecast as forecast
from pipo_model import pipo_pricing_functions as functions
from pipo_model import pipo_suggested_price as suggested_price

def main():
    a = suggested_price.suggestedPrice(30, 1, 1, 1, 1, 1, 1, 1)
    print(a.columns)
    with open('df','wb') as f:
        pickle.dump(a,f);    

main()



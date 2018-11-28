from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import csv


engine = create_engine("postgresql://group2:123456@10.240.61.106:5432/group2")
engine.execute('DROP TABLE "Issuer"')

data = pd.read_csv("ftp://10.240.61.80/Chengdu80 PPIO case material/Average credit card spending across factors.csv")
data.columns = ['name', 'age', 'marital_status', 'sex', 'number_of_kids', 'occupation','education_level', 'house_tenure', 'income_past12months','avg_credit_card_spending_semi_annual']
sql_data = data.to_sql("Issuer", engine,index_label="id")
engine.execute('ALTER TABLE "Issuer" ADD PRIMARY KEY ("id");');

engine.execute('DROP TABLE "IPO"')
data_ipo = pd.read_excel("ftp://10.240.61.80/Chengdu80 PPIO case material/Issue details.xlsx")
sql_data_ipo = data.to_sql("IPO", engine)
engine.execute('ALTER TABLE "IPO" ADD FOREIGN KEY ("Issuer.id");');




print(engine.execute('SELECT * FROM "Issuer"').fetchall())



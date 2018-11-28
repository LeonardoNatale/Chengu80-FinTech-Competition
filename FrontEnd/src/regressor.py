import numpy
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

#data = pd.read_csv("../data/Average credit card spending across factors.csv")
data = pd.read_csv("../data/data.csv")

y = data.income_past12months;
y = y.values;
data = data.drop(columns = ['income_past12months'])
#data = data.drop(columns = ['avg_credit_card_spending_semi_annual'])
data = data.drop(columns = ['id'])

X = data;
X = X.values
print(X.shape)

def baseline_model():
    model = Sequential()
    model.add(Dense(42, input_dim=42, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
# Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

seed = 7
numpy.random.seed(seed)
estimator = KerasRegressor(build_fn=baseline_model, epochs = 20, batch_size=5, verbose=0)


kfold = KFold(n_splits = 20, random_state = seed)
results= cross_val_score(estimator, X, y, cv=kfold);
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

X_train = X[:-1000]
y_train = y[:-1000]
X_test = X[-1000:]
y_test = y[-1000:]
estimator.fit(X_train, y_train)
prediction = estimator.predict(X_test)
train_error =  numpy.abs(y_test - prediction)
mean_error = numpy.mean(train_error)
min_error = numpy.min(train_error)
max_error = numpy.max(train_error)
std_error = numpy.std(train_error)
print(mean_error,min_error,max_error,std_error)

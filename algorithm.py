import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

df = pd.read_excel('dshouse.xlsx')

x = df.drop('harga', axis=1)
y = df['harga']

# Misalkan Anda memiliki data dan target (X, y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Membuat dan melatih model XGBoost
xg_reg = xgb.XGBRegressor()
xg_reg.fit(x_train, y_train)



def input_attribute():
# Tipe Rumah, LT, LB, M2, Lantai, KT, KM, Listrik, Fasilitas Perum, Carpot, Univ, TransporUmum, Perkantoran, Market, Akses TOLL, Security
    input_data = np.array([[6, 50, 50, 2000, 2, 2, 2, 2200, 3, 1, 6, 2, 7, 7, 4, 1]])
    return xg_reg.predict(input_data)[0]

print(input_attribute())

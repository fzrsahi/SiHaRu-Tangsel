import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import locale

df = pd.read_excel('dshouse.xlsx')

x = df.drop('harga', axis=1)
y = df['harga']

features = ['TipeRumah', 'Lantai', 'KamarTidur', 'KamarMandi', 'carpot']
x = df[features]
y = df['harga']

# Membuat dan melatih model XGBoost
model = xgb.XGBRegressor(objective='reg:squarederror')
model.fit(x, y)


def input_attribute( tipe_rumah, jumlah_lantai, tipe_kamar, tipe_kamar_mandi, tipe_garasi):
    # Mengubah tipe data menjadi integer (jika sesuai dengan kebutuhan model)
    input_data = np.array([[tipe_rumah, jumlah_lantai, tipe_kamar, tipe_kamar_mandi, tipe_garasi]], dtype=np.int64)
    formatted_rupiah = format_to_rupiah(model.predict(input_data)[0])
    return formatted_rupiah


def format_to_rupiah(angka):
    locale.setlocale(locale.LC_ALL, 'id_ID')  # Mengatur locale ke Indonesia (id_ID)
    formatted = locale.currency(angka, grouping=True, symbol=False)
    return formatted

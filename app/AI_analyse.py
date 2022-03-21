import joblib 
import math

def analyze(data): # AIモデルから予測結果を取得
     model = joblib.load('./model_Classifier.pkl') 
     pred = model.predict(data)
     return pred

def percent(data): # 調査結果画面での％表示
     model = joblib.load('./model_Regression.pkl')
     pred = model.predict(data)
     pred = math.ceil(pred*100)
     return pred
     
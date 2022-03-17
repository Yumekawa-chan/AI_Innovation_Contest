import joblib 

def analyze(data): # AIモデルから予測結果を取得
     model = joblib.load('./model.pkl')
     pred = model.predict(data)
     return pred

def percent(data): # 調査結果画面での％表示
     lonely = int(data[0][5])
     age = int(data[0][0])
     sick = int(data[0][2])
     money = int(data[0][7])


     if lonely == 0: # 孤独度（7~40）
          lonely = 40
     elif lonely == 1:
          lonely = 30
     elif lonely == 2:
          lonely = 15
     else:
          lonely = 7
     
     if 74 < age: # 年齢（0~30）
          age = 30
     elif 67 < age < 75:
          age = 20
     elif 59 < age < 68:
          age = 10
     else:
          age = 0
     
     if sick == 0: # 過去の重病の有無（0 or 20）
          sick = 0
     else:
          sick = 20
     
     if money > 1999: # 貯金（5 or 10）
          money = 5
     else:
          money = 10
     
     return lonely + age + sick + money

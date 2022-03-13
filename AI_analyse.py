import joblib 

def analyze(data):
     model = joblib.load('./model.pkl')
     pred = model.predict(data)
     return pred

def percent(data):
     lonely = int(data[0][5]) # 0:25,1:15,2:8,3:0
     age = int(data[0][0]) # 75~:25,70~74:15,65~69:8,~64:0
     sick = int(data[0][2]) # 1:25,0:0
     excersice = int(data[0][6]) # 0:25,1~2:15,3~:0

     if lonely == 0:
          lonely = 25
     elif lonely == 1:
          lonely = 15
     elif lonely == 2:
          lonely = 8
     else:
          lonely = 0
     
     if 74 < age:
          age = 25
     elif 69 < age < 75:
          age = 15
     elif 64 < age < 70:
          age = 8
     else:
          age = 0
     
     if sick == 0:
          sick = 0
     else:
          sick = 1
     
     if excersice == 0:
          excersice = 25
     elif 1 <= excersice <= 2:
          excersice = 15
     else:
          excersice = 0
     
     return lonely + age + sick + excersice

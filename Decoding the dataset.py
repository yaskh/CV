import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("SCIT dataset.csv")

Districts = ('East', 'West', 'South', 'Central', 'Malir', 'Korangi')
dataset = pd.DataFrame
print(data.head())

for value in data["District"]:
    print(Districts[value-1])
    data["Distrit"].replace(data["Distrit"],Districts[value-1])
#    print(data["District"])
    
#data.District.replace(1,"East")

districts = sorted(data.District.unique())
for i in range(len(Districts)):
    data.District = data.District.replace(districts[i],Districts[i])
    
Transport = ("Van","Bus","Car","Bike","Walk")
transport = sorted(data['Mode of transport'].unique())
for i in range(len(Transport)):
    data['Mode of transport'] = data['Mode of transport'].replace(transport[i],Transport[i])

data.to_csv("scit_updated.csv",index = False,columns = ["Roll No","District","Time to reach","Mode of transport","Distance"])

X = data["Distance"]
y = data["Time to reach"]

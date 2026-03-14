import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

# Read dataset 
df = pd.read_csv('dataset.csv')
df = pd.get_dummies(df, columns=['Gender'])

features = df.drop(['Spending Score (1-100)','CustomerID'], axis=1)
print(features)
target = df['Spending Score (1-100)']

random = RandomForestRegressor(n_estimators=3)
random.fit(features,target)

with open('model.pkl','wb') as file:
    pickle.dump(random,file)
    print("Model saved successfully")
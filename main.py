import pandas as pd
from sklearn.linear_model import LinearRegression

# Creating a tiny dataset manually so you don't need a CSV yet
data = {
    'SqFt': [1000, 1500, 2000, 2500],
    'Price': [200000, 300000, 400000, 500000]
}

df = pd.DataFrame(data)
x=df[['SqFt']]
y=df['Price']
model = LinearRegression()
model.fit(x,y)

new_house_size = [[2800]]
predicted_price = model.predict(new_house_size)
print (f"Prediction for 2800 SqFt: ${predicted_price[0]:,.2f}")
# Final push for Project 1


accuracy = model.score(x, y)
print(f"Model Accuracy (R² Score): {accuracy * 100:.2f}%")
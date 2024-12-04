import pandas as pd
import matplotlib.pyplot as plt


data_path = "scraping.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(data_path)

x = df['Brand'].unique().astype(str)
y = df['Average Rating'].astype(str)
# y = df.groupby('Brand')['Average Rating']
# y= df['Average Rating']
y=y[:80]
x =x[:80]
print("y",y)
print("x",x)
print("x",type(x))
print("rating",type(y))
plt.xlabel('Brand Name', fontsize=18)
plt.ylabel('Rating',fontsize=16)
plt.bar(x,y)


plt.show()
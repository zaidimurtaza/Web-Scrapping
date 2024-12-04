import pandas as pd
import matplotlib.pyplot as plt

# Assuming the data is in a CSV file named 'product_data.csv'
df = pd.read_csv('noon-yoga-products.csv')


# a. Most Expensive Product

def bar_chart_min_price_product(n):
    """
    Generates a bar chart of the n cheapest products.

    Parameters:
    n (int): Number of lowest-priced products to display.

    Functionality:
    - Sorts products by 'Sales Price' in ascending order.
    - Handles missing values, formats prices, and customizes chart appearance.
    - Displays a bar chart with product prices on the y-axis.
    """
    product_name_list=[]
    product_price_list=[]
    df['Sales Price'] = pd.to_numeric(df['Sales Price'].replace({',': ''}, regex=True), errors='coerce')
    cheapest_products = df.sort_values(by='Sales Price', ascending=True).head(n)
    for index, row in cheapest_products.iterrows():
        product_name = row['Name']
        price = row['Sales Price']
        # Handle missing values and format the price
        if pd.isnull(price):
            price = "N/A"
        else:
            price = f"{float(str(price).replace(',', '')):.2f}"
        product_name_list.append(product_name)
        product_price_list.append(price)
    plt.xlabel('Products', fontsize=18,color='#008080')
    plt.ylabel('<-Min Product Prices (AED) Max->', fontsize=14,color='#008080')
    plt.bar(product_name_list[:n],product_price_list[:n])
    plt.xticks([])
    plt.title("Minimum Prices of Products",color='#DAA520',fontweight='bold',y=1)
    plt.show()

def bar_chart_max_price_product(n):
    """
    Generates a bar chart of the n most expensive products.

    Parameters:
    n (int): Number of top-priced products to display.

    Functionality:
    - Sorts products by 'Sales Price' in descending order.
    - Handles missing values, formats prices, and customizes chart appearance.
    - Displays a bar chart with product prices on the y-axis.
    """

    product_name_list=[]
    product_price_list=[]
    df['Sales Price'] = pd.to_numeric(df['Sales Price'].replace({',': ''}, regex=True), errors='coerce')
    most_expensive = df.sort_values(by='Sales Price', ascending=False).head(n)
    for index, row in most_expensive.iterrows():
        product_name = row['Name']
        price = row['Sales Price']
        # Handle missing values and format the price
        if pd.isnull(price):
            price = "N/A"
        else:
            price = f"{float(str(price).replace(',', '')):.2f}"
        product_name_list.append(product_name)
        product_price_list.append(price)
    plt.figure(figsize=(10, 6))
    # plt.tight_layout()
    plt.bar(product_name_list[:n],product_price_list[:n])
    # plt.ylim(0,1865)
    plt.xlabel('Products', fontsize=18,color='#008080')
    plt.ylabel('<-Max Product Prices (AED) Min->', fontsize=14,color='#008080')
    plt.xticks([])
    plt.xticks(rotation=45, ha='right')
    plt.title("Maximum Prices of Products ",color='#DAA520',fontweight='bold',y=1)
    plt.show()
    
def pie_chart_brand_and_product(n):
    """
    Displays a pie chart of the top n brands and their market share percentage.

    Parameters:
    n (int): The number of top brands to display.

    """
    brand_counts = df['Brand'].value_counts()
    brand_list = brand_counts.index.tolist()
    count_list = brand_counts.values.tolist()
    adjusted_list = ([0.05,.2] * (n // len([0.05,.2]) + 1))[:n]
    plt.pie(count_list[:n], labels=brand_list[:n],radius=1.2,autopct='%0.01f%%', shadow=True,explode=adjusted_list)
    # plt.subplots_adjust(left=-0.12)
    plt.subplots_adjust(top=0.8)
    plt.title(f"{n} BRAND'S AND THEIR MARKET % AGE",color='#008080',fontweight='bold', y=1.2)
    plt.show()

n = 12
# pie_chart_brand_and_product(n)
# bar_chart_min_price_product(n)
# bar_chart_max_price_product(n)
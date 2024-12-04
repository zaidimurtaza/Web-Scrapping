from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import datetime
import os

# Initialize WebDriver (replace with your preferred browser)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/")  # Replace with the actual URL


 # Execute JavaScript to simulate clicking on the desired option or triggering the necessary action

def Scrape_one_page():
    # Find the span element by its class name
    span_element = driver.find_element(By.CSS_SELECTOR, ".sc-63bc8e9b-7.hZVQUI.grid")
    card_container = span_element.find_elements(By.CSS_SELECTOR, ".sc-57fe1f38-1.gYzxDm.grid")
    s_price = []
    o_price = []
    avg_rating = []
    rating_count = []
    sponsered= []
    image_text = []
    sku = []
    brand= []
    link_list = []
    title_ =  []
    sale_price = span_element.find_elements(By.CSS_SELECTOR,"strong[class='amount']")
    for pr in sale_price:
        s_price.append(pr.text)
    for each_card in card_container:
        try :
            is_sponsered = each_card.find_element(By.CSS_SELECTOR, "div[class='sc-d96389d1-24 kXouJu']")
            if is_sponsered.text.strip() == "Sponsored":
                sponsered.append("Y")
            else: 
                sponsered.append("N")
        except: 
            sponsered.append("N")
        try:
            old_price = each_card.find_element(By.CSS_SELECTOR,"span[class='oldPrice']")
            o_price.append(old_price.text)
        except: 
            o_price.append("None")
        try :
            time.sleep(0.020)
            rating_avg = each_card.find_element(By.CSS_SELECTOR,"div[class='sc-d96389d1-30 hyHyxq']")
            if rating_avg.text.strip()!="":
                avg_rating.append(rating_avg.text)
            else:avg_rating.append("None")
        except :
            avg_rating.append("None")
        try:
            time.sleep(0.020)
            rating_in_num = each_card.find_element(By.CSS_SELECTOR,"div[class='sc-d96389d1-30 hyHyxq'] span")
            rating_count.append(rating_in_num.text)
        except: 
            rating_count.append("None")
        try :
            image_tags = each_card.find_element(By.CSS_SELECTOR, "div[data-qa='product-noon-express'] img")
            alt_text = image_tags.get_attribute("alt")
            if alt_text.strip() == 'noon-express':
                image_text.append("Y")
            else:image_text.append("N")
        except:
            image_text.append("none")
            
            
    # Extract the text content from the span element
    anchor_tag = span_element.find_elements(By.CSS_SELECTOR, "div[class='sc-57fe1f38-0 eSrvHE'] a")
    for a in anchor_tag:
        link = a.get_attribute("href")
        sku.append(link.split("/")[5])
        link_list.append(f"{link}\n")


    
    product_name_divs = span_element.find_elements(By.CSS_SELECTOR, "div[data-qa='product-name']")
    for div in product_name_divs:
        # Find the title element within the div
        title_element = div.get_attribute("title")
        brand.append(title_element.strip().split()[0])
        title_.append(title_element.strip()) 
        # Extract the text content and remove leading/trailing whitespace
    if len(link_list) < len(image_text):
        link_list += ['None'] * (len(image_text) - len(link_list))
    elif len(link_list) > len(image_text):
        link_list = link_list[:len(s_price)]
        
    if len(sku) < len(image_text):
        sku += ['None'] * (len(image_text) - len(sku))
    elif len(sku) > len(image_text):
        sku = sku[:len(s_price)]
        
        
    if len(brand) < len(image_text):
        brand += ['None'] * (len(s_price) - len(brand))
    elif len(brand) > len(image_text):
        brand = brand[:len(s_price)]
        
        
    if len(title_) < len(image_text):
        title_ += ['None'] * (len(image_text) - len(title_))
    elif len(title_) > len(image_text):
        title_ = title_[:len(s_price)]
        
    with open('link.txt',"a+") as file:
        file.writelines(link_list)
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    data = {
        "DateTime": [current_datetime] * len(s_price),  # Assign the same timestamp to all entries
        "SKU": sku,
        "Name": title_,
        "Brand": brand,
        "Average Rating": avg_rating,
        "Rating Count": rating_count,
        "Sponsered": sponsered,
        "Price": o_price,
        "Sales Price": s_price,
        "Express": image_text,
        "Rank": [i for i in range(1,len(o_price)+1)],
        "Link": link_list
            
    }

    data_frame = pd.DataFrame(data)

    file = "noon-yoga-products.csv"

    if not os.path.exists(file):
        # If file doesn't exist, write with header
        data_frame.to_csv(file, mode='a', index=False, header=True)
    else:
        # If file exists, append without header
        data_frame.to_csv(file, mode='a', index=False, header=False)
        
    next_page = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next page']")
    next_page.click()
    time.sleep(5)
"""Here, n represents the number of webpage pages,
with each page containing approximately 67 products."""
n=3 # for 3 pages
for run_fun in range(n):
    Scrape_one_page()
    
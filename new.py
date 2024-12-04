import pandas as pd
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium import webdriver
from collections import defaultdict
driver = webdriver.Chrome()

driver.get("https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/")
def Scrape_one_page():
    


  # Find all card containers in one go
    card_containers = driver.find_elements(By.CSS_SELECTOR, ".sc-57fe1f38-1.gYzxDm.grid")

    data = defaultdict(list)  # Use defaultdict for easier data collection

    for each_card in card_containers:
        # Use explicit waits for dynamic elements
        rating_avg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='sc-9cb63f72-2 dGLdNc']"))
        ).text
        data["Average Rating"].append(rating_avg)

        rating_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='sc-9cb63f72-5 DkxLK']"))
        ).text
        data["Rating Count"].append(rating_count)

        try:
            is_sponsered = each_card.find_element(By.CSS_SELECTOR, "div[class='sc-d96389d1-24 kXouJu']")
            data["Sponsored"].append(is_sponsered.text.strip() == "Sponsored" and "Y" or "N")
        except:
            ta["Sponsored"].append("None")

        try:
            old_price = each_card.find_element(By.CSS_SELECTOR, "span[class='oldPrice']")
            data["Price"].append(old_price.text)
        except:
            data["Price"].append("None")

        try:
            sale_price = each_card.find_element(By.CSS_SELECTOR, "strong[class='amount']")
            data["Sales Price"].append(sale_price.text)
        except:
            data["Sales Price"].append("None")

        try:
            image_tags = each_card.find_element(By.CSS_SELECTOR, "div[class='sc-51c372d5-3 HwYne'] img")
            alt_text = image_tags.get_attribute("alt")
            data["Express"].append(alt_text.strip() == 'noon-express' and "Y" or "N")
        except:
            data["Express"].append("none")

        # Extract other data using similar logic within the loop

        # Extract product name and brand (assuming structure is consistent)
        product_name_divs = each_card.find_elements(By.CSS_SELECTOR, "div[data-qa='product-name']")
        for div in product_name_divs:
            title_element = div.get_attribute("title").strip()
            data["Name"].append(title_element)
            data["Brand"].append(title_element.split()[0])

        # Extract link and SKU
        anchor_tag = each_card.find_element(By.CSS_SELECTOR, "div[class='sc-57fe1f38-0 eSrvHE'] a")
        link = anchor_tag.get_attribute("href")
        data["Link"].append(link)
        data["SKU"].append(link.split("/")[5])

    # Generate timestamps efficiently outside the loop
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["DateTime"] = [current_datetime] * len(data["Sales Price"])

    # Rank can be generated as a list comprehension outside the loop
    data["Rank"] = [i for i in range(1, len(data["Sales Price"]) + 1)]

    # Create pandas DataFrame and save to CSV
    data_frame = pd.DataFrame(data)
    file = "scraping.csv"

    if not os.path.exists(file):
        data_

Scrape_one_page()
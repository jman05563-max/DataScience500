
import requests
import pandas as pd
import re
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
books_data = []

session = requests.Session()

# Scrape all catalogue pages
for page in range(1, 51):
    if page == 1:
        url = BASE_URL
    else:
        url = urljoin(
            BASE_URL,
            f"catalogue/page-{page}.html"
        )

    print(f"Scraping page {page}...")

    response = session.get(url, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price_text = book.find(
            "p", class_="price_color"
        ).get_text(strip=True)

        price = float(
            re.search(r"\d+\.\d+", price_text).group()
        )

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).get_text(" ", strip=True)

        # Open the individual product page
        product_url = urljoin(url, book.h3.a["href"])

        product_response = session.get(
            product_url, timeout=20
        )
        product_response.raise_for_status()

        product_soup = BeautifulSoup(
            product_response.text, "html.parser"
        )

        # Extract genre from the breadcrumb
        breadcrumbs = product_soup.select(
            "ul.breadcrumb li a"
        )

        genre = (
            breadcrumbs[2].get_text(strip=True)
            if len(breadcrumbs) > 2
            else "Unknown"
        )

        # Extract stock quantity where available
        stock_element = product_soup.select_one(
            "p.instock.availability"
        )

        stock_text = (
            stock_element.get_text(" ", strip=True)
            if stock_element else availability
        )

        match = re.search(r"\((\d+) available\)", stock_text)
        stock_quantity = (
            int(match.group(1)) if match else None
        )

        books_data.append({
            "Title": title,
            "Price_GBP": price,
            "Rating": rating,
            "Availability": availability,
            "Stock_Quantity": stock_quantity,
            "Genre": genre,
            "Product_URL": product_url
        })

    # Small delay to avoid excessive requests
    time.sleep(0.3)

# Create a DataFrame
df = pd.DataFrame(books_data)

# Save the raw dataset
df.to_csv("books_raw.csv", index=False, encoding="utf-8")

print("\nScraping completed!")
print("Total books collected:", len(df))
print(df.head())
print("\nDataset saved as books_raw.csv")

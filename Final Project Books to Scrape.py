import requests
from bs4 import BeautifulSoup
import csv
import os
import re


def sanitize_filename(filename):
    # Remove or replace invalid characters for filenames
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', filename)

def download_images(image_url, title, category):
    if not os.path.exists(category):
        os.mkdir(category)
    
    # Handle the full URL case
    if not image_url.startswith('http'):
        image_url = 'https://books.toscrape.com/' + image_url

    try:
        # Download the image
        r = requests.get(image_url)
        r.raise_for_status()  # Raise an error for bad status codes
        
        # Sanitize title for the filename
        safe_title = sanitize_filename(title)
        image_path = os.path.join(category, f"{safe_title}.jpg")

        # Save the image
        with open(image_path, "wb") as f:
            f.write(r.content)
        print(f"Image saved to {image_path}")
    
    except requests.RequestException as e:
        print(f"Error downloading the image: {e}")
    except IOError as e:
        print(f"Error saving the image: {e}")

# Function to get data from a book page
def get_book_data(book_url):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extracting data
    product_page_url = book_url
    upc = soup.find('th', string='UPC').next_sibling.text
    title = soup.find('h1').text.strip()
    price_including_tax = soup.find('th', string='Price (incl. tax)').next_sibling.text.strip('Â')
    price_excluding_tax = soup.find('th', string='Price (excl. tax)').next_sibling.text.strip('Â')
    availability = soup.find('th', string='Availability').next_sibling.text.strip()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].text.strip()
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.find('div', class_='item active').img['src']
    
    download_images(image_url, title, category)

    # Prepare data as a dictionary
    book_data = {
        'product_page_url': product_page_url,
        'universal_product_code (upc)': upc,
        'book_title': title,
        'price_including_tax': price_including_tax,
        'price_excluding_tax': price_excluding_tax,
        'quantity_available': availability,
        'product_description': description,
        'category': category,
        'review_rating': review_rating,
        'image_url': image_url
    }
    
    return book_data

# Function to scrape books from a category page
def scrape_books_in_category(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all book links in the category
    books = soup.find_all('h3')
    base_url = 'https://books.toscrape.com/catalogue/'
    book_data_list = []

    for book in books:
        book_url = base_url + book.a['href'].replace('../', '')
        book_data = get_book_data(book_url)
        book_data_list.append(book_data)
    
    return book_data_list

# Function to save data to CSV
def save_to_csv(category, book_data_list):
    folder_path = './scraped_data'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    
    filename = f'{folder_path}/{category.replace(" ", "_")}_books.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code (upc)', 'book_title', 
                      'price_including_tax', 'price_excluding_tax', 'quantity_available', 
                      'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book_data in book_data_list:
            writer.writerow(book_data)
    
    print(f'CSV file saved for category: {category}')

# Main function to scrape all categories
def main():
    base_url = 'https://books.toscrape.com/'
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all categories
    categories = soup.find('ul', class_='nav-list').find_all('a')
    
    for category in categories:
        category_name = category.text.strip()
        category_url = base_url + category['href']
        print(f'Scraping books for category: {category_name}')
        book_data_list = scrape_books_in_category(category_url)
        save_to_csv(category_name, book_data_list)

if __name__ == '__main__':
    main()
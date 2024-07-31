This application aims to provide the user updated product information for all books listed on https://books.toscrape.com/. This code will extract product information accurately, saving down all detailed product information by category within various excel file located within a created folder named "scraped_data". This application will also save down each associated book image segregated into Folders named by category.
The scraping of the data will use Beautiful Soup, Beautiful Soup is a Python library for pulling data out of HTML and XML files. Requirements to run this code are as follows:

# Python Environment
### Python Version: Ensure you're running Python 3.6 or higher. This code uses f-strings and other Python 3 features that might not be available in earlier versions.
   
# Required Libraries
The following Python libraries would need to be installed:
##### 1.) requests: For making HTTP requests.  
##### 2.) beautifulsoup4: For parsing HTML and XML documents.  
##### 3.) csv: Standard library for handling CSV files (already included in Python’s standard library).
You can install the required libraries using pip:  
pip install requests beautifulsoup4
# Directory and File Handling
Directory Creation: The script creates directories to store images and CSV files. It expects to be able to create and write to directories and files in the working directory where the script is run.
# Internet Access
Web Scraping: The script fetches data from https://books.toscrape.com/. Ensure that you have internet access, and that the website is reachable from your network.
# Dependencies
Ensure that the script is run in an environment where it has permission to write files and make network requests. If running in a restricted environment, you might need to adjust permissions or configurations.
# Error Handling and Debugging
The script has basic error handling with try and except blocks for network requests and file operations. If the script encounters issues, it will print out error messages to help with debugging.
## Additional Considerations
Character Encoding: The script handles text encoding with utf-8, which should be compatible with most text data. Ensure your environment supports this encoding.
Web Structure Changes: The script is tailored for the specific structure of the books.toscrape.com website. If the structure of the site changes, you may need to update the code accordingly.
# Running the Code
## Save the code to a Python file, for example, scrape_books.py, and execute it using Python:
python scrape_books.py
# To run the code:
1.	Ensure you have Python 3.6+ installed.
2.	Install the required libraries using pip.
3.	Verify you have internet access and directory write permissions.
4.	Run the script from the command line or an IDE that supports Python.
If you follow these requirements and setup instructions, the code should execute and perform the web scraping and data saving tasks as intended.



import urllib.request
import re
import sys
import mysql.connector
from dotenv import load_dotenv
import os
from pathlib import Path

__author__="Hasan Ramazan Yurt"

#Sets the path of environment file and loads it
env_path = Path('.') / 'my.env'
load_dotenv(dotenv_path=env_path)

#Arrays of products' names, images' links, and prices
name_arr = []
img_arr = []
price_arr = []

#Checks the system argument if it given correct
if (len(sys.argv) < 2):
    print("You did not provide the requirement: a product detail page URL in hepsiburada.com ")
elif (len(sys.argv)>2):
    print("You did not provide the requirement: multiple product detail page URL parsed by comma in hepsiburada.com ")
else:
    urls = sys.argv[1]
    #Parses the given url and get proper multiple URLs
    if("," in urls):
        url_arr = urls.split(",")
    else:
        url_arr = [urls]

    for url in url_arr:
        # Check the url if it is from hepsiburada.com
        url_check = re.search('hepsiburada.com', url)
        if (url_check is None):
            print("The url provided is not from hepsiburada.com")
        else:
            response = urllib.request.urlopen(url);
            html_code = response.read().decode('utf-8')
        #Searches spesific pattern to reach name, image link and price of a product
        name_arr.append(re.search(r'\'productName\'\">(.*)</span>', html_code).group(1))
        price_arr.append(re.search(r'id=\"offering-price\".*content=(.*)>', html_code).group(1))
        img_arr.append(re.search(r'data-img=\"(.*)\"',html_code).group(1).replace("#imgSize","552"))

    #number of the products
    number = len(name_arr)

#Connecting MySql and creating database
mydb = mysql.connector.connect(
  host=os.environ.get("HOST"),
  user=os.environ.get("USER"),
  passwd=os.environ.get("PASSWORD")
)

mycursor = mydb.cursor()
db_name=os.environ.get("DATA_BASE_NAME")
sql_db=("CREATE DATABASE IF NOT EXISTS "+db_name)
mycursor.execute(sql_db)
#After creating database second connection by pointing created database
mydb2 = mysql.connector.connect(
  host=os.environ.get("HOST"),
  user=os.environ.get("USER"),
  passwd=os.environ.get("PASSWORD"),
  database=db_name
)
mycursor = mydb2.cursor()
sql_drop = "DROP TABLE IF EXISTS Product"
mycursor.execute(sql_drop)
#Addin the inputs to the Product Table
mycursor.execute("CREATE TABLE Product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), image VARCHAR(255), price VARCHAR(255))")
sql = "INSERT INTO Product (name, image, price) VALUES (%s, %s, %s)"
for i in range(number):
    val = [(name_arr[i],img_arr[i],price_arr[i])]
    mycursor.executemany(sql, val)
mydb2.commit()
print(mycursor.lastrowid,"input was inserted.")




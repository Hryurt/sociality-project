# Sociality-Project

A program that gets names, images' links, and prices of given products in given URLs. Then, writes these data to SQL table named 'Product'. This program only works with URLs of hepsiburada.com like [this](https://www.hepsiburada.com/apple-macbook-pro-touch-bar-intel-core-i5-8259u-8gb-256gb-ssd-macos-13-qhd-tasinabilir-bilgisayar-mr9q2tu-a-gri-p-HBV00000CVXAY) 

## Before Running

Before installing this program, follow the instructions below. (If you have already installed these requirement, disregard this part.)
* Install Python from [here](https://www.python.org/downloads/)
* Install MySQL and MySQL Workbench (for instruction look at [here](https://dev.mysql.com/downloads/) and [here](https://www.mysql.com/products/workbench/))
* Install PIP (for detailed information [click](https://phoenixnap.com/kb/install-pip-windows))
* Install MySQL Connector, use code below
```
pip install mysql-connector-python
```
## How To Run

* There are two files in the program: product.py and my.env. product.py is the main code that do the given purpose. my.env is the environment values file. There are four environment values in the file. HOST variable is the name of the host you want to use. USER variable is the name of the MySql user you want to connect. PASSWORD variable is the password of the MySql Connection. DATA_BASE_NAME variable is the database that you want to create. You can change these 4 value by editing the file. **Please do the necessary regulations then run the program.**
* Optionally you can write only one URL or multiple URLs to run the code. If you to use multiple URLs please parse these URLs with comma. 
* You can run the code by using the command below
```
python product.py {{ValidURL1},{ValidURL2},...,{ValidURLN}}
```

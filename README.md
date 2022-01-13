# os-python-scripts
Python code that uses selenium web driver to scrape sales data from OpenSea collections page


## How to use it 

First you'll need to install the requirements for you local machine and that means Python3 must be installed.

0.) Install the dependencies

```
> pip install -r requirements.txt 
```

1.) Get the MoonCat data

`> python3 get_mooncat_data.py`

will use the **Selenium** headless Browser to open tabs for OpenSea and then save the pages, which will later be scraped for data.

2.) Calculate the floors 

`> python3 calculate_floors.py`

Will take the data pages scraped from **1.)** and then parse it for relevant data and perform the calculations. The output will be file **curr_floors.txt**

3.) Optional - Use Tweepy to send twitter update

This step requires uncommenting some code on the first run to generate access key & secret. Additionally, it requires creation of a web app in the Twitter Developer portal. 
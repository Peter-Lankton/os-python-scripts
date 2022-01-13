from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os, shutil, pathlib, fnmatch
import datetime


urls = [
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Coat&search[stringTraits][0][values][0]=Orange%20Tabby",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Coat&search[stringTraits][0][values][0]=Pale%20Sky%20Blue%20Pure&search[stringTraits][0][values][1]=Pale%20Blue%20Pure",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Coat&search[stringTraits][0][values][0]=Pale%20Purple%20Tabby&search[stringTraits][0][values][1]=Pale%20Magenta%20Tabby&search[stringTraits][0][values][2]=Pale%20Fuchsia%20Tabby",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Coat&search[stringTraits][0][values][0]=Pale%20Fuchsia%20Pure&search[stringTraits][0][values][1]=Pale%20Red%20Pure",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Coat&search[stringTraits][0][values][0]=Pale%20Green%20Pure&search[stringTraits][0][values][1]=Pale%20Teal%20Pure&search[stringTraits][0][values][2]=Pale%20Cyan%20Pure",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Has%20Clones%3F&search[stringTraits][0][values][0]=Yes",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Rescue%20Year&search[stringTraits][0][values][0]=2017",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Rescue%20Year&search[stringTraits][0][values][0]=2018",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Rescue%20Year&search[stringTraits][0][values][0]=2019",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Rescue%20Year&search[stringTraits][0][values][0]=2020",
	"https://opensea.io/collection/acclimatedmooncats?search[sortAscending]=false&search[sortBy]=LAST_SALE_DATE&search[stringTraits][0][name]=Rescue%20Year&search[stringTraits][0][values][0]=2021"

]

# To make job easier 
# can save each one to a different file at least 
names = [
	"GARFIELD.txt",
	"ALIEN.txt",
	"CHESHIRE.txt",
	"PINKPANTHER.txt",
	"ZOMBIE.txt",
	"CLONES.txt",
	"2017.txt",
	"2018.txt",
	"2019.txt",
	"2020.txt",
	"2021.txt"
]

if __name__ == "__main__":
	driver = webdriver.Chrome('../chromedriver')
	driver.maximize_window()
	driver.delete_all_cookies()
	for posts in range(len(urls)):
		driver.get(urls[posts])    
		driver.execute_script("window.open('');")
		chwd = driver.window_handles
		driver.switch_to.window(chwd[-1])
	# Wait for the data to fully load
	driver.implicitly_wait(200)
	for num,tab in enumerate(chwd):
		driver.switch_to.window(tab)
		with open("data/"+names[num], 'w') as f:
			f.write(driver.page_source)
		
	

	

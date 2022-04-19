from tokenize import PlainToken
from flask import request
from selenium import webDriver
from bs4 import BeautifulSoup
import time
import csv
START_URL="https://exoplanets.nasa.gov/exoplanet-catalog/"
browser=webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",ettrs={"class","expoplanet"}):
        li_tags=ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index==0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
def scrape_more_data(hyperlink):
    age=requests.get(hyperlink)
    soup=BeautifulSoup(page.content,"html.parser")
    for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
        td_tags=tr_tags.find_all("td")
        temp_list=[]
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs={"class":"value"}[0]:0.contents[0]))
                except:
                    temp_list.append("")
                    new_planet_data.append(temp_list)
scrape()
for data in planet_data:
    scrape_more_data(data[5])
    final_planet_data=[]
    for index,data in enumerate(planet_data):
        final_planet_data.append(data+final_planet_data[index])
        with open("final.csv","w") as f:
            csvwriter=csv.writer(f)
            csvwriter=writerow(headers)
            csvwriter.writerows(final_planet_data)
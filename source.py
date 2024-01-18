import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

city_name=input("Ievadiet pilsētas nosaukumu: ")

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.google.com/"
driver.get(url)
time.sleep(2)

find=driver.find_element(By.ID, "L2AGLb")
find.click()

search=driver.find_element(By.NAME, "q")
search.send_keys('weather ' + city_name)
search.submit()
time.sleep(2)

from tabulate import tabulate
top =["Darba Diena","Temperatūra °C","Laikapstākļi","Nokrišņi","Mitrums","Vējš"]
data=[]

for i in range(1,8):
    find=driver.find_element(By.ID, f"dimg_{2*i-1}")
    find.click()
    time.sleep(0.5)
    
    find=driver.find_element(By.ID, "wob_dts") ##datums
    date=find.text
    find=driver.find_element(By.ID, "wob_tm") ##temperatūra
    temp=find.text
    find=driver.find_element(By.ID, "wob_dc") ##apstākļi
    weather=find.text
    find=driver.find_element(By.ID, "wob_pp") ##nokrišņi
    rain=find.text
    find=driver.find_element(By.ID, "wob_hm") ##mitrums
    humidity=find.text
    find=driver.find_element(By.ID, "wob_ws") ##vējš
    wind=find.text

    temp=f"{temp}°C"

    data.append([date,temp,weather,rain,humidity,wind])

print(tabulate(data,top,tablefmt="fancy_grid"))

time.sleep(3)
driver.quit()
from selenium import webdriver
import time
import pandas as pd
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
import re

p = re.compile("[^0-9]")
#options = Options()
#options.add_argument('--start-fullscreen')




driver = webdriver.Chrome("C:/python_ML/chromedriver.exe")
Toss = driver.get("https://toss.im/every-moment")
#time.sleep(1)
driver.maximize_window()
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

aa = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[1]/ul[2]").text
bb = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/ul[2]").text
cc = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[3]/ul[2]").text
dd = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[4]/ul[2]").text


aa = "".join(p.findall(aa))
bb = "".join(p.findall(bb))
cc = "".join(p.findall(cc))
dd = "".join(p.findall(dd))

list_aa = aa.replace("\n","").split("번째 불편함")
list_bb = bb.replace("\n","").split("번째 불편함")
list_cc = cc.replace("\n","").split("번째 불편함")
list_dd = dd.replace("\n","").split("번째 불편함")
list_all = list_aa + list_bb + list_cc + list_dd
print(list_all)
print(len(list_all))
#for number in : 
#    complain = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[1]/ul[2]/li["+str(number)+"]/div/p")
# =============================================================================
# /html/body/div[1]/main/div[2]/div/div[1]/ul[2]/li[2]/div/p
# /html/body/div[1]/main/div[2]/div/div[2]/ul[2]/li[1]/div/p
# /html/body/div[1]/main/div[2]/div/div[2]/ul[2]/li[2]/div/p
# =============================================================================
df = {'의견':list_all}
stock_conversation = pd.DataFrame(df)
stock_conversation.to_csv('C:/python_ML/tossopinion_3.csv', encoding ='UTF-16')


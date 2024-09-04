from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import random

def is_valid_result(video_name, driver):
    try:
        wait = WebDriverWait(driver, 10)
        first_result = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="video-title"]')))
        
        first_video_title = first_result.get_attribute("title") 
        
        if video_name.lower() in first_video_title.lower():
            return True
        else:
            return False
    except:
        return False

video_names = ['The weeknd - starboy', 
               'Taylor swift - exile', 
              'Khalid - 8TEEN', 
              'aasdfasdfasf', 
              'dayglow - can i call you tonight', 
              'The police - every breath you take', 
              'Radiohead - creep',
              'sabrina carpenter - espresso', 
              'never gonna give you up',
              'Kendrick Lamar - Not like us']

video_name = random.choice(video_names)

print(video_name)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com")

WebDriverWait(driver , 5).until(
    EC.presence_of_element_located((By.NAME, "search_query"))
)

search_box = driver.find_element(By.NAME, "search_query")
search_box.clear()
search_box.send_keys(video_name)
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 5)


if is_valid_result(video_name, driver):
    print("Valid video found.")
else:
    print("Invalid video name. No relevant results found.")
    driver.quit()

time.sleep(2)

video = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-video-renderer ytd-thumbnail a#thumbnail')))
video.click()

share_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-watch-flexy ytd-menu-renderer yt-button-view-model')))
print("Share button found")
share_button.click()
print("share button clicked")

time.sleep(2)

copy_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ytd-unified-share-panel-renderer #copy-link yt-button-shape')))
print("Copy button detected")
copy_link.click()
print("copy button clicked")
copy_link = pyperclip.paste()
print("copied link = " + copy_link)

driver.get("https://downloaderto.com/engf/")

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//input[@placeholder = 'Paste Your URL...']"))
)

text_box = driver.find_element(By.XPATH, "//input[@placeholder = 'Paste Your URL...']")
print("text box found")
time.sleep(2)
text_box.send_keys(copy_link)

load = driver.find_element(By.XPATH, "//button[@id='load']")
load.click()
print("load button clicked")

time.sleep(2)

download_button = driver.find_element(By.XPATH, "//a[@class='btn-download']")
print("download button detected")
time.sleep(5)
download_button.click()
print("download started")
    
time.sleep(20)

driver.quit()
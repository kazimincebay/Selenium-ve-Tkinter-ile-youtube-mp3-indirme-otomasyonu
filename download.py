from selenium import webdriver
import requests
import time

def urll(url):
    


    driver=webdriver.Chrome("C:\chromedriver.exe") 

    link="https://mp3y.download/tr/nice-mp3-convert"
    driver.get(link) 
    time.sleep(2) 
    urlyaz=driver.find_element_by_name("url").send_keys(url) 
    time.sleep(1) 
    butontikla=driver.find_element_by_class_name("input-group-append").click()
    time.sleep(18)
    downloadstart=driver.find_element_by_xpath('//*[@id="app"]/div/article/div/p[2]/button').click()
    time.sleep(5)
    window_name = driver.window_handles[1]
    driver.switch_to_window(window_name=window_name)
    driver.close()
    time.sleep(4)
    windoww_name = driver.window_handles[0]
    driver.switch_to_window(window_name=windoww_name)
    downloadresume=driver.find_element_by_xpath('//*[@id="app"]/div/article/div/p[2]/a').click()
    time.sleep(20)
    driver.quit()
    


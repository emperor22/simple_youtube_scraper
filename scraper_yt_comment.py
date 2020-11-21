from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import pandas as pd
import os
from joblib import Parallel, delayed
#import dill as pickle

SCROLL_NUMBERS = 100
#KEYWORD = 'satu dua'

#keyw = lambda x: x.replace(' ', '+')
#query = keyw(KEYWORD)

#url = f'https://www.youtube.com/results?search_query={query}'

urls = [
    'https://www.youtube.com/watch?v=YmbwPLuASQw',
    'https://www.youtube.com/watch?v=m-_EYWMK-Uk',
    'https://www.youtube.com/watch?v=LNJnkV9iAh0', 
    'https://www.youtube.com/watch?v=DBhsovSJbpg']


def scrape_yt_comments(url, timeit=False):
    filename = f'yt_comments_{urls.index(url)}.csv'

    driver_path = 'chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(driver_path, options=chrome_options)
    actions = ActionChains(driver) 

    start1 = time.time()
    comments = []
    driver.get(url)
    time.sleep(5)

    for i in range(SCROLL_NUMBERS):
        if i < 1:
            driver.find_element_by_id('container').click()
            for _ in range(4):
                #actions = actions.send_keys(Keys.DOWN)
                driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
            actions.perform()
        time.sleep(1)
        WebDriverWait(driver, 10).until(presence_of_element_located((By.TAG_NAME, "body")))
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        WebDriverWait(driver, 10).until(presence_of_element_located((By.ID, "content-text")))
        comment_length = len(comments)
        print('appending comments..')
        for i in driver.find_elements_by_id('content-text')[comment_length:]:
                comments.append(i.text)


    df = pd.DataFrame(comments, columns=['comments'])
    df.to_csv(filename)   
    print('File: ',filename, ' ---- Total comments: ', len(set(comments)))
    if timeit:
        print(time.time() - start1)

Parallel(n_jobs=-1)(delayed(scrape_yt_comments)(url) for url in urls)

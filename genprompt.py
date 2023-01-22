from multiprocessing.context import SpawnProcess
from bs4 import Tag
import requests,base64
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import (
    ElementNotVisibleException,
    ElementClickInterceptedException,
    WebDriverException,
    TimeoutException,
)
import threading
import numpy as np
from requests.structures import CaseInsensitiveDict
import webbrowser
import subprocess, threading, selenium, requests, logging, base64, json, time, os, webbrowser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
fen_chars=list('_KQRBNPkqrbnp')
def gen():
    fen_arr = np.random.choice(fen_chars, 64)
    fen_param = "".join(fen_arr)
    fen_arr = np.hstack(np.split(fen_arr, 8)[::-1])
    fen_arr[fen_arr == fen_chars[0]] = "1"
    img_filename_prefix = "/".join(map("".join, np.split(fen_arr, 8)))
    return img_filename_prefix


fen_ = gen()
print(fen_)
options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
options.add_argument("--headless")
driver = webdriver.Chrome("./chess_com_board_generator/chromedriver",options=options)
link_to_game = 'https://www.chess.com/tinymce/chessdiagram'
driver.get(link_to_game)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div/div/div[3]/div/button'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sidebar"]/div/div/div[3]/section/div/input'))).send_keys(fen_)
driver.find_element(By.XPATH,'//*[@id="sidebar"]/div/div/div[3]/section/div/button').click()
time.sleep(1)
img64 = driver.find_element(By.TAG_NAME,'chess-board').screenshot_as_base64
#decode img64
imgdata = base64.b64decode(img64)
fen_file = fen_.replace('/','-')
print(f'{fen_file}.png')
with open(f'.//{fen_file}.png', 'wb') as f:
    f.write(imgdata)
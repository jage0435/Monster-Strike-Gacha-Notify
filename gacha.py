from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import schedule
import time

def send_line_notify(message, token):
    """
    Args:
        message (str): message to send
        token (str): Line Notify Token
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': message}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code


def job():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')

        # 設定 ChromeDriver 的路徑
        driver_path = "/usr/local/bin/chromedriver"

        # 建立 ChromeDriver 的服務
        service = Service(executable_path=driver_path)

        # 啟動 ChromeDriver
        driver = webdriver.Chrome(service=service,options=chrome_options)
        # 載入網頁
        driver.get('http://monst-multi.net/Gacha')

        # 等待網頁中的 JavaScript 加載完成
        wait = WebDriverWait(driver, 5)

        # 找到 iframe 元素
        iframe = driver.find_element(By.XPATH, '//iframe[@id="igacha"]')
        # 切換到 iframe
        driver.switch_to.frame(iframe)
        # 抓取 iframe 中的元素
        images = driver.find_elements(By.TAG_NAME, 'img')
        trs = driver.find_elements(By.TAG_NAME, 'tr')

        # 取得所有 img 標籤的 src 屬性值
        for img in images:
            if(img.get_attribute('src') == 'http://monstgacha-yosou.xyz/linemulti/images/content06-01.png'):
                result = '\n超絕大\n'
                prob = '\n'.join([tr.text for tr in trs])
                send_line_notify(result+prob, line_token)
            # elif(img.get_attribute('src') == 'http://monstgacha-yosou.xyz/linemulti/images/content05-01.png'):
            #     result = '\n超絕\n'
            #     prob = '\n'.join([tr.text for tr in trs])
            #     send_line_notify(result+prob, line_token)

        # 關閉瀏覽器
        driver.quit()
    except Exception as e:
        print(e)

line_token = ""
# 每分鐘執行一次 job() 函式
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

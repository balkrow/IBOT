import pickle

from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
import pyautogui
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
user_ag = UserAgent().random
options.add_argument('user-agent=%s'%user_ag)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
driver = webdriver.Chrome(options=options)

# 크롤링 방지 설정을 undefined로 변경
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})
driver.maximize_window()
cookies = pickle.load(open("cupang_cookies.pki", "rb"))

#for cookie in cookies:
 #driver.add_cookie(cookie)

driver.get("https://login.coupang.com/login/login.pang?rtnUrl=https://www.coupang.com/vp/products/7630888734?isAddedCart=&vendorItemId=87340557098")
driver.implicitly_wait(2)
#driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")

# 아이디 입력창
id = driver.find_element(By.NAME, "email")
id.click()
# id.send_keys("아이디")
pyperclip.copy("balkrow@gmail.com")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
# 비밀번호 입력창
pw = driver.find_element(By.NAME, "password")
pw.click()
# pw.send_keys("비밀번호")
pyperclip.copy("v449xnf")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# log.login
login_btn = driver.find_element(By.XPATH, "//button[@class='login__button login__button--submit _loginSubmitButton login__button--submit-rds']")  # \. : 이스케이프 문자
login_btn.click()
#87340557714 블루 티타늄
#87340557098 내츄럴 티나늄
#url = 'https://www.coupang.com/vp/products/7630888734?isAddedCart=&vendorItemId=87340557714'
#driver.get(url)
time.sleep(10)

while True:

    buy = driver.find_element(By.XPATH, "//button[@class='prod-pre-order-btn']")
    # buy = driver.find_element(By.LINK_TEXT, "바로 예약구매")
    print(buy.text)

    if buy.text == '바로 예약구매':
        buy.click()

        driver.find_element(By.CSS_SELECTOR, '#rocketCard-quota-select').click()
        time.sleep(0.5)
        select = Select(driver.find_element(By.ID, 'rocketCard-quota-select'))
        select.select_by_visible_text('22개월 (무이자)')

        buy2 = driver.find_element(By.XPATH, "//*[@id = 'paymentBtn']")
        buy2.click()
        #driver.implicitly_wait(10)
        time.sleep(1.5)

        driver.switch_to.frame("callLGPayment")
        driver.save_screenshot("pay.png")
        pyautogui.locateOnScreen("pay.png")

        img_capture = pyautogui.locateOnScreen("6.png")  # 70%
        pyautogui.click(img_capture)
        img_capture = pyautogui.locateOnScreen("5.png")  # 70%
        pyautogui.click(img_capture)
        img_capture = pyautogui.locateOnScreen("2.png")  # 70%
        pyautogui.click(img_capture)
        img_capture = pyautogui.locateOnScreen("4.png")  # 70%
        pyautogui.click(img_capture)
        img_capture = pyautogui.locateOnScreen("0.png")  # 70%
        pyautogui.click(img_capture)
        img_capture = pyautogui.locateOnScreen("6.png")  # 70%
        pyautogui.click(img_capture)


        """
        keypad = driver.find_elements(By.CLASS_NAME, "div.rocketpay-keypad-password-wrap")
        #keypad = driver.find_elements(By.CSS_SELECTOR, "a")
        for index, value in enumerate(keypad):
            print(value.text)
            body = value.find_elements("span")[0].a
            print(body.text)

        
        keypad = driver.find_element(By.XPATH, "//*[@id='rocketpay-service']/form/div[3]/div[5]/table")
        tobdy = keypad.find_element(By.TAG_NAME,"tbody")
        rows = tobdy.find_elements(By.TAG_NAME, "tr")
        for index, value in enumerate(rows):
            print(value)
            body = value.find_elements("td")[1]
            print(body.text)
        
        """
        time.sleep(60)
        #pickle.dump(driver.get_cookies(), open("cupang_cookies.pki", "wb"))
        break
    else:
        driver.refresh()
        driver.implicitly_wait(10)
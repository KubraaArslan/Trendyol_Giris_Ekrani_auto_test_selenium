
#from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options



class Test_Trendyol:
    def test_login_screen(self):
        #--> Giriş yap ekranına geçilebilmesi.
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        loginPageMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/h3") 
        testResult = loginPageMessage.text == "Trendyol’a giriş yap veya hesap oluştur, indirimleri kaçırma!"
        print(f"TEST SONUCU: {testResult}")
        sleep(2)

    def test_invalid_login(self):
        #--> Eposta ve şifrenin aynı anda yanlış girilmesi 
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input") 
        usernameInput.send_keys("1")
        loginInput.send_keys("1")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[1]/span[2]") 
        testResult = errorMessage.text == "Lütfen geçerli bir e-posta adresi giriniz."
        print(f"TEST SONUCU: {testResult}")
        sleep(5)

    def test_invalid_login2(self):
        #--> Eposta alanına geçerli olandan fazla karakter girilmesi (sonuna boşluk)
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input")
        usernameInput.send_keys("doğru mail adresi(boşluk) ")
        loginInput.send_keys("doğru şifre")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[1]/span[2]") 
        testResult = errorMessage.text == "Lütfen geçerli bir e-posta adresi giriniz."
        print(f"TEST SONUCU: {testResult}")
        sleep(5)

    def test_invalid_login3(self):
        #--> Epostanın doğru, şifrenin yanlış girilmesi
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input")
        usernameInput.send_keys("doğru mail adresi")
        loginInput.send_keys("2")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        sleep(2)
        errorMessage2 = driver.find_element(By.ID, "error-box-wrapper") 
        testResult = errorMessage2.text == "E-posta adresiniz ve/veya şifreniz hatalı."
        print(f"TEST SONUCU: {testResult}")
        #print("E-posta adresiniz ve/veya şifreniz hatalı.")
        sleep(5)    
    def test_invalid_login4(self):
        #--> Alanlara değer girilmeden giriş yap butonuna basılması.
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input")
        usernameInput.send_keys("")
        loginInput.send_keys("")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[1]/span[2]") 
        testResult = errorMessage.text == "Lütfen geçerli bir e-posta adresi giriniz."
        print(f"TEST SONUCU: {testResult}")
        sleep(5)
    def test_invalid_login5(self):
        #--> Eposta alanına eposta formatında bir değer girilmemesi
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input")
        usernameInput.send_keys("fkgjsjgks")
        loginInput.send_keys("")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[3]/div[1]/span[2]") 
        testResult = errorMessage.text == "Lütfen geçerli bir e-posta adresi giriniz."
        print(f"TEST SONUCU: {testResult}")
        sleep(5) 

    def test_valid_login(self):
        #--> Eposta ve şifrenin aynı aynı anda doğru girilmesi
        option = Options()
        option.add_argument('--disable-notifications')
        driver = webdriver.Chrome(option)
        driver.maximize_window()
        driver.get("https://www.trendyol.com/")
        acceptCookie = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]")
        loginBtn.click()
        usernameInput = driver.find_element(By.ID, "login-email")
        loginInput = driver.find_element(By.ID, "login-password-input")
        usernameInput.send_keys("doğru-mail adresi")
        loginInput.send_keys("doğru şifre")
        loginBtn2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[3]/div[1]/form/button/span")
        loginBtn2.click()
        sleep(2)
        checkLoginUserText = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/p")
        testResult = checkLoginUserText.text == "Hesabım"
        print(f"TEST SONUCU: {testResult}")

        sleep(5) 
    
    

testClass = Test_Trendyol()
testClass.test_valid_login()
testClass.test_invalid_login3()
testClass.test_login_screen()
testClass.test_invalid_login()
testClass.test_invalid_login2()
testClass.test_invalid_login4()
testClass.test_invalid_login5()






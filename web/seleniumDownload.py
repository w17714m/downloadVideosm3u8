from selenium import webdriver
import os

from selenium.common.exceptions import WebDriverException

PATH_DRIVER_CHROME = os.getcwd() + "\\lib\\chromedriver.exe"


class SeleniumDownload:
    seleniumInstance = None

    def __init__(self):
        try:
            self.seleniumInstance = webdriver.Chrome(executable_path=PATH_DRIVER_CHROME,
                                                     chrome_options=self.buildChromeOptions())
        except WebDriverException as wde:
            print("No se encontro el web driver " + PATH_DRIVER_CHROME)

    def testweb(self):
        self.seleniumInstance.implicitly_wait(300)
        self.seleniumInstance.get('https://www.google.com/')

    def buildChromeOptions(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_untrusted_certs = True
        chrome_options.assume_untrusted_cert_issuer = True
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-impl-side-painting")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-seccomp-filter-sandbox")
        chrome_options.add_argument("--disable-breakpad")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-cast")
        chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
        chrome_options.add_argument("--disable-cloud-import")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-session-crashed-bubble")
        chrome_options.add_argument("--disable-ipv6")
        chrome_options.add_argument("--allow-http-screen-capture")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--disable-infobars")
        return chrome_options

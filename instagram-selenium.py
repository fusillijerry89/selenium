# http://stackoverflow.com/questions/38304253/how-to-set-proxy-authentication-user-password-using-python-selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from base64 import b64encode
import time

emailOrPhoneNumber = "+639464360553"
fullName = "Michelle Krazni"
#username = ""
password = "luke82817"
proxyHost = "89.40.113.199"
proxyPort = "3051"

browserWidth = "800"
browserHeight = "950"


##+ PROXY +##
#proxy = {'host': "51.15.251.43", 'port': "62007", 'usr': 'comet2_5bxvo','pwd': 'euCtN1BP'}
fp = webdriver.FirefoxProfile()

# Check out http://stackoverflow.com/questions/17988821/running-selenium-behind-a-proxy-server
# for possibly cleaner code

#fp.add_extension(extension="extensions/close_proxy_authentication.xpi")
#fp.set_preference('network.proxy.type', 1)
#fp.set_preference('network.proxy.http', proxy['host'])
#fp.set_preference('network.proxy.http_port', int(proxy['port']))
#fp.set_preference('network.proxy.ssl', proxy['host'])
#fp.set_preference('network.proxy.ssl_port', int(proxy['port']))
#fp.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
#credentials = '{usr}:{pwd}'.format(**proxy)
#credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
#fp.set_preference('extensions.closeproxyauth.authtoken', credentials)
##- PROXY -##

# disable flash
#fp.set_preference('plugin.state.flash', 0);

#fp.add_extension(extension="extensions/canvas_defender.xpi")
#fp.add_extension(extension="extensions/random_agent_spoofer.xpi")

driver = webdriver.Firefox(fp)
#driver2 = webdriver.Firefox(fp)

#driver.set_window_size(browserWidth, browserHeight)
#driver.set_window_position(0,0)

driver.get("https://www.instagram.com")
#assert "Instagram" in driver.title

#try:
#    element_present = EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Log in')]"))
#    WebDriverWait(driver, 3).until(element_present)
#    print("Page is ready!")
#except TimeoutException:
#    print("Loading took too much time!")


#elem = driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")


#numberOrEmail_i = driver.find_element_by_xpath("//input[@placeholder='Mobile Number or Email']")
#numberOrEmail_i.send_keys(emailOrPhoneNumber)
#fullName_i = driver.find_element_by_xpath("//input[@placeholder='Full Name']")
#fullName_i.send_keys(fullName)


## let IG generate usernames for now
#username_i = driver.find_element_by_xpath("//input[@placeholder='Username']")
#username_i.send_keys(username)
#password_i = driver.find_element_by_xpath("//input[@placeholder='Password']")
#password_i.send_keys(password)

#signup_button = driver.find_element_by_xpath("//button[contains(text(), 'Sign up')]")
#signup_button.click()

#assert "No results found." not in driver.page_source

#user_agent = driver.execute_script("return navigator.userAgent")
#print("user agent : " + user_agent)

#driver.close()

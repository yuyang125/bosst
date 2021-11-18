from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "/自动化/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.baidu.com")

shuruhuang = driver.find_element_by_id("kw")
shuruhuang.send_keys("QQ邮箱")
baiduyixia = driver.find_element_by_id("su")
baiduyixia.click()
sleep(1)
diyiyuansu = driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
diyiyuansu.click()

print(driver.window_handles)
print(driver.current_window_handle)

driver.switch_to.window(driver.window_handles[1])
# sleep(1)
# driver.find_element_by_link_text("基本版").click()


sleep(1)
driver.switch_to.frame("login_frame")
diyigehuan = driver.find_element_by_css_selector("#u")
diyigehuan.send_keys("123456")
diyigehuan.send_keys(Keys.TAB, "123456")

driver.get_screenshot_as_file("1.png")

sleep(5)
driver.quit()

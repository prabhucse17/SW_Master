from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import datetime
import Scaling_lib

lib = Scaling_lib.Test

url_link = "http://192.168.91.173"
driver = webdriver.Chrome(r"D:/chromedriver.exe")
driver.get(url_link)

Enter_username = lib.find(driver, "id", "input_0", "send", "admin")
if (Enter_username):
    print("username entered")

Enter_pass = find(driver, "id", "input_1", "send", "default")
if (Enter_pass):
    print("Enter_pass Done")

Submit = find(driver, "xpath", '//*[@id="vibe-sso"]/ui-view/vibe-sso-login/div/div/form/md-content/div/button', "click",
              "")
if (Submit):
    print("Submit Done")

print("==============")
# time.sleep(15)
end_point_button = find(driver, "xpath", '/html/body/md-toolbar/div/div[3]/button[3]', "click", "")
if (end_point_button):
    print("end_point_button clicked Done")
print("==============")
# time.sleep(15)

search_vpma = find(driver, "id", 'input_2', "send", "genericx86-64-15833054357")
if search_vpma:
    print("search_vpma Done")

# select_vpma = find(driver,"xpath",'/html/body/div[3]/md-content/div/vi-testpoint-select/div[2]/div/div[1]/div/div/div[5]/button[1]',"click","")
# if select_vpma:
#     print("select_vpma Done")

new_test_page = find(driver, "xpath", '/html/body/md-toolbar/div/div[3]/button[1]', "click", "")
if new_test_page:
    print("new_test_page click Done")

new_test_button = find(driver, "xpath", '/html/body/div[3]/div/div/div[1]/button', "click", "")
if new_test_button:
    print("new_test_button click Done")

select_twamp = find(driver, "id", 'radio_28', "click", "")
if select_twamp:
    print("select_twamp test radio button")

select_button = find(driver, "xpath",
                     '/html/body/div[3]/md-content/div[1]/vi-test-select/div/md-content/md-card/md-card-actions/button[1]',
                     "click", "")
if select_button:
    print("select_button clicked")

search_twamp_intiator = find(driver, "id", 'input_39', "send", "genericx86-64-1583305359047")
if search_twamp_intiator:
    print("select_twamp_intiator search")

select_twamp_intiator = find(driver, "xpath",
                             '/html/body/div[3]/md-content/div[1]/div[5]/md-card/vi-testpoint-select/div[2]/div/div[1]/div/div/div[5]/button',
                             "click", "")
if select_twamp_intiator:
    print("select_twamp_intiator clicked")

switch_to_new_frame = switchtoframe(driver, 'uicframe')
if switch_to_new_frame:
    print("Switched to new Frame")

pm_interval = find(driver, "id", 'pmInterval', 'send', "1 minute")
if pm_interval:
    print("PM Interval Changed")

input_intiator_IP = find(driver, "id", 'srcIPAddress', "clearandsend", "10.10.10.10")
if input_intiator_IP:
    print("input_intiator_IP set")

input_intiator_Mask = find(driver, "id", 'srcNetmask', "clearandsend", "255.255.255.128")
if input_intiator_Mask:
    print("input_intiator_Mask set")

input_Gateway = find(driver, "id", 'gatewayIPAddress', "clearandsend", "10.10.10.1")
if input_Gateway:
    print("input_Gateway set")

input_base_udp_port = find(driver, "id", 'srcStartingPort', "clearandsend", "60000")
if input_base_udp_port:
    print("input_base_udp_port set")

click_sessions_tab = find(driver, "xpath", '/html/body/div[1]/div[1]/ul/li[2]/a', "click", "")
if click_sessions_tab:
    print("Clicked Sessions Tab")

set_Session_name = find(driver, "xpath", '/html/body/div[1]/div[5]/div[4]/div/div[2]/input', "clearandsend", "sess_1")
if set_Session_name:
    print("set_Session_name Tab")

click_refelector = find(driver, "xpath", '/html/body/div[1]/div[5]/div[4]/div/div[3]/div[4]', "click", "")
if click_refelector:
    print("click_refelector Done")

enter_reflector_ip = find(driver, "xpath", '/html/body/div[1]/div[5]/div[8]/div[2]/div/div/div/div[2]/div[1]/input',
                          "clearandsend", "192.168.10.1")
if enter_reflector_ip:
    print("enter_reflector_ip Done")

twamp_mode_light = find(driver, "xpath",
                        '/html/body/div[1]/div[5]/div[8]/div[2]/div/div/div/div[1]/div/div[1]/label/span', "click", "")
if twamp_mode_light:
    print("click_refelector Done")

click_done = find(driver, "xpath", '/html/body/div[1]/div[5]/div[8]/div[3]/button[1]', "click", "")
if click_done:
    print("click_done Done")

flow_edit = find(driver, "xpath", '/html/body/div[1]/div[5]/div[4]/div/div[5]/div[1]/table/tbody/tr[1]/td[2]', "click",
                 "")
if flow_edit:
    print("flow_edit Done")

print("---------------")
enter_flow_details = find(driver, "xpath", '//*[@id="flowName"]', "clearandsend", "FN_1")
if enter_flow_details:
    print("enter_flow_details")

select_service = find(driver, "xpath",
                      '/html/body/div[1]/div[5]/div[10]/div[2]/div/div/div[1]/div/div[1]/div[1]/select', "send", "8")
if select_service:
    print("Select_service Done")

frame_size = find(driver, "xpath", '/html/body/div[1]/div[5]/div[10]/div[2]/div/div/div[1]/div/div[1]/div[5]/input',
                  "clearandsend", "87")
if frame_size:
    print("frame_size Done")

reflector_udp_port = find(driver, "xpath",
                          '/html/body/div[1]/div[5]/div[10]/div[2]/div/div/div[1]/div/div[2]/div/input', "clearandsend",
                          "60000")
if reflector_udp_port:
    print("reflector_udp_port Done")

tx_interval = find(driver, "xpath", '/html/body/div[1]/div[5]/div[10]/div[2]/div/div/div[2]/div/div/div/select', "send",
                   "20")
if tx_interval:
    print("tx_interval Done")

done_button = find(driver, "xpath", '/html/body/div[1]/div[5]/div[10]/div[3]/button[1]', "click", "")
if done_button:
    print("done_button Done")

# add_session = find(driver,"xpath",'/html/body/div[1]/div[5]/div[1]/a[1]',"click","")
# if add_session:
#     print("add_session Done")

# add_session_name = find(driver,"xpath",'/html/body/div[1]/div[3]/div[2]/div/input',"clearandsend","sess_2")
# if add_session:
#     print("add_session Done")

# session_done_btn = find(driver, "xpath", '/html/body/div[1]/div[3]/div[3]/button[1]', "click", "")
# if session_done_btn:
#     print("session_done_btn Done")

Change_to_default_frame = switchtoframe(driver, "")
start_test = find(driver, 'xpath', '/html/body/div[3]/md-toolbar/div[1]/div/button[4]', 'click', "")
if start_test:
    print("Test Started Done")

result = Check_test_status(driver)
if result:
    print("result Done")
else:
    print("Test Submission Failed")
# ActionChains(driver) \
#     .key_down(Keys.ALT) \
#     .send_keys('s') \
#     .key_up(Keys.ALT) \
#     .perform()

# enable_shortcut = find(driver, "id", 'srcStartingPort', "keys", "alt+s")
# if enable_shortcut:
#     print("enable_shortcut set")
# while driver.find_element_by_id("input_0").is_displayed() is False:
#     print("Waiting for pwd field")
#
# driver.find_element_by_id("input_0").send_keys('admin')
# driver.find_element_by_id("input_1").send_keys('default')
# driver.find_element_by_id("input_1").submit()
# driver.find_element_by_xpath('/html/body/md-toolbar/div/div[3]/button[3]').click()
# driver.find_element_by_id('input_2').send_keys("genericx86-64-15833053590")
# driver.find_element_by_xpath('/html/body/div[3]/md-content/div/vi-testpoint-select/div[2]/div/div[1]/div/div/div[5]/button[1]').click()
#

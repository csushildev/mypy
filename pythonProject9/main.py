import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#open browser
driver = webdriver.Chrome()
time.sleep(3)

#BLOCK 1
"""
**** Block one is to test the element locator and browse throught pages. 
but since we dont have success page or url in pega as of now. for login assertion will 
create a block two.

#go to webpage
driver.get("http://localhost:9090/prweb/PRServlet/app/default/beEBp4uRVTogorRwSwWqbOtn9IL2fwdI*/!STANDARD")
time.sleep(3)

#username locator
username_locator = driver.find_element(By.ID, "txtUserID")
username_locator.send_keys("scdev@gms")

#password locator
password_locator = driver.find_element(By.ID, "txtPassword")
password_locator.send_keys("install")

#submit button locator
submit_locator = driver.find_element(By.XPATH, "/html//button[@id='sub']")
submit_locator.click()

actual_url = driver.current_url

if actual_url.__contains__("renewable"):
    print("login to rems was successful")
else:
    print("login to rems failed")

time.sleep(5)
#print(actual_url)
"""
# BLOCK 2
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(2)

login_message_locator=driver.find_element(By.XPATH, "//div[@id='content']//p")
actual_message=login_message_locator.text

#assert actual_message == "Congratulations! You must have the proper credentials"
assert actual_message.__contains__("Congratulations")



"""
these are extra comments or roughwork for the above testing.

# samples from pega PE login page :
# GENERIC XPATH Format:  //tag[@attribute='value']
# //input[@id='txtUserID']
# /html//button[@id='sub']
# /html//input[@id='txtUserID']
# /html//input[@id='txtPassword']
# # //button[@id]

#//aside[@id='sidebar-region-one']/div/div[@id='RULE_KEY']/div[2]//button[@title='SC']
#loginsuccess 
/html//button[@id='sub']


#/html//a[@id='spnLoginFrgtPwd']





# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



"""
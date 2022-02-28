#  Selenium
import sys
from time import sleep
import moodle_locators as locators
from selenium import webdriver  # imports selenium to the file
from selenium.webdriver.chrome.service import Service
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options

# Moodle Test Plan Automation
# Launch Moodle APP WEBSITE - Validate
# Navigate to log in screen - Validate
# Login with admin account - Validate we are on dashboard page
# Navigate to add new user page - Validate
# Populate the new user using Faker fake data
# submit the form - validate
# search for new user - Validate
# logout
# login with new user credentials - validate
# logout
# login admin
# search for new user
# delete new user


# create variable & specify path

# create a Chrome driver instance, specify path to chromedriver file
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


# driver= webdriver.Chrome('chromedriver.exe')

# driver= webdriver.Chrome('chromedriver.exe')

# ---------------------------------------------


def setUp():
    print(f'Launch {locators.app} App')
    # print(f'Launch Moodle App')
    print('-----------------------*-----------------------')

    # Make browser full screen
    driver.maximize_window()

    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)

    # Navigate to Moodle app website
    driver.get(locators.moodle_url)

    # Check that Moodle URL and the home page title are displayed
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print(f' Yey! {locators.app}  Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
        # driver.close()
    else:
        print(f'{locators.app}  Moodle did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url} Page Title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('-----------------------*-----------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


#Login to Moodle

def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:
            print(f'{locators.app} Application Login Page is Displayed')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)  # method1 using ID
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()

            # Validate we are at the dashboard

            # LOCATORS PRACTICE XPATH
            # method2 Xpath
            # driver.find_element(By.XPATH,'//button[contains(.,"Log in")]').click()
            # method3
            # driver.find_element(By.XPATH, '//button[contains(@id,"loginbtn")]').click()
            # method 4
            # driver.find_element(By.XPATH,'//button[@id="loginbtn"]').click()
            # method5
            # driver.find_element(By.XPATH,'//*[@id="loginbtn"]').click()

            # CSS Selectors #method 1
            # driver.find_element(By.CSS_SELECTOR,'button[id="loginbtn"]').click()
            # CSS Selectors #method 2
            # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()

            if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashborad_url:
                assert driver.current_url == locators.moodle_dashborad_url
                assert driver.title == locators.moodle_dashboard_page_title
                print('Login is Successful! Moodle Dashboard is displayed - Page title:', driver.title)
            else:
                print('Dashboard is not displayed, check your code and try again!!')


def log_out():
    # driver.find_element(By.CLASS_NAME,'user picture default user pic').click()
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print('')
        print('Logout Successful!!')
        print(f'Webpage URL after Logout : {driver.current_url}')
        print(f'Webpage Title after logout : {driver.title}')
        print('')
        sleep(2)
    else:
        print('Logout not Successful!!')
        tearDown()


def create_new_user():
    # Navigate to site administration
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    # validate we are on add new user page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.add_new_user_page_title
    print('')
    print(f'---------Navigate to add new user page --> Page Title :{driver.title}')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    # select an option 'Allow eveyone to see
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text(
        'Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_value('America/Vancouver')
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_lang')).select_by_value('en')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    # click picture
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)
    # Navigate to image
    # driver.find_element(By.XPATH,'//span[contains(.,"Server files")]').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_Frozen').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'Course image').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT,'gieEd4R5T.png').click()
    # sleep(0.25)
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    # select radio button
    # method1
    driver.find_element(By.XPATH, '//input[@value="4"]').click()
    # method2
    # driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)

    # populate ADDITIONAL NAMES
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)

    # Populate Intrest
    driver.find_element(By.LINK_TEXT, 'Interests').click()
    for tag in locators.list_of_interest:
        # driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + Keys.ENTER)
        # driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + "\n")
        driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(tag + ",")
        sleep(0.25)
        # driver.find_element(By.XPATH, '//input[contains(@id,"form_autocomplete_input")]').send_keys(Keys.ENTER)

    # Populating Optional

    driver.find_element(By.LINK_TEXT, 'Optional').click()

    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        # print(f'Populate {opt}')
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(0.25)

    driver.find_element(By.ID, 'id_submitbutton').click()
    print(
        f'---------New User {locators.new_username}, {locators.new_password}, {locators.email} is added -----------------')
    sleep(0.25)


def search_user():
    assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
    sleep(0.25)
    if driver.current_url == locators.moodle_users_main_page and driver.title == locators.moodle_users_main_page_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        assert driver.title == locators.browse_list_of_users_title
        print('')
        print('Browser Users Webpage Title : ', driver.title)
        print('Browser Users Webpage URL :', driver.current_url)
        print('')
        sleep(0.25)
        print(f'-------Search for user by email address : {locators.email}---------')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'Newly Created user {locators.full_name} now exist in our database with {locators.email}')


# def newuser_login(username,password):
#     if driver.current_url == locators.moodle_url:
#         driver.find_element(By.LINK_TEXT, 'Log in').click()
#         if driver.current_url == locators.moodle_login_page_url:
#             print(f'{locators.app} Application Login Page is Displayed')
#             sleep(0.25)
#             driver.find_element(By.ID, 'username').send_keys(username)  # method1 using ID
#             sleep(0.25)
#             driver.find_element(By.ID, 'password').send_keys(password)
#             sleep(0.25)
#             driver.find_element(By.ID, 'loginbtn').click()


def check_new_user_can_login():
    if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashborad_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'------ User with {locators.full_name} is displayed------ ')
            logger('Created')


def delete_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    search_user()
    driver.find_element(By.XPATH, '//i[@title = "Delete"]').click()
    driver.find_element(By.XPATH, '//button[contains(.,"Delete")]').click()
    print('')
    print(f'The New User {locators.full_name} is Now Deleted')
    logger('Deleted')


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{locators.new_username}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# setUp()
# log_in(locators.admin_username, locators.admin_password)
# create_new_user()
# search_user()
# log_out()
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# log_out()
# # logger('created')
# log_in(locators.admin_username, locators.admin_password)
# # delete new user
# delete_user()
# log_out()
# # logger('deleted')
# tearDown()

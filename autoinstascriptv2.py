from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

# getting handles from file

#last messaging run was Book9

with open('Book9.csv', 'r', encoding = 'utf-8-sig') as handlesfile:
    handles = []
    check = 'initial'
    while check != '':
        handle = handlesfile.readline()
        check = handle
        handles.append(handle.strip())


#receiver handles
user = handles
message_ = ('hey! i was going through ig profiles because my team in bastrop is looking to expand and reach out to people who live / have lived in the area and your profile stood out. the job is an entry level sales / service position. it\'s super flexible, you don\'t need any experience, and you can work remotely / from home. would you be interested in hearing more about part time summer work? if so, lmk and i\'ll send more info! thanks :)')

class bot:
    
    def __init__(self, username, password, audience, message):
        
        #initializing username
        self.username = username
        
        #initializing password
        self.password = password
        
        #passing the list of user or initializing
        self.user = user
        
        #passing the message of user or initializing
        self.message = message
        
        #initializing the base url
        self.base_url = 'https://www.instagram.com/'
        
        #calls the driver to open chrome web browser
        self.bot = driver
        
        #initializing login function
        self.login()
        
    
    def login(self):
        self.bot.get(self.base_url)
        
        #entering username for login 
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        
        enter_username.send_keys(self.username)
        
        #entering password for login
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        
        #returning the password and logging in to the account
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        
        #first pop up
        first_pop_up = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        first_pop_up.click()
        time.sleep(5)
        
        #second pop up
        second_pop_up = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
        second_pop_up.click()
        
        #dm button
        dm_button = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')))
        dm_button.click()
        
        #pencil button
        pencil_button = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')))
        pencil_button.click()
        
        #loop to send messages
        for i in user:
            
            print("user is:", i)
            
            #enter handle
            enter_handle = WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input')))
            enter_handle.send_keys(i)
            time.sleep(2)
            
            #click on the handle
            click_handle = WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[2]/div[2]/div')))
            click_handle.click()
            print("    clicked handle")
            time.sleep(1)
            
            #click next
            click_next = WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[1]/div/div[3]/div/button/div')))
            click_next.click()
            print('    clicked next')
            time.sleep(2)
            
            #click message box
            send_message = WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')))
            send_message.click()
            print('    clicked message box')
            #types message
            send_message.send_keys(self.message)
            time.sleep(1)
            #sends message
            send_message.send_keys(Keys.RETURN)
            print('    sent message')
            
            #clicks on pencil icon again
            pencil_button = WebDriverWait(self.bot, 20).until(
                expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')))
            pencil_button.click()
            #time.sleep(2)
            
def init():
    bot('qthan_rutt', 'Sul;comcom', user, message_)
    
    print('DONE')
    
init()
            
            
            
            
            
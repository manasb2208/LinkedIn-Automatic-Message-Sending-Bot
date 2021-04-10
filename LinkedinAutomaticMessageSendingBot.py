email = 'manasb2208@gmail.com'
password = 'Alienbrains@700074'
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe" #chorome driver path 
from selenium import webdriver
import time

driver = webdriver.Chrome(cd) #creating webdriver
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin") #to go to the sign in page of linked in 
time.sleep(5)

eml=driver.find_element_by_xpath('//*[@id="username"]')
eml.send_keys(email)
pswrd = driver.find_element_by_xpath('//*[@id="password"]')
pswrd.send_keys(password)
btn=driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
btn.click()

time.sleep(2)
driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
time.sleep(2)
connection = driver.find_element_by_xpath('//*[@id="ember49"]/header/h1').text
print(connection)
connection = connection[0]
connection = int(connection)
print(connection)

#scroll over all the connections
i=0
while (i<connection):
	time.sleep(1)
	pgsource=driver.page_source # return the source code
	ref=BeautifulSoup(pgsource,'html.parser') #it refers to the soup element /translated element
	selection_all=ref.findAll('li',{'class':"mn-connection-card artdeco-list ember-view"})
	i=len(selection_all)
	driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	driver.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	
print(len(selection_all))

#Extracting the data and making the list of profile link of all connections. 
connection_list=[]
for i in selection_all:
	q=i.find('a',{'class':"ember-view mn-connection-card__link"})
	profile_link=q.get('href')
	connection_list.append(profile_link)


message='Hello! This is a test message by a message sending bot.Please ignore.Thank you.' #message which is to be sent


url1="https://www.linkedin.com/"
for i in connection_list:
	url=url1+i
	driver.get(url)
	time.sleep(5)
	btn1=driver.find_element_by_xpath('//*[@class="message-anywhere-button pv-s-profile-actions pv-s-profile-actions--message ml2 artdeco-button artdeco-button--2 artdeco-button--muted artdeco-button--primary"]')
	btn1.click()
	time.sleep(1)
	msg=driver.find_element_by_xpath('//*[@class="msg-form__contenteditable t-14 t-black--light t-normal flex-grow-1 full-height notranslate"]')
	msg.send_keys(message)
	msg.send_keys(Keys.ENTER)
	time.sleep(2)
	btn2 = driver.find_element_by_xpath('//*[@class="msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]')
	btn2.click()

print("Done")
time.sleep(30)
driver.close()
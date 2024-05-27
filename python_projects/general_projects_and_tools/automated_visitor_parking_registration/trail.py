from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver_path = '../chromedriver\chromedriver.exe'
try:
    # Check if a driver instance already exists
    if driver is not None:
        # If yes, close the existing driver
        driver.quit()
except NameError:
    pass

driver = webdriver.Chrome()
driver.get("https://parking.com") # website hidden for legal reasons
time.sleep(1)
propertname='propertname' 
apt=2333
make='Honda'
model='Accord'
lplate='platenumber'
email='email'


p_name=driver.find_element(By.ID,'propertyName')
p_name.send_keys(propertname)

confirm=driver.find_element(By.ID,'confirmProperty')
confirm.click()

time.sleep(1)
mainform=driver.find_elements(By.CLASS_NAME,'property')
mainform[1].click()

confirm2=driver.find_element(By.ID,'confirmPropertySelection')
confirm2.click()

confirm3=driver.find_element(By.ID,'registrationTypeVisitor')
confirm3.click()
time.sleep(1)

carform=driver.find_element(By.ID,'property-name-form')
carform

f_apt=driver.find_element(By.ID,'vehicleApt')
f_make=driver.find_element(By.ID,'vehicleMake')
f_model=driver.find_element(By.ID,'vehicleModel')
f_lplate1=driver.find_element(By.ID,'vehicleLicensePlate')
f_lpate2=driver.find_element(By.ID,'vehicleLicensePlateConfirm')


f_apt.send_keys(apt)
f_make.send_keys(make)
f_model.send_keys(model)
f_lplate1.send_keys(lplate)
f_lpate2.send_keys(lplate)

time.sleep(1)

carform=driver.find_element(By.ID,'vehicleInformation')
carform.click()
time.sleep(1.5)
# success
current_time = datetime.now().strftime("%m-%d-%Y_%H%M")
success=driver.find_elements(By.CLASS_NAME,'circle-success')
if len(success):
    print('The vehicle listed above is approved\nto park in an authorized space.')
    conf=driver.find_element(By.XPATH,r"//div[@class='circle-success']/div[@class='circle-inner']/h3").text
    print(conf)
    success[0].screenshot(f'C:/Users/moata/Desktop/ParkingConf/{current_time}_{conf}.png')
    # time.sleep(1)
    # emailconf=driver.find_element(By.ID,'email-confirmation')
    # emailconf.click()
    # time.sleep(1)


    # emailenter=driver.find_element(By.ID,'emailConfirmationEmailView')
    # emailenter.send_keys(email)

    # time.sleep(1)
    # emailsend=driver.find_element(By.ID,'email-confirmation-send-view')
    # emailsend.click()


    input('Press enter to exit!')
    driver.quit()
else:
    print('Somehting went wrong!!')
    input('Press enter to exit!')
    
    
    


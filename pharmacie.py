from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url ="https://www.abrp.bj/officine.php"
PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(url)

buton = driver.find_element(By.CLASS_NAME,'close')
time.sleep(3)
buton.click()
time.sleep(30)

print("Debut du programme")
mon_fichier = open("fichierPharmacie.json", "a")

def separate(leSeparate):
   liste = []
   liste = leSeparate.split(" ")
   return liste


count = 1
leId = 1
while count < 5:
   tr = 1
   while tr < 101:
      lepath = '//*[@id="example"]/tbody/tr' + str([tr]) 
      
      nomPharmacie = driver.find_element(By.XPATH, lepath+'/td[6]')
      doctor = driver.find_element(By.XPATH, lepath+'/td[8]')
      communeBrute = driver.find_element(By.XPATH, lepath+'/td[4]')
      commune = separate(communeBrute.text)[0]
      indication = driver.find_element(By.XPATH, lepath+'/td[7]')
      number1Brute = driver.find_element(By.XPATH, lepath+'/td[9]')
      number2Brute = driver.find_element(By.XPATH, lepath+'/td[10]')
      
      leData = {
         "id":leId,
         "name":nomPharmacie.text,
         "garde": True,
         "doctor":doctor.text,
         "commune": commune,
         "indication": indication.text,
         "assurance": ["NSIA","AFRICAINE DES ASSURANCES","SAHAM","UBA"],
         "paie": ["MTN Mobile Money","Moov Money", "Espece"],
         "number": ["+229 60000000","+229 67000000"],
         "number1Brute":number1Brute.text,
         "number2Brute":number2Brute.text,
         "numberWhatsApp":"+229 60000000",
         "numberCall":"+229 65000000",
         "location":{
            "latitude":6.358803255597362,
            "longitude":2.3704744306877275
         }
      }
      
      json.dump(leData,mon_fichier, indent=3)
      tr +=1 
      leId +=1
   print('Avant le clic dans 5 seconde')
   time.sleep(5)
   WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="example_next"]'))).click()
   print('le clic')
   time.sleep(5)
   count +=1
driver.close()


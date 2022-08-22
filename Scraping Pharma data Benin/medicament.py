from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url ="https://www.abrp.bj/medicamentsautorises.php"
PATH = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(url)
buton = driver.find_element(By.CLASS_NAME,'close')
time.sleep(3)
buton.click()
time.sleep(60)

print("Debut du programme")
mon_fichier = open("fichieron.json", "a")

def separate(leSeparate):
   liste = []
   liste = leSeparate.split("+")
   return liste


        
cou = 1
leId = 2100
while cou < 25:
    tr = 1
    while tr < 101:
        lepath = '//*[@id="example"]/tbody/tr' + str([tr]) 
        
        designation = driver.find_element(By.XPATH, lepath+'/td[2]')
        dci = driver.find_element(By.XPATH, lepath+'/td[3]')
        dosage = driver.find_element(By.XPATH, lepath+'/td[4]')
        forme = driver.find_element(By.XPATH, lepath+'/td[5]')
        voie = driver.find_element(By.XPATH, lepath+'/td[6]')
        presentation = driver.find_element(By.XPATH, lepath+'/td[7]')
        classeTherap = driver.find_element(By.XPATH, lepath+'/td[8]')
        codeAMM = driver.find_element(By.XPATH, lepath+'/td[9]')
        dateExpire = driver.find_element(By.XPATH, lepath+'/td[10]')
        fabriquant = driver.find_element(By.XPATH, lepath+'/td[11]')
        demandeur = driver.find_element(By.XPATH, lepath+'/td[12]')
        pght = driver.find_element(By.XPATH, lepath+'/td[13]')
    
        dci = separate(dci.text)
        dosageListe = []
        dosageListe = separate(dosage.text)
        print(dosageListe)
        listes = []
        count = 0
        print(len(dci))
        print(len(dosageListe))
        
        if (dosage.text == "-"):
            while count < len(dci):
                print(dci[count])
                listes.append({"name": dci[count], "dosage":"-"})
                print(listes)
                count +=1
        elif (len(dosageListe) != len(dci)):
            if (len(dosageListe) < len(dci)+1):
                dosageListe.append("-")
                while (len(dosageListe) != len(dci)) :
                    dosageListe.append("-")
                    
                while count < len(dci):
                    print(dci[count])
                    listes.append({"name": dci[count], "dosage":dosageListe[count]})
                    print(listes)
                    count +=1
            elif (len(dosageListe)+1 > len(dci)):
                dci.append("-")
                while (len(dosageListe) != len(dci)) :
                    dci.append("-")
                while count < len(dci):
                    print(dci[count])
                    listes.append({"name": dci[count], "dosage":dosageListe[count]})
                    print(listes)
                    count +=1
        elif (len(dosageListe) == len(dci)):
            dosage = separate(dosage.text)
            while count < len(dci):
                print(dci[count])
                listes.append({"name": dci[count], "dosage":dosage[count]})
                print(listes)
                count +=1
    
        print (listes)
        leData = {
            "id":leId,
            "designation":designation.text,
            "dcifrancais":listes,
            "forme":forme.text,
            "voie":voie.text,
            "presentation":presentation.text,
            "classeTherap":classeTherap.text,
            "codeAMM":codeAMM.text,
            "dateExpire":dateExpire.text,
            "fabriquant":fabriquant.text,
            "demandeur":demandeur.text,
            "PGHT":pght.text
        }
        
        leId +=1
        json.dump(leData,mon_fichier, indent=3)
        tr +=1 
        
        
    print('Avant le clic dans 5 seconde')
    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="example_next"]'))).click()
    print('le clic')
    time.sleep(5)
    cou +=1
driver.close()


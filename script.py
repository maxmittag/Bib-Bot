from matplotlib import image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

from selenium.webdriver.common.by import By

def PlatzReservieren(FavPlatz1, FavPlatz2, FavPlatz3, FavPlatz4, FavPlatz5, benutzername, Passwort):

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://sso.uni-muenster.de/ULB/sso/wwu/platzreservierung/")
    #driver.maximize_window()

    #benutzername = 'mmittag'
    #Passwort = 'M@X.MITt1234'
    
    #Variablen vereinbaren
    benutzername = benutzername
    Passwort = Passwort
    FavPlatz1 = FavPlatz1
    FavPlatz2 = FavPlatz2
    FavPlatz3 = FavPlatz3
    FavPlatz4 = FavPlatz4
    FavPlatz5 = FavPlatz5

    benutzernameSeite = driver.find_element(By.ID, 'httpd_username')
    PasswortSeite     = driver.find_element(By.ID, 'httpd_password')
    
    benutzernameSeite.send_keys(benutzername)
    PasswortSeite.send_keys(Passwort)

    #time.sleep(3)

    Anmeldebutton = driver.find_element(By.XPATH, "//input[@value='Anmelden / login']")
    Anmeldebutton.click()


    #Bild raussuchen
    bild = driver.find_element(By.XPATH, "//div[@class='ym-fbox ym-fbox-text']//img")

    #Bild screenshoten
    bild.screenshot(r'C:\Users\maxmi\Pictures\ocr-test.png')
    image = Image.open(r'C:\Users\maxmi\Pictures\ocr-test.png')

    #captcha speichern
    captchaWort = pytesseract.image_to_string(image)

    TEST = "TESTEN"
    #captcha eingeben
    captchfeld = driver.find_element(By.ID, 'captcha')
    captchfeld.send_keys(captchaWort)


    #kontrolle ob geklappt
    def erfolg():
        try:
            driver.find_element(By.XPATH, "//span[normalize-space()='Erfolg:']")
            return True
        except NoSuchElementException:
            return False

    while(erfolg() == False):
        #Bild raussuchen
        bild = driver.find_element(By.XPATH, "//div[@class='ym-fbox ym-fbox-text']//img")

        #Bild screenshoten
        bild.screenshot(r'C:\Users\maxmi\Pictures\ocr-test.png')
        image = Image.open(r'C:\Users\maxmi\Pictures\ocr-test.png')

        #captcha speichern
        captchaWort = pytesseract.image_to_string(image)

        #captcha eingeben
        captchfeld = driver.find_element(By.ID, 'captcha')
        captchfeld.send_keys(captchaWort)

    
    #weiter Button clicken
    weiterButton = driver.find_element(By.XPATH, "//a[@class='ym-button ym-next ym-success']")
    weiterButton.click()

    #bestimmte bibliothek
    bestimmteBibliothek = driver.find_element(By.XPATH, "//a[normalize-space()='Zur Auswahl der Bibliothek']")
    bestimmteBibliothek.click()

    #Zentralbibliothek
    zentralBibliothek = driver.find_element(By.XPATH, "//a[normalize-space()='Zentralbibliothek']")
    zentralBibliothek.click()

    #Tag/timeslot finden:

    #                                                                                                                                T
    westfalica = driver.find_element(By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/table[2]/tbody[1]/tr[3]/td[3]/a[1]")
    westfalica.click()

    #Plätze finden und auswählen:

    try:
        platz1=driver.find_element(By.XPATH, "//a[normalize-space()='Platz "+ FavPlatz1 +"']")
        platz1.click()
        print("Erfolgreich Platz 1 für " +  benutzername + " ausgewählt")
    except NoSuchElementException:
        try:
            platz2=driver.find_element(By.XPATH, "//a[normalize-space()='Platz "+ FavPlatz2 +"']")
            platz2.click()
            print("Erfolgreich Platz 2 für " +  benutzername + " ausgewählt")
        except NoSuchElementException:
            try:
                platz3=driver.find_element(By.XPATH, "//a[normalize-space()='Platz "+ FavPlatz3 +"']")
                platz3.click()
                print("Erfolgreich Platz 3 für " +  benutzername + " ausgewählt")
            except NoSuchElementException:
                try:
                    platz4=driver.find_element(By.XPATH, "//a[normalize-space()='Platz "+ FavPlatz4 +"']")
                    platz4.click()
                    print("Erfolgreich Platz 4 für " +  benutzername + " ausgewählt")
                except NoSuchElementException:
                    try:
                        platz5=driver.find_element(By.XPATH, "//a[normalize-space()='Platz "+ FavPlatz5 +"']")
                        platz5.click()
                        print("Erfolgreich Platz 5 für " +  benutzername + " ausgewählt")
                    except NoSuchElementException:
                        print("Kein Platz gefunden für " + benutzername + " gefunden")
                        #driver.quit()
                        #exit()
            
    
    

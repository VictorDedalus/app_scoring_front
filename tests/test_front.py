import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dashboard():
    # Instancier le navigateur
    driver = webdriver.Chrome()

    try:
        # Ouvrir le dashboard Streamlit
        driver.get("https://appscoringfront-c56b4417d98a.herokuapp.com/")

        # Attendre un court instant pour que le dashboard se charge
        time.sleep(15)

        #Le tableau initial du choix d'user_id s'affiche-t-il ?
        driver.find_element("xpath",'//*[contains(concat( " ", @class, " " ), concat( " ", "glideDataEditor", " " ))]')

    finally:
        # Fermer le navigateur
        driver.quit()
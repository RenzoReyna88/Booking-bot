from scraper import InitWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from icecream import ic
import pandas as pd
import random


class ScrapBookingSite(InitWeb):

    def scrap_booking(self):

        url_booking = "https://www.booking.com/searchresults.es.html?label=gen173rf-1FCAMoDEIHbWVuZG96YUgsWANoDIgBAZgBLLgBF8gBDNgBAegBAfgBA4gCAaICC2NoYXRncHQuY29tqAIDuAK9ypG-BsACAdICJGIxN2FhY2NiLTEwZjYtNDgyYS1hNTk4LTkxMjJmNDAxNzI3ONgCBeACAQ&aid=304142&ss=Uspallata%2C+Provincia+de+Mendoza%2C+Argentina&ssne=Tupungato&ssne_untouched=Tupungato&lang=es&src=searchresults&dest_id=-1018188&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=es&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=6c456d40ecf301b2&checkin=2025-04-01&checkout=2025-05-01&group_adults=2&no_rooms=2&group_children=1&age=7&nflt=ht_id%3D220"

        self.driver.get(url_booking)

        time.sleep(30)  # Esperar 24 segundos a que cargue la página 


        # Comprobar si existen ventanas emergentes o de notificaciones para quitar
        try:    
            pop_ups = self.driver.find_element(By.XPATH, '//*[@id="b2searchresultsPage"]/div[21]/div/div/div/div[1]/div[1]/div/button/span')
            time.sleep(2) 
            pop_ups.click()
        except NoSuchElementException:
            pop_ups = "No disponible"

        self.driver.maximize_window()

        try:
            notice_banner = self.driver.find_element(By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/section[1]/div/div/div/div/div/button/span')
            time.sleep(4)
            notice_banner.click()
        except NoSuchElementException:
            notice_banner = "No disponible"
            
        try:
            seconds_notice_banner = self.driver.find_element(By.XPATH, '//*[@id="bodyconstraint-inner"]/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/section[1]/div/div/div/div/div/button')
            print(seconds_notice_banner)

            time.sleep(3)
            seconds_notice_banner.click()
        except NoSuchElementException:
            seconds_notice_banner = "No disponible"

        try:
            # Localizar los elementos en la web
            publications = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card-container"]')
            print(f"Total de publicaciones encontradas: {len(publications)}")

            data_booking = []


            for publication in publications:
                    
                    try:
                        name_hotel = publication.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text.strip()
                    except NoSuchElementException:
                        name_hotel = "No disponible"

                    try:
                        price_hotel = publication.find_element(By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]').text.strip()
                    except NoSuchElementException:
                        price_hotel = "No disponible"

                    try:
                        distance_center = publication.find_element(By.CSS_SELECTOR, 'span[data-testid="address"]').text.strip()
                    except NoSuchElementException:
                        distance_center = "No disponible"

                    data_booking.append({
                                "Nombre Hotel":name_hotel,
                                "Precio Hotel":price_hotel,
                                "Distancia al centro":distance_center
                            })
                    
            # Convertir datos DataFrame y luego gardarlo en un archivo CSV 
            try:
                datos_hoteles_booking = pd.DataFrame(data_booking)
                datos_hoteles_booking.to_csv("Datos-CasasYChalets-Uspallata.csv", index=False, encoding='utf-8')
                ic("Los datos fueron cargados con éxito en el archivo CSV") 
            except Exception as e:
                 print(f"Error{e}: Los datos no fueron cargados en el archvivo CSV")

 
        finally:
            ic("Scraping finalizado")    
   

    def close_navegator(self):
        time.sleep(random.randint(9, 12))
        self.driver.quit() # Cerrar navegador web


bot_booking = ScrapBookingSite() 

bot_booking.scrap_booking()

bot_booking.close_navegator()
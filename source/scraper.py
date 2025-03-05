from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from icecream import ic



class InitWeb:

    def __init__(self):
    
        try:
            # Configurar opciones y servicio del navegador
            chrome_options = Options()
            chrome_options.page_load_strategy = 'normal'
            chrome_options.add_argument('''user-agent=Mozilla/5.0 (Windows NT 10.O; Win64; x64) 
                                        ApplewebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36''')
            chrome_options.add_experimental_option('detach', True)
            service = Service(ChromeDriverManager().install())
            # Inicializar el driver
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            ic("Conexión éxitosa al navegador chrome")

        except Exception as e:
            ic(f"Error de conexión al Navegador: {e}")

if __name__ == '__main__':
    
    bot = InitWeb()
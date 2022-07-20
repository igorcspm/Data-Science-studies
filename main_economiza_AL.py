from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import barcode_scanner
import parse_economiza_AL
import take_photo

def economiza_AL_scrap_to_df(barcode=None, image_path=None):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('headless')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # acessando a página
    driver.get('https://economizaalagoas.sefaz.al.gov.br/')
    driver.maximize_window()

    if barcode is None:
        if image_path is None:
            # tira foto
            image_path = take_photo.take_photo()

        # código de barras extraído da foto selecionada
        barcode = barcode_scanner.extract_barcode(image_path)

    sleep(5)

    preenche_barcode = driver.find_element(By.ID, 'textoConsulta')
    preenche_barcode.send_keys(barcode)
    preenche_barcode.submit()

    sleep(5)

    try:
        click_categoria = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[1]/div[1]/li[1]')
        click_categoria.click()
    except:
        raise ValueError('Categoria não encontrada')

    sleep(5)

    df = parse_economiza_AL.scrap_economiza_AL(driver.page_source)

    driver.close()
    driver.quit()

    return df
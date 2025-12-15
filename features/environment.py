from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    # Configurações globais (opcional)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    context.chrome_options = chrome_options

def before_scenario(context, scenario):
    # Abre o navegador no início de cada cenário
    context.browser = webdriver.Chrome(options=context.chrome_options)

def after_scenario(context, scenario):
    # Fecha o navegador após cada cenário
    if context.browser:
        context.browser.quit()

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for(context, by, value):
    return WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((by, value))
    )

def click_when_clickable(context, by, value):
    return WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((by, value))
    ).click()




@given("que o navegador está aberto")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()


@given("que estou na página inicial do site SauceDemo")
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/")


@when('informo o usuário "{usuario}"')
def step_impl(context, usuario):
    campo = wait_for(context, By.ID, "user-name")
    campo.clear()
    campo.send_keys(usuario)


@when('informo a senha "{senha}"')
def step_impl(context, senha):
    campo = wait_for(context, By.ID, "password")
    campo.clear()
    campo.send_keys(senha)


@when("clico no botão de login")
def step_impl(context):
    click_when_clickable(context, By.ID, "login-button")


@then("devo ver a lista de produtos carregada")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("inventory")
    )


@then('o título da página deve ser "Products"')
def step_impl(context):
    titulo = wait_for(context, By.CLASS_NAME, "title")
    assert titulo.text == "Products"


@given("que estou logado no sistema")
def step_impl(context):
    context.execute_steps('''
        When informo o usuário "standard_user"
        And informo a senha "secret_sauce"
        And clico no botão de login
    ''')


@when('clico no produto "{nome_produto}"')
def step_impl(context, nome_produto):
    elemento = wait_for(context, By.XPATH, f"//div[text()='{nome_produto}']")
    elemento.click()


@then("devo ver a página de detalhes desse produto")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_contains("inventory-item")
    )


@then('o botão "Add to cart" deve estar visível')
def step_impl(context):
    btn = wait_for(context, By.XPATH, "//button[contains(text(),'Add to cart')]")
    assert btn.is_displayed()


@when('adiciono o produto "{nome_produto}" ao carrinho')
def step_impl(context, nome_produto):
    # abrir o produto
    wait_for(context, By.XPATH, f"//div[text()='{nome_produto}']").click()

    # clicar no botão de adicionar ao carrinho
    click_when_clickable(context, By.XPATH, "//button[contains(text(),'Add to cart')]")


@then('o ícone do carrinho deve mostrar "1"')
def step_impl(context):
    badge = wait_for(context, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"


@then('devo ver "{texto}"')
def step_impl(context, texto):
    body = wait_for(context, By.TAG_NAME, "body")
    assert texto in body.text

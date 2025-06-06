import os
from dotenv import load_dotenv
load_dotenv()

LOGIN = os.getenv("METRIX_LOGIN")
SENHA = os.getenv("METRIX_SENHA")

# Importa a API síncrona do Playwright
from playwright.sync_api import sync_playwright

#Primeiro teste: valida se o botão "Login" da home leva à pagina de login
def teste_login_player():
    with sync_playwright() as p:
        #Inicia o navegador Chromium (sem headless para visualizar)
        browser = p.chromium.launch(headless=False)

        # Abre uma nova aba
        page = browser.new_page()

        # passo 1: Acessa a página inicial do Metrix
        page.goto("https://staging.metrix.bet")


        # passo 2: Acessar a pagina de login do Metrix
        page.locator(
            "body > div.container-fluid.navbar_limit.desktop.blue_header_footer_background > div > div:nth-child(3) > div > div.col-11 > div > div"
        ).click()

        # Passo 3: Aguarda o redirecionamento para a tela de login
        page.wait_for_url("**/player_login", timeout=5000)

        #Passo 4: Preencher o campo de LOGIN
        page.locator('xpath=//*[@id="id_phone"]').fill(LOGIN)

        #Passo 5: Clicar no botão "Entrar"
        page.locator('xpath=//*[@id="loginInput"]/form/div[4]/div/input[2]').click()


        #Passo 6: Preencher o campo de SENHA
        page.locator('xpath=//*[@id="password"]').fill(SENHA)
        
        #Passo 7: Clicar no botão "Entrar"
        page.locator('xpath=//*[@id="loginInput"]/form/div[4]/div/input[2]').click()

        #Passo 8: Aguarda a pagina carregar 9s
        page.wait_for_timeout(5000)

        page.locator('a.btn-regular[href="/play/1245/"]').click()


        #Espera 9 segundos antes de fechar, para visualizar
        page.wait_for_timeout(19000)

        # Fecha o browser
        browser.close()

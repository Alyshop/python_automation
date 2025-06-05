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
        page.locator('xpath=//*[@id="id_phone"]').fill("11000000001")

        #Passo 5: Clicar no botão "Entrar"
        page.locator('xpath=//*[@id="loginInput"]/form/div[4]/div/input[2]').click()


        #Passo 6: Preencher o campo de SENHA
        page.locator('xpath=//*[@id="password"]').fill("123456")
        
        #Passo 7: Clicar no botão "Entrar"
        page.locator('xpath=//*[@id="loginInput"]/form/div[4]/div/input[2]').click()

        


        #Espera 9 segundos antes de fechar, para visualizar
        page.wait_for_timeout(9000)

        # Fecha o browser
        browser.close()

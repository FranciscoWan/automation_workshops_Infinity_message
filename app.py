from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json
import os

data_atual = datetime.now()
duas_semanas = timedelta(weeks=2)
data_duas_semanas = data_atual + duas_semanas

def cpf_login():
    cpf = input("       Digite o CPF de login: ")
    data = input("      Digite a data (senha) de login: ")
    dados_login = {"cpf": cpf, "data": data}
    with open("login_infinity_app","w",encoding="utf-8") as login_salvo:
        json.dump(dados_login,login_salvo,indent=4,ensure_ascii=False)

def login():
    navegador = webdriver.Chrome()
    navegador.get("https://www.infinityschool.app/area/")
    with open("login_infinity_app","r") as login_salvo:
        login_salvo = json.load(login_salvo)
    try:
        elemento = navegador.find_element(By.NAME, "projectFilePath") # Encontra elemento pelo NAME
        elemento.send_keys(login_salvo["cpf"])
        elemento = navegador.find_element(By.NAME, "data") # Encontra elemento pelo NAME
        elemento.send_keys(login_salvo["data"])
        botao = navegador.find_element(By.CLASS_NAME, "button2")
        botao.click()
        return navegador
    except:
        print("     Elemento não encontrado")

def workshops():
    navegador = login()
    botao = navegador.find_element(By.XPATH, '//*[@id="geral_home"]/div[2]/div[2]/div[1]/form[3]/button') # Acessa a área de aulas compartilhadas (workshops) pelo XPATH
    botao.click()
    time.sleep(2)
    conteudo_html = navegador.page_source
    soup = BeautifulSoup(conteudo_html, 'html.parser')
    info_workshops = soup.find_all(class_="aulas_compartilhadas")
    lista_aulas_compartilhadas = []
    for elemento in info_workshops:
        text_tratado = elemento.text.split("\n")
        lista_aulas_compartilhadas.append(text_tratado)
    lista_dados = []
    chave_dicionario = ["workshop_title","requisito","data","hora","vagas","status"]
    for i in range(len(lista_aulas_compartilhadas)):
        text_list = lista_aulas_compartilhadas[i:i+1][0]
        clean_list = [item.strip() for item in text_list if item.strip()]
        data_workshop = clean_list[2].split(":").pop(1).strip()
        data_workshop_tratada = datetime.strptime(data_workshop, "%d/%m/%Y")
        if data_atual < data_workshop_tratada < data_duas_semanas:
            json_workshops = dict(zip(chave_dicionario, clean_list))
            lista_dados.append(json_workshops)
    with open("calendario_workshops_completo", "w",encoding="utf-8") as arquivo_calendario:
        json.dump(lista_dados,arquivo_calendario,indent=4,ensure_ascii=False)
    enviar_mensagem()

def enviar_mensagem():
    with open("calendario_workshops_completo", "r",encoding="utf-8") as arquivo_calendario:
        workshops = json.load(arquivo_calendario)
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com/")
    input("     Pressione ENTER após escanear o QR code e o WhatsApp Web carregar completamente.")
    with open("grupos_wpp_alunos", "r") as grupos_infinity:
        grupos_alunos_infinity = json.load(grupos_infinity)
    for grupo in grupos_alunos_infinity:
        elemento = navegador.find_element(By.CLASS_NAME, "selectable-text") # Busca a caixa de texto para procurar o grupo
        elemento.send_keys(Keys.CONTROL + "a")  # Seleciona todo o texto (CTRL+A)
        elemento.send_keys(Keys.BACKSPACE) # Garante que o nome do grupo será apagado antes de inserir o próximo nome de grupo
        elemento = navegador.find_element(By.CLASS_NAME, "selectable-text") # Busca a caixa de texto para procurar o grupo 
        elemento.send_keys(grupo)
        time.sleep(5)
        elemento = navegador.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/span') 
        elemento.click()
        elemento = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p') # Garante que a caixa de texto do wpp dentro da cnv esteja selecionado para escrever a msg. (Verificar o XPATH caso dê erro.)
        elemento.send_keys("*Fique por dentro dos workshops que irão rolar essa e próxima semana!*\n")
        for tema_workshop in range(len(workshops)):
            elemento = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p') # Garante que a caixa de texto do wpp dentro da cnv esteja selecionado para escrever a msg. (Verificar o XPATH caso dê erro.)
            mensagem_workshops = f'''*{workshops[tema_workshop]["workshop_title"]}* // `{workshops[tema_workshop]["requisito"]}` // *{workshops[tema_workshop]["data"]}* // *{workshops[tema_workshop]["hora"]}* // {workshops[tema_workshop]["vagas"]}'''
            elemento.send_keys(mensagem_workshops)
            time.sleep(4)
            elemento.send_keys(Keys.ENTER)
            time.sleep(2)
    navegador.quit()

def adc_grupo_wpp():
    lista_grupos = []
    opcao = int(input("     Digite o número de grupos que irá adicionar: "))
    for i in range(opcao):
        nome_grupo = input("        Digite o nome do grupo que deseja adicionar a lista de disparo de mensagens automáticas: ")
        lista_grupos.append(nome_grupo)
    grupos_wpp_alunos = "grupos_wpp_alunos"
    if not os.path.exists(grupos_wpp_alunos):
        with open("grupos_wpp_alunos","w",encoding="utf-8") as arquivo_grupo_alunos:
            json.dump(lista_grupos,arquivo_grupo_alunos,indent=4,ensure_ascii=False)
    else:
        with open("grupos_wpp_alunos","r") as arquivo_grupo_alunos:
            grupos_antigos = json.load(arquivo_grupo_alunos)
            for grupo in grupos_antigos:
                lista_grupos.append(grupo)
            with open("grupos_wpp_alunos","w",encoding="utf-8") as arquivo_grupo_alunos:
                json.dump(lista_grupos,arquivo_grupo_alunos,indent=4,ensure_ascii=False)

def menu():
    while True:
        print('''
        -----------------------------
        Digite a opção desejada - 
        1 - Inserir dados para login
        2 - Adc grupos de whatsapp
        3 - Enviar informações de workshops          
    ''')
        op = int(input("        Opção: "))
        if op == 1:
            cpf_login()
        elif op == 2:
            adc_grupo_wpp()
            print("Grupos adicionados.\n")
        elif op == 3:
            workshops()
            print("Mensagem automática enviada. Até a próxima semana.\n")
            break
        else:
            print("Opção inválida\n")

menu()
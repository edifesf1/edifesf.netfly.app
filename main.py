
#Panda para lidar com excell
import pandas as pd

#para controlar o navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tkinter import *
import time
from datetime import datetime

def main():

#data de expiração
    vardia = 31
    varmes = 3
    varano = 2025
#pega o dia da data
    timedia = datetime.now()
    timemes = datetime.now()
    timeano = datetime.now()
    timedia = timedia.day
    timedia = int(timedia)
    timemes = timemes.month
    timemes = int(timemes)
    timeano = timeano.year
    timeano = int(timeano)
    if(timeano >= varano):
        if(timemes >= varmes):
            if(timedia > vardia):
                strdia = str(timedia)
                strmes = str(timemes)
                strano = str(timeano)
                strdata = strdia + '-' + strmes + '-' + strano
                janela = Tk()
                janela.geometry("600x100")
                janela.title("PROGRAMA EXPIRADO 69 984442503")
                texto = "Expirado em :",strdata," Entre em contato pelo WhatsApp (69) 984442503"
                texto = Label(janela, text=texto)
                texto.pack()
                janela.mainloop()
                exit()

    if(timeano >= varano):
        if(timemes >= varmes):
            if(timedia > vardia-5):
                strdia = str(vardia)
                strmes = str(varmes)
                strano = str(varano)
                strdata = strdia + '-' + strmes + '-' +strano
                janela = Tk()
                janela.geometry("600x100")
                janela.title("ALERTA 69 984442503")
                texto = "Seu Program Expira em :", strdata," Entre em contato pelo WhatsApp (69) 984442503"
                texto = Label(janela, text=texto)
                texto.pack()
                janela.mainloop()
#função abre navegado no link do whatsaapp
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com")
    time.sleep(5)

#função espera logar no whatapp elemento side

    while len(navegador.find_elements(By.XPATH, '//*[@id="side"]/div[2]')) < 1:
        pass
        time.sleep(5)

    #armazena no panda a planilha
    contatos_df = pd.read_excel("Clientes.xlsx")
    #exclui linhas que data esteja vazio
    contatos_df = contatos_df.dropna(subset=["DIA"])
    
    #Partes do link do whatsaapp
    link1 = "https://web.whatsapp.com/send?phone="
    link2 = "&text="

    #pegar dados no excell
    for i, dfdia in enumerate(contatos_df['DIA']):
        #foi necessário tranformar em inteiro para comparar
        dfdia = int(dfdia)
        if dfdia == timedia:
            mensagem = contatos_df.loc[i, 'MSG']
            fone = contatos_df.loc[i, "TELEFONE"]
            
            #tranformei telefone em inteiro e depois em str para juntar em uma variavel
            fone = int(fone)
            fone = str(fone)
            dfdia = str(dfdia)
            link = link1 + fone + link2 + mensagem
            navegador.get(link)
            time.sleep(10)
            navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div/p/span').send_keys(Keys.ENTER)
            time.sleep(10)

###############################
#Chama a função main
main()
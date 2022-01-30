from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import gravar_json
import config

options = webdriver.ChromeOptions()
options.add_argument("--headless") # rodar invisivel, 2 plano
options.add_experimental_option('excludeSwitches', ['enable-logging']) # não mostrar infos 

count = 1

# driver que pega a quantidade de paginas
pathChromeDrive = config.path_chrome_driver
driver = webdriver.Chrome(pathChromeDrive,chrome_options=options)

# verificar se as versoes são compativeis, se não form mostra mensagem
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
if str1[0:2] != str2[0:2]:
    print('Versão do Navegador', str1)
    print('Versão chromeDriver', str2)  
    print("Por favor, fazer download da correta versao chromeDriver")


driver.get('https://programathor.com.br/jobs/page/1')
last_page = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[17]/nav/ul/li[7]/a')
id_last_page = int(last_page.get_attribute("href").split('page/')[1])

for id_page in range(1,(id_last_page+1)):
    driver =  webdriver.Chrome(pathChromeDrive,chrome_options=options)
    driver_data =  webdriver.Chrome(pathChromeDrive,chrome_options=options)

    # baixar o site
    driver.get('https://programathor.com.br/jobs/page/'+str(id_page))
    time.sleep(3)

    x = 0
    # o codigo pega 15 vagas por pagina
    # alguns blocos de codigo, não são vagas são propagandas
    for i in range(1,16):
        print('Pagina',id_page,'de',id_last_page,': vaga',i)
        x=x+1
        try:
            # pega o nome da vaga
            # procura o nome da vaga, se for uma propaganda, vai dar um erro e vai sair do try
            name_path = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div['+str(i)+']/a/div/div[2]/div/h3')
            name = name_path.text

            # se a vaga é recente aparereca a string NOVA
            name = name.replace('\nNOVA','')
            count+=1
            time.sleep(1)

            # pegar o link da vaga
            link_path = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a')
            link = link_path.get_attribute("href")
            

            # pega as skills da  vaga
            skills = []
            for j in range(1, 10):
                try:
                    skill = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a/div/div[2]/div/div[2]/span['+str(j)+']')
                    skills.append(skill.text)
                except:
                    break
                j+=1
            #print(skills)

            # pega as informacoes  da  vaga
            infos = []
            for j in range(1,10):
                try:
                    info = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[' + str(x) + ']/a/div/div[2]/div/div[1]/span['+str(j)+']')
                    infos.append(info.text)
                except:
                    break
            #print(infos)

            # pegar a data da vaga
            driver_data.get(link)
            time.sleep(3)
            codigo_fonte = driver_data.page_source
            id_data = codigo_fonte.find('"datePosted": ')
            data = codigo_fonte[id_data+15:id_data+25]
            
            # criar um item json
            vaga = {
                link : {
                    'titulo' : name,
                    'skills' : skills,
                    'infos' : infos,
                    'data' : data
                }
            }

            # adicionar item json no arquivo vagas.json
            retorno = gravar_json.adicionar_arquivo_json(vaga)
            
            # se o retorno for TRUE então já tem a vaga cadastrada, para o programa
            if retorno == True:
                id_page = id_last_page
                break
            
        # se for uma propaganda, vai dar um erro
        # então passa para o proximo loop, e diminui o contador
        except NameError:
            print('NameError\n',NameError)
        except:
            print('Propaganda')
            i-=1

    # encerra o driver
    driver.quit()
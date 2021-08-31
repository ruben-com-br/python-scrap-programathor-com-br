from selenium import webdriver
import time

# codigo para rodar o scraping no chrome invisivel
options = webdriver.ChromeOptions()
options.add_argument("--headless")

count = 1

for id_page in range(1,100):
    # abrir chrome Driver
    pathChromeDrive = 'C:\chrome\chromedriver.exe'
    driver = webdriver.Chrome(pathChromeDrive,chrome_options=options)

    # baixar o site
    driver.get('https://programathor.com.br/jobs/page/'+str(id_page))
    time.sleep(3)

    x = 0
    # o codigo pega 15 vagas por pagina
    # alguns blocos de codigo, não são vagas são propagandas
    for i in range(1,16):
        x=x+1
        try:
            # pega o nome da vaga
            # procura o nome da vaga, se for uma propaganda, vai dar um erro e vai sair do try
            name_path = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(i)+']/a/div/div[2]/div/h3')
            name = name_path.text

            # se a vaga é recente aparereca a string NOVA
            name = name.replace('\nNOVA','')
            print(count, name)
            count+=1
            time.sleep(1)

            # pegar o link da vaga
            link_path = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a')
            link = link_path.get_attribute("href")
            print(link)


            # pega as skills da  vaga
            skills = []
            for j in range(1, 10):
                try:
                    skill = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div['+str(x)+']/a/div/div[2]/div/div[2]/span['+str(j)+']')
                    skills.append(skill.text)
                except:
                    break
                j+=1
            print(skills)

            # pega as informacoes  da  vaga
            infos = []
            for j in range(1,10):
                try:
                    info = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[' + str(x) + ']/a/div/div[2]/div/div[1]/span['+str(j)+']')
                    infos.append(info.text)
                except:
                    break
            print(infos)


        # se for uma propaganda, vai dar um erro
        # então passa para o proximo loop, e diminui o contador
        except:

            i-=1

    # encerra o driver
    driver.quit()
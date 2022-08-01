from re import template
import matplotlib.pyplot as plt
import fastf1.plotting 
from PIL import Image, ImageDraw, ImageFont
from matplotlib.transforms import Bbox   
import datetime 
import timple
from fastf1.core import Laps


def RPM(ano, rodada, sessao, nome_piloto_a, nome_piloto_b):
    
    fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\data')
    fastf1.plotting.setup_mpl()

    # FP1, FP2, FP3, Q, SQ, S, R
    # load a session and its telemetry data
    session = fastf1.get_session(ano, rodada, sessao)
    session.load()


    #Siglas piloto -> VER, PER, HAM, RUS, LEC, SAI, BOT, ZHO, NOR, RIC, ALO, OCO, MAG, MSC, LAT, ALB, VET, STR
    piloto_um = session.laps.pick_driver(nome_piloto_a).pick_fastest()
    piloto_dois = session.laps.pick_driver(nome_piloto_b).pick_fastest()

    team_a = "Equipe: " + piloto_um['Team']
    team_b = "Equipe: " + piloto_dois['Team']

    fnt_linha= ImageFont.truetype("br.com.telemetriaf1\\font\\ruda-regular.ttf", 25)

    if (team_a == team_b):
        print("tes")
        equipe_um_color = fastf1.plotting.driver_color(fastf1.plotting.DRIVER_TRANSLATE[nome_piloto_a])
        equipe_dois_color = fastf1.plotting.driver_color(fastf1.plotting.DRIVER_TRANSLATE[nome_piloto_b])

        
        d.text((20,altura), "____________________________________________" , font=fnt_linha, fill=(255,255,255))
    else:
        # Siglas -> RBR, WIL, AST, MER, MAC, APT, HAA, FER, ALP, Alpha Romeu
        equipe_um_color = fastf1.plotting.team_color(piloto_um['Team'])
        equipe_dois_color = fastf1.plotting.team_color(piloto_dois['Team'])

        

   
   

    piloto_um_tel = piloto_um.get_car_data().add_distance()
    piloto_dois_tel = piloto_dois.get_car_data().add_distance()


    

    fig, ax = plt.subplots()   
    ax.plot(piloto_um_tel['Distance'], piloto_um_tel['Speed'], color=equipe_um_color, label=nome_piloto_a)
    ax.plot(piloto_dois_tel['Distance'], piloto_dois_tel['Speed'], color=equipe_dois_color, label=nome_piloto_b)

    

    ax.set_xlabel('Distância em metros', fontsize=13)
    ax.set_ylabel('RPM', fontsize=13)
    print(session.event['EventName'])
    nome_evento = str()
    if str(session.event['EventName']) in fastf1.plotting.NOME_DO_EVENTO:
        # try short team abbreviations first
       nome_evento = fastf1.plotting.NOME_DO_EVENTO[str(session.event['EventName'])]

    nome_da_sessao = str()
    if str(session.event['EventName']) in fastf1.plotting.NOME_DO_EVENTO:
        # try short team abbreviations first
       nome_da_sessao = fastf1.plotting.SESSAO[sessao]

    print(nome_da_sessao)
    ax.legend() 
    plt.title(f"{nome_evento} {session.event.year} - {nome_da_sessao}", fontsize=28, y=1.09)   
    plt.suptitle(f"Comparação de Velocidade da Volta Mais Rápida \n ", y=0.92, fontsize=20)
    plt.savefig("figura_comp_dois_piloto", bbox_inches='tight')
    
    fig, aux = plt.subplots()
    aux.plot(piloto_um_tel['Distance'], piloto_um_tel['Speed'], color=equipe_um_color, label=nome_piloto_a)  

    img_comp_dois_piloto = Image.open('figura_comp_dois_piloto.png')
    template = Image.open('br.com.telemetriaf1\\template\\template_comp_dois_piloto.png')

    template.paste(img_comp_dois_piloto, (0,160))
    template.save("temporario_comp_dois_piloto.png")

    template = Image.open('temporario_comp_dois_piloto.png')
    d = ImageDraw.Draw(template)
    fnt = ImageFont.truetype("br.com.telemetriaf1\\font\\ruda-regular.ttf", 19)
    fnt_titulo = ImageFont.truetype("br.com.telemetriaf1\\font\\ruda-regular.ttf", 23)

    altura = 875

    d.text((20,altura), "_______________________________________" , font=fnt_linha, fill=equipe_um_color,)
    d.text((560,altura),"_______________________________________" , font=fnt_linha, fill=equipe_dois_color)
    

    if nome_piloto_a in fastf1.plotting.DRIVER_TRANSLATE:
        # try short team abbreviations first
       nome_a = "Piloto: " +  fastf1.plotting.DRIVER_TRANSLATE[nome_piloto_a]
    
    
    
    d.text((25,altura-5), nome_a , font=fnt_titulo, fill=(255,255,255))


    d.text((275,altura-5), team_a , font=fnt_titulo, fill=(255,255,255))





    tempo_a = str(piloto_um['LapTime'])
    cont = 0
    cont_if = 0
    diferenca_a_formatado = str("")
    diferenca_a_formatado

    for a in range(len(tempo_a)):
        cont = cont + 1
        if (cont > 10) & (cont < 19) :

            diferenca_a_formatado = diferenca_a_formatado + tempo_a[cont]
            cont_if = cont_if + 1

    # print(tempo_a_formatado)

    diferenca_a_formatado = "Tempo da Volta: " + str(diferenca_a_formatado)
    #
    d.text((30, altura + 40), diferenca_a_formatado , font=fnt, fill=(255,255,255))
    
    # print(piloto_um)
    
    #---------- Diferença
    diferenca = list()
    diferenca.append(piloto_um)
    diferenca.append(piloto_dois)

    diferenca = Laps(diferenca).sort_values(by='LapTime').reset_index(drop=True)

    pole_lap = diferenca.pick_fastest()

    diferenca['LapTimeDelta'] = diferenca['LapTime'] - pole_lap['LapTime']

    if (str(piloto_um[['Driver', 'LapTime']]) == str(pole_lap[['Driver', 'LapTime']])):
        diferenca_a_formatado = str("")
        # print(diferenca[['Driver', 'LapTime', 'LapTimeDelta']])
    else:
        velocidade_a = str(piloto_um['LapTime'] - pole_lap['LapTime'])
        cont = 0
        cont_if = 1
        diferenca_a_formatado = str("+")
        

        for a in range(len(velocidade_a)):
            cont = cont + 1
            if (cont > 13) & (cont < 19) :

                diferenca_a_formatado = diferenca_a_formatado + velocidade_a[cont]
                cont_if = cont_if + 1

        print(diferenca_a_formatado)

    diferenca_a_formatado = "Diferença: " + str(diferenca_a_formatado)
    
    d.text((30, altura + 70), diferenca_a_formatado , font=fnt, fill=(255,255,255))


    # print(piloto_um['SpeedST'])

    velocidade_a = str(piloto_um['SpeedST'])
    cont = 0
    cont_if = 0
    velocidade_a_formatado = str("")
    for a in range(len(velocidade_a)):
        
        if (cont < 3) :

            velocidade_a_formatado = velocidade_a_formatado + velocidade_a[cont]
            cont_if = cont_if + 1
        cont = cont + 1


    velocidade_a_formatado = "Velocidade Máx.: " + str(velocidade_a_formatado) + " Km/h"
    
    d.text((30,altura + 100), velocidade_a_formatado , font=fnt, fill=(255,255,255))


    print(piloto_um) 
    
    composto_a_formatado = "Tipo de Pneu: " + str(fastf1.plotting.COMPOSTOS[piloto_um['Compound']])
    
    d.text((30, altura + 130), composto_a_formatado , font=fnt, fill=(255,255,255))

    meteorologia = piloto_um.get_weather_data()
    print(meteorologia)

    temperatura_ambiente_a_formatado = "Temp. Ambiente: " + str(meteorologia['AirTemp']) + " °C"
    
    d.text((290,altura + 40), temperatura_ambiente_a_formatado , font=fnt, fill=(255,255,255))

    temperatura_pista_a_formatado = "Temp. da Pista: " + str(meteorologia['TrackTemp']) + " °C"
    
    d.text((290,altura + 70), temperatura_pista_a_formatado , font=fnt, fill=(255,255,255))

    vel_vento_a_formatado = "Vel. do Vento: " + str(meteorologia['WindSpeed']) + " Km/h"
    
    d.text((290,altura + 100), vel_vento_a_formatado , font=fnt, fill=(255,255,255))


    ####################################################################################
    ####################################################################################
    ####################################################################################
    ####################################################################################
    # Piloto B

    if nome_piloto_b in fastf1.plotting.DRIVER_TRANSLATE:
        # try short team abbreviations first
       nome_b = "Piloto: " +  fastf1.plotting.DRIVER_TRANSLATE[nome_piloto_b]
    
    altura = 875
    
    d.text((565,altura-5), nome_b , font=fnt_titulo, fill=(255,255,255))


    d.text((815,altura-5), team_b , font=fnt_titulo, fill=(255,255,255))


    





    tempo_b = str(piloto_dois['LapTime'])
    cont = 0
    cont_if = 0
    diferenca_b_formatado = str("")
    

    for a in range(len(tempo_b)):
        cont = cont + 1
        if (cont > 10) & (cont < 19) :

            diferenca_b_formatado = diferenca_b_formatado + tempo_b[cont]
            cont_if = cont_if + 1

    # print(tempo_a_formatado)

    diferenca_b_formatado = "Tempo da Volta: " + str(diferenca_b_formatado)
    #
    d.text((570, altura + 40), diferenca_b_formatado , font=fnt, fill=(255,255,255))
    
    # print(piloto_um)
    
    #---------- Diferença
    diferenca = list()
    diferenca.append(piloto_um)
    diferenca.append(piloto_dois)

    diferenca = Laps(diferenca).sort_values(by='LapTime').reset_index(drop=True)

    pole_lap = diferenca.pick_fastest()

    diferenca['LapTimeDelta'] = diferenca['LapTime'] - pole_lap['LapTime']

    if (str(piloto_dois[['Driver', 'LapTime']]) == str(pole_lap[['Driver', 'LapTime']])):
        diferenca_a_formatado = str("")
        # print(diferenca[['Driver', 'LapTime', 'LapTimeDelta']])
    else:
        velocidade_a = str(piloto_dois['LapTime'] - pole_lap['LapTime'])
        cont = 0
        cont_if = 1
        diferenca_a_formatado = str("+")
        

        for a in range(len(velocidade_a)):
            cont = cont + 1
            if (cont > 13) & (cont < 19) :

                diferenca_a_formatado = diferenca_a_formatado + velocidade_a[cont]
                cont_if = cont_if + 1

        print(diferenca_a_formatado)

    diferenca_a_formatado = "Diferença: " + str(diferenca_a_formatado)
    
    d.text((570, altura + 70), diferenca_a_formatado , font=fnt, fill=(255,255,255))


    # print(piloto_dois['SpeedST'])

    velocidade_a = str(piloto_dois['SpeedST'])
    cont = 0
    cont_if = 0
    velocidade_a_formatado = str("")
    for a in range(len(velocidade_a)):
        
        if (cont < 3) :

            velocidade_a_formatado = velocidade_a_formatado + velocidade_a[cont]
            cont_if = cont_if + 1
        cont = cont + 1


    velocidade_a_formatado = "Velocidade Máx.: " + str(velocidade_a_formatado) + " Km/h"
    
    d.text((570,altura + 100), velocidade_a_formatado , font=fnt, fill=(255,255,255))


    print(piloto_dois) 
    
    composto_a_formatado = "Tipo de Pneu: " + str(fastf1.plotting.COMPOSTOS[piloto_dois['Compound']])
    
    d.text((570, altura + 130), composto_a_formatado , font=fnt, fill=(255,255,255))

    meteorologia = piloto_dois.get_weather_data()
    print(meteorologia)

    temperatura_ambiente_a_formatado = "Temp. Ambiente: " + str(meteorologia['AirTemp']) + " °C"
    
    d.text((830,altura + 40), temperatura_ambiente_a_formatado , font=fnt, fill=(255,255,255))

    temperatura_pista_a_formatado = "Temp. da Pista: " + str(meteorologia['TrackTemp']) + " °C"
    
    d.text((830,altura + 70), temperatura_pista_a_formatado , font=fnt, fill=(255,255,255))

    vel_vento_a_formatado = "Vel. do Vento: " + str(meteorologia['WindSpeed']) + " Km/h"
    
    d.text((830,altura + 100), vel_vento_a_formatado , font=fnt, fill=(255,255,255))

    

    template.show()
    template.save("comp_dois_piloto.png")

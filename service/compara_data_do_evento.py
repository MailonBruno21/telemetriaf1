from re import template
import matplotlib.pyplot as plt
import fastf1.plotting 
from PIL import Image, ImageDraw, ImageFont
from matplotlib.transforms import Bbox   
import datetime
import timple
from fastf1.core import Laps

def compara_data_evento():
    fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\data')
    fastf1.plotting.setup_mpl()

    data_atual = datetime.datetime.now()

    ano = data_atual.year
    mes = data_atual.month
    dia = data_atual.day

    print(ano, mes, dia)

    week = fastf1.get_event_schedule(ano)
    # print(week.get_event_by_round(11))
    # print(week)


    data_tl_um = week['Session1Date']
    numero_da_rodada = str(week['RoundNumber'])

    
    cont = 0
    cont_if = 0
    
    ano_rodada = str("")
    mes_rodada = str("")
    
    dia_rodada = str("")
    

    for a in data_tl_um:
        aux = str(a)
        print(ano_rodada)
        
        for b in range(len(str(a))):
            if (cont < 4) :
                ano_rodada = ano_rodada + aux[cont]
                cont_if = cont_if + 1

            if (cont > 4 & cont < 7) :
                mes_rodada = mes_rodada + aux[cont]
                cont_if = cont_if + 1
            cont = cont + 1


   
    print(ano_rodada)

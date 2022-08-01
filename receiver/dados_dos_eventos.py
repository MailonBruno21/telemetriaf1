
from timple.timedelta import strftimedelta
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import fastf1
from fastf1.core import Laps
from fastf1 import utils
from fastf1 import plotting




ano = 2022

plotting.setup_mpl()
fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\data')

week = fastf1.get_event_schedule(ano)



round = 1
# t = teste['RoundNumber']

print(week)

print(week['EventName'])





# while(session.index.max):
#         teste = session.get_event_by_round(round)
        
           
#         if(session.index.max < round):
#                 break
        
#         round = round + 1
#         print(teste)



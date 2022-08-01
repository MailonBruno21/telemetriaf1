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
plotting.setup_mpl()


fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\data')

year = 2022
wknd = 12
ses = 'Q'
driver = 'VER'
# colormap = mpl.cm.plasma


session = fastf1.get_session(year, wknd, ses)
weekend = session.event
session.load()

# lap = session.laps.pick_drivers([driver, 'SAI'])

# print(lap[['LapTime', 'Driver', 'LapNumber']])


laps = session.laps

# print(laps)

#METODOS
# meteorologia = laps.get_weather_data()
# print(meteorologia)

# voltas_do_piloto = laps.pick_driver('LEC')
# print(voltas_do_piloto)

# voltas_dos_pilotos = laps.pick_drivers(['LEC', 'VER'])
# print(voltas_dos_pilotos)

# voltas_do_time = laps.pick_team('Mercedes')
# print(voltas_do_time)

# voltas_dos_times = laps.pick_teams(['Mercedes', 'Red Bull'])
# print(voltas_dos_times)

# volta_mais_rapida = voltas_do_time.pick_fastest()
# print(volta_mais_rapida)


piloto_um = session.laps.pick_driver('LEC').pick_fastest()
pilot_dois = session.laps.pick_driver('VER')

print(piloto_um)

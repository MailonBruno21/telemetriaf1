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


fastf1.Cache.enable_cache('br.com.telemetriaf1.dados')


# Carrega a seção passando o ano, cidade
session = fastf1.get_session(2022, 'France', 'FP2')
session.load()

# fastf1.api.timing_data ( caminho , resposta = Nenhum , livedata = Nenhum )
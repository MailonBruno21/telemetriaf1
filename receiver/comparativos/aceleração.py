import matplotlib.pyplot as plt
import fastf1.plotting

fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\dados')
fastf1.plotting.setup_mpl()

# load a session and its telemetry data
session = fastf1.get_session(2022, 12, 'FP3')
session.load()

driver_um = 'LEC'
driver_dois = 'VER'


#Siglas piloto -> VER, PER, HAM, RUS, LEC, SAI, BOT, ZHO, NOR, RIC, ALO, OCO, MAG, MSC, LAT, ALB, VET, STR
piloto_um = session.laps.pick_driver(driver_um).pick_fastest()
pilot_dois = session.laps.pick_driver(driver_dois).pick_fastest()

piloto_um_tel = piloto_um.get_car_data().add_distance()
piloto_dois_tel = pilot_dois.get_car_data().add_distance()


# Siglas -> RBR, WIL, AST, MER, MAC, APT, HAA, FER, ALP, Alpha Romeu
equipe_um_color = fastf1.plotting.team_color('FER')
equipe_dois_color = fastf1.plotting.team_color('RBR')

fig, ax = plt.subplots()
ax.plot(piloto_um_tel['Distance'], piloto_um_tel['Throttle'], color=equipe_um_color, label=driver_um)
ax.plot(piloto_dois_tel['Distance'], piloto_dois_tel['Throttle'], color=equipe_dois_color, label=driver_dois)

ax.set_xlabel('Distancia em metros')
ax.set_ylabel('Aceleração em %')

ax.legend()
plt.suptitle(f"Comparação da Volta Mais Rápida \n "
             f"{session.event['EventName']} {session.event.year} Treino Livre 1")

plt.show()
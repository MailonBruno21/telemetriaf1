import matplotlib.pyplot as plt
import fastf1.plotting

fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\dados')
fastf1.plotting.setup_mpl()

# load a session and its telemetry data
session = fastf1.get_session(2022, 12, 'FP2')
session.load()


#Siglas piloto -> VER, PER, HAM, RUS, LEC, SAI, BOT, ZHO, NOR, RIC, ALO, OCO, MAG, MSC, LAT, ALB, VET, STR
piloto_um = session.laps.pick_driver('VET').pick_fastest()
pilot_dois = session.laps.pick_driver('STR').pick_fastest()

piloto_um_tel = piloto_um.get_car_data().add_distance()
piloto_dois_tel = pilot_dois.get_car_data().add_distance()


# Siglas -> RBR, WIL, AST, MER, MAC, APT, HAA, FER, ALP, Alpha Romeu
equipe_um_color = fastf1.plotting.team_color('Alpha Romeu')
equipe_dois_color = fastf1.plotting.team_color('ALP')

fig, ax = plt.subplots()
ax.plot(piloto_um_tel['Distance'], piloto_um_tel['nGear'], color=equipe_um_color, label='PILOTO UM')
ax.plot(piloto_dois_tel['Distance'], piloto_dois_tel['nGear'], color=equipe_dois_color, label='PILOTO DOIS')

ax.set_xlabel('Distancia em metros')
ax.set_ylabel('Marchas')

ax.legend()
plt.suptitle(f"Comparação da Volta Mais Rápida \n "
             f"{session.event['EventName']} {session.event.year} Treino Livre 1")

plt.show()
import fastf1
from fastf1.livetiming.data import LiveTimingData

fastf1.Cache.enable_cache('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\dados', force_renew=True)

livedata = LiveTimingData('C:\\Users\\pedri\\OneDrive\\Área de Trabalho\\Projeto\\TelemetriaFormulaUm\\br.com.telemetriaf1\\dados.dados_ao_vivo.txt')
session = fastf1.get_session(2022, 'Franch', 'Q')


session.load(livedata=livedata)
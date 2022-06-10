from cmath import nan
import numpy as np
import pandas as pd
import math
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.layouts import row , gridplot
import csv
b = math.nan


year2018df = pd.read_csv('2018.csv', sep = ';')
year2018df['Tiempo'] = pd.to_datetime(year2018df['Tiempo'])
#year2018df['DiaAño'] = year2018df['Tiempo'].dt.strftime('%m-%d-%H')

#print(year2018df)


#year2018df.info()


year2019df = pd.read_csv('2019.csv', sep = ';')
year2019df['Tiempo'] = pd.to_datetime(year2019df['Tiempo'])
#year2019df.info()


year2021df = pd.read_csv('2021.csv', sep = ';')
year2021df['Tiempo'] = pd.to_datetime(year2021df['Tiempo'])

#year2020df.info()

#print(year2018df)



a = year2018df['Carvajal_Sevillana_CO_pmm'].fillna((year2019df['Carvajal_Sevillana_CO_pmm']+year2021df['Carvajal_Sevillana_CO_pmm'])/2)
b = year2019df['Carvajal_Sevillana_CO_pmm'].fillna((year2018df['Carvajal_Sevillana_CO_pmm']+year2021df['Carvajal_Sevillana_CO_pmm'])/2)
c = year2021df['Carvajal_Sevillana_CO_pmm'].fillna((year2018df['Carvajal_Sevillana_CO_pmm']+year2019df['Carvajal_Sevillana_CO_pmm'])/2)

a.to_csv('carbajal2018.csv')
b.to_csv('carbajal2019.csv')
c.to_csv('carbajal2021.csv')



year2018df['Carvajal_Sevillana_CO_pmm'].to_csv('data1.csv')

weekly_data = year2018df.resample('W-Wed', label='right', closed = 'right', on='Tiempo').sum().reset_index().sort_values(by='Tiempo')


xYear2018 = a.tolist()
xYear2019 = b.tolist()
xYear2021 = c.tolist()

y = []
n = 0
for i in xYear2018:
    y.append(n)
    n += 1


pYear2018 = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018.line(y,xYear2018, legend_label="Temp.", line_width=2)

pYear2019 = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019.line(y,xYear2019, legend_label="Temp.", line_width=2)

pYear2021 = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021.line(y,xYear2021, legend_label="Temp.", line_width=2)




a = year2018df['Centro_de_Alto_Rendimiento_CO_pmm'].fillna((year2019df['Centro_de_Alto_Rendimiento_CO_pmm']+year2021df['Centro_de_Alto_Rendimiento_CO_pmm'])/2)
b = year2019df['Centro_de_Alto_Rendimiento_CO_pmm'].fillna((year2018df['Centro_de_Alto_Rendimiento_CO_pmm']+year2021df['Centro_de_Alto_Rendimiento_CO_pmm'])/2)
c = year2021df['Centro_de_Alto_Rendimiento_CO_pmm'].fillna((year2018df['Centro_de_Alto_Rendimiento_CO_pmm']+year2019df['Centro_de_Alto_Rendimiento_CO_pmm'])/2)


#Year2018Centrodf['Centro_de_Alto_Rendimiento_CO_pmm'].to_csv('data1.csv')

#weekly_data = Year2018Centrodf.resample('W-Wed', label='right', closed = 'right', on='Tiempo').sum().reset_index().sort_values(by='Tiempo')
a.to_csv('altoRendimiento2018.csv')
b.to_csv('altoRendimiento2019.csv')
c.to_csv('altoRendimiento2021.csv')

xYear2018Centro = a.tolist()
xYear2019Centro = b.tolist()
xYear2021Centro = c.tolist()

pYear2018Centro = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Centro.line(y,xYear2018Centro, legend_label="Temp.", line_width=2)

pYear2019Centro = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Centro.line(y,xYear2019Centro, legend_label="Temp.", line_width=2)

pYear2021Centro = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Centro.line(y,xYear2021Centro, legend_label="Temp.", line_width=2)


bd=year2018df.groupby(year2018df.Tiempo.dt.week)['Centro_de_Alto_Rendimiento_CO_pmm'].mean()
bd1=year2018df.groupby(year2018df.Tiempo.dt.week)['Centro_de_Alto_Rendimiento_CO_pmm'].mean()



a = year2018df['Kennedy_CO_pmm'].fillna((year2019df['Kennedy_CO_pmm']+year2021df['Kennedy_CO_pmm'])/2)
b = year2019df['Kennedy_CO_pmm'].fillna((year2018df['Kennedy_CO_pmm']+year2021df['Kennedy_CO_pmm'])/2)
c = year2021df['Kennedy_CO_pmm'].fillna((year2018df['Kennedy_CO_pmm']+year2019df['Kennedy_CO_pmm'])/2)

a.to_csv('kennedy2018.csv')
b.to_csv('kennedy2019.csv')
c.to_csv('kennedy2021.csv')


xYear2018Kennedy = a.tolist()
xYear2019Kennedy = b.tolist()
xYear2021Kennedy = c.tolist()




pYear2018Kennedy = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Kennedy.line(y,xYear2018Kennedy, legend_label="Temp.", line_width=2)

pYear2019Kennedy = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Kennedy.line(y,xYear2019Kennedy, legend_label="Temp.", line_width=2)

pYear2021Kennedy = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Kennedy.line(y,xYear2021Kennedy, legend_label="Temp.", line_width=2)








a = year2018df['Las_Ferias_CO_pmm'].fillna((year2019df['Las_Ferias_CO_pmm']+year2021df['Las_Ferias_CO_pmm'])/2)
b = year2019df['Las_Ferias_CO_pmm'].fillna((year2018df['Las_Ferias_CO_pmm']+year2021df['Las_Ferias_CO_pmm'])/2)
c = year2021df['Las_Ferias_CO_pmm'].fillna((year2018df['Las_Ferias_CO_pmm']+year2019df['Las_Ferias_CO_pmm'])/2)

a.to_csv('ferias2018.csv')
b.to_csv('ferias2019.csv')
c.to_csv('ferias2021.csv')

xYear2018Las_Ferias = a.tolist()
xYear2019Las_Ferias = b.tolist()
xYear2021Las_Ferias = c.tolist()

pYear2018Las_Ferias = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Las_Ferias.line(y,xYear2018Las_Ferias, legend_label="Temp.", line_width=2)

pYear2019Las_Ferias = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Las_Ferias.line(y,xYear2019Las_Ferias, legend_label="Temp.", line_width=2)

pYear2021Las_Ferias = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Las_Ferias.line(y,xYear2021Las_Ferias, legend_label="Temp.", line_width=2)





a = year2018df['Puente_Aranda_CO_pmm'].fillna((year2019df['Puente_Aranda_CO_pmm']+year2021df['Puente_Aranda_CO_pmm'])/2)
b = year2019df['Puente_Aranda_CO_pmm'].fillna((year2018df['Puente_Aranda_CO_pmm']+year2021df['Puente_Aranda_CO_pmm'])/2)
c = year2021df['Puente_Aranda_CO_pmm'].fillna((year2018df['Puente_Aranda_CO_pmm']+year2019df['Puente_Aranda_CO_pmm'])/2)

a.to_csv('puente2018.csv')
b.to_csv('puente2019.csv')
c.to_csv('puente2021.csv')


xYear2018Puente_Aranda = a.tolist()
xYear2019Puente_Aranda = b.tolist()
xYear2021Puente_Aranda = c.tolist()

pYear2018Puente_Aranda = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Puente_Aranda.line(y,xYear2018Puente_Aranda, legend_label="Temp.", line_width=2)

pYear2019Puente_Aranda = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Puente_Aranda.line(y,xYear2019Puente_Aranda, legend_label="Temp.", line_width=2)

pYear2021Puente_Aranda = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Puente_Aranda.line(y,xYear2021Puente_Aranda, legend_label="Temp.", line_width=2)




a = year2018df['Tunal_CO_pmm'].fillna((year2019df['Tunal_CO_pmm']+year2021df['Tunal_CO_pmm'])/2)
b = year2019df['Tunal_CO_pmm'].fillna((year2018df['Tunal_CO_pmm']+year2021df['Tunal_CO_pmm'])/2)
c = year2021df['Tunal_CO_pmm'].fillna((year2018df['Tunal_CO_pmm']+year2019df['Tunal_CO_pmm'])/2)

a.to_csv('tunal2018.csv')
b.to_csv('tunal2019.csv')
c.to_csv('tunal2021.csv')


xYear2018Tunal = a.tolist()
xYear2019Tunal = b.tolist()
xYear2021Tunal = c.tolist()



pYear2018Tunal = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Tunal.line(y,xYear2018Tunal, legend_label="Temp.", line_width=2)

pYear2019Tunal = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Tunal.line(y,xYear2019Tunal, legend_label="Temp.", line_width=2)

pYear2021Tunal = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Tunal.line(y,xYear2021Tunal, legend_label="Temp.", line_width=2)





a = year2018df['Usaquen_CO_pmm'].fillna((year2019df['Usaquen_CO_pmm']+year2021df['Usaquen_CO_pmm'])/2)
b = year2019df['Usaquen_CO_pmm'].fillna((year2018df['Usaquen_CO_pmm']+year2021df['Usaquen_CO_pmm'])/2)
c = year2021df['Usaquen_CO_pmm'].fillna((year2018df['Usaquen_CO_pmm']+year2019df['Usaquen_CO_pmm'])/2)

a.to_csv('usaquen2018.csv')
b.to_csv('usaquen2019.csv')
c.to_csv('usaquen2021.csv')

xYear2018Usaquen = a.tolist()
xYear2019Usaquen = b.tolist()
xYear2021Usaquen = c.tolist()





bd1=year2018df.groupby(year2018df.Tiempo.dt.week)['Carvajal_Sevillana_CO_pmm'].mean().to_frame()
bd2=year2019df.groupby(year2019df.Tiempo.dt.week)['Carvajal_Sevillana_CO_pmm'].mean().to_frame()
bd3=year2021df.groupby(year2021df.Tiempo.dt.week)['Carvajal_Sevillana_CO_pmm'].mean().to_frame()


bd4=year2018df.groupby(year2018df.Tiempo.dt.week)['Centro_de_Alto_Rendimiento_CO_pmm'].mean().to_frame()
bd5=year2019df.groupby(year2019df.Tiempo.dt.week)['Centro_de_Alto_Rendimiento_CO_pmm'].mean().to_frame()
bd6=year2021df.groupby(year2021df.Tiempo.dt.week)['Centro_de_Alto_Rendimiento_CO_pmm'].mean().to_frame()



bd7=year2018df.groupby(year2018df.Tiempo.dt.week)['Kennedy_CO_pmm'].mean().to_frame()
bd8=year2019df.groupby(year2019df.Tiempo.dt.week)['Kennedy_CO_pmm'].mean().to_frame()
bd9=year2021df.groupby(year2021df.Tiempo.dt.week)['Kennedy_CO_pmm'].mean().to_frame()


be1=year2018df.groupby(year2018df.Tiempo.dt.week)['Las_Ferias_CO_pmm'].mean().to_frame()
be2=year2019df.groupby(year2019df.Tiempo.dt.week)['Las_Ferias_CO_pmm'].mean().to_frame()
be3=year2021df.groupby(year2021df.Tiempo.dt.week)['Las_Ferias_CO_pmm'].mean().to_frame()


be4=year2018df.groupby(year2018df.Tiempo.dt.week)['Puente_Aranda_CO_pmm'].mean().to_frame()
be5=year2019df.groupby(year2019df.Tiempo.dt.week)['Puente_Aranda_CO_pmm'].mean().to_frame()
be6=year2021df.groupby(year2021df.Tiempo.dt.week)['Puente_Aranda_CO_pmm'].mean().to_frame()


be7=year2018df.groupby(year2018df.Tiempo.dt.week)['Tunal_CO_pmm'].mean().to_frame()
be8=year2019df.groupby(year2019df.Tiempo.dt.week)['Tunal_CO_pmm'].mean().to_frame()
be9=year2021df.groupby(year2021df.Tiempo.dt.week)['Tunal_CO_pmm'].mean().to_frame()

bf1=year2018df.groupby(year2018df.Tiempo.dt.week)['Usaquen_CO_pmm'].mean().to_frame()
bf2=year2019df.groupby(year2019df.Tiempo.dt.week)['Usaquen_CO_pmm'].mean().to_frame()
bf3=year2021df.groupby(year2021df.Tiempo.dt.week)['Usaquen_CO_pmm'].mean().to_frame()

result = pd.concat([bd1,bd2,bd3,bd4,bd5,bd6,bd7,bd8,bd9,be1,be2,be3,be4,be5,be6,be7,be8,be9,bf1,bf2,bf3], axis=1, join="inner")

result.to_csv("resultados.csv")

print(result)
bd2.to_csv('usaquenSem2021.csv')




pYear2018Usaquen = figure(title="2018", x_axis_label='x', y_axis_label='y')

pYear2018Usaquen.line(y,xYear2018Usaquen, legend_label="Temp.", line_width=2)

pYear2019Usaquen = figure(title="2019", x_axis_label='x', y_axis_label='y')

pYear2019Usaquen.line(y,xYear2019Usaquen, legend_label="Temp.", line_width=2)

pYear2021Usaquen = figure(title="2021", x_axis_label='x', y_axis_label='y')

pYear2021Usaquen.line(y,xYear2021Usaquen, legend_label="Temp.", line_width=2)


grid = gridplot([[pYear2018,pYear2019, pYear2021]
,[pYear2018Centro,pYear2019Centro, pYear2021Centro]
,[pYear2018Kennedy,pYear2019Kennedy, pYear2021Kennedy]
,[pYear2018Las_Ferias,pYear2019Las_Ferias, pYear2021Las_Ferias]
,[pYear2018Puente_Aranda, pYear2019Puente_Aranda, pYear2021Puente_Aranda]
,[pYear2018Tunal,pYear2019Tunal,pYear2021Tunal]
,[pYear2018Usaquen,pYear2019Usaquen,pYear2021Usaquen]], width=350, height=350)

show(grid)

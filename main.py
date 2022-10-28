# html data downloading
import pandas as pd

simpsons = pd.read_html ('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print(len(simpsons))
print(simpsons[1])

#------------------------------------------------------
# Download csv file

df_premier21=pd.read_csv('https://football-data.co.uk/mmz4281/2223/E0.csv')
df_premier21.rename(columns={'FTHG':'Home_underscore_goals','FTAG':'away_goals'}, inplace=True)
df_premier21.to_csv('premier.csv')
print(df_premier21)

#--------------------------------------------------------
#Extract information from pdf
import camelot

#tables = camelot.read_pdf('foo.pdf',pages='1')
#print(tables)

#---------------------------------------------------------
#Read Excel
#df = pd.read_excel('supermarket_sales.xlsx')
#df = df[['Gender','Product line', 'Total']]
#print(df)

#pivot_table = df.pivot_table(index='Gender', columns= 'Product line', values='Total', aggfunc='sum').round(0)
#pivot_table.to_excel('pivot_table.xlsx','Report', startrow=4)

#-----------------------------------------------------------------------------------------------------
# Whatsapp automation
import pywhatkit

pywhatkit.sendwhatmsg("+34 635 52 47 65","EL PODER , LA MALDAD , KOGI PUEDE CONTROLAR!!! enviado por python robot",20,28,15,True,5)

#-----------------------------------------------------------------------------------------------------

# Whatsapp group


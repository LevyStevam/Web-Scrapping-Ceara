import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://fbref.com/en/squads/2f335e17/Ceara-Stats')


html_pagina = BeautifulSoup(response.content, 'html.parser')
html_tabela = html_pagina.find('table', attrs={'id': 'matchlogs_for'})


tbody_html = html_tabela.find('tbody')
data_html = html_tabela.findAll('tr')
# print(tbody_html.prettify())
data_list = []
for tr in data_html:
    rows = []
    for data in tr.findAll(['th','td']):
        rows.append(data.text)
    data_list.append(rows)
# print(data_list)
matches_df = pd.DataFrame(data_list)
matches_df.columns = matches_df.iloc[0]
matches_df = matches_df[1:]
matches_df.drop('Match Report',axis= 1, inplace= True)
matches_df.drop('Notes', axis=1, inplace=True)
matches_df.drop('Round', axis=1, inplace=True)
matches_df.drop('Comp', axis=1, inplace=True)
# print(matches_df)
matches_df.to_excel('Partidas Ceará.xlsx', index=False)




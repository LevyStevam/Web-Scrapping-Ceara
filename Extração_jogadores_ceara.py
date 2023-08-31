import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get('https://fbref.com/en/squads/2f335e17/Ceara-Stats')
data = BeautifulSoup(response.content, 'html.parser')
tabela = data.find('table', attrs={'class', 'stats_table'} )
# print(data.prettify())
header = ['Player', 'Nation', 'Pos', 'Age', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 'G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'Gls', 'Ast', 'G+A', 'G-PK', 'G+A-PK', 'Matches']
players_table_html = tabela.find('tbody')
# print(players_table.prettify())
players_list = []
for player in players_table_html.find_all('tr'):
    row = []
    for stats in player.find_all('td'):
        row.append(stats.text)
    players_list.append(row)
print(players_list)

players_table = pd.DataFrame(players_list, columns=["Nation", "Pos", "Age", "MP", "Starts", "Min", "90s", "Gls", "Ast", "G+A", "G-PK", "PK", "PKatt", "CrdY", "CrdR", "Gls", "Ast", "G+A", "G-PK", "G+A-PK", "Matches"])


names = ["Erick", "Willian Maranhão", "Richardson", "Chayene Santos", "Jean Carlos Vicente", "Warley", "Tiago Pagnussat", "Bruno Ferreira", "Luiz Otávio", "Caíque de Jesus Gonçalves", "David Loiola", "Richard", "Nicolas", "Gabriel Lacerda", "Danilo Barcelos", "Janderson", "Zé Ricardo", "Vitor Gabriel", "Willian Formiga", "Guilherme Bissoli", "Guilherme Carvalho", "Paulo Victor ", "Breno", "Léo Santos", "Arthur", "Paulo Victor", "Saulo da Silva", "Hygor", "Erick Pulga", "Michel ", "Chrystian Barletta ", "Sidnei ", "André Luiz ", "Alvaro ", "Henrique Luvannor ", "Cléber ", "Pedrinho ", "Jonathan ", "Pedro Lucas ", "Alfredo Aguilar ", "Cristian ", "Luis Manuel Orejuela ", "Léo Rafael",'João Victor']
nomes = pd.Series(names)
players_table.insert(0, 'Names', nomes)
players_table.to_excel('Data Frame Player.xlsx', index=False)


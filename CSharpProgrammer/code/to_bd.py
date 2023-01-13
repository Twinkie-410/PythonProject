import sqlite3
import pandas as pd

df = pd.read_csv('data/statistic_by_year_CSharp.csv')
connection = sqlite3.connect('../../db.sqlite3')
cursor = connection.cursor()

df.index.rename('id', inplace=True)
df.columns = ['year', 'middle_salary', 'count_vacancy', 'middle_salary_profession', 'count_vacancy_profession']
df.to_sql(name='CSharpProgrammer_statisticyear', con=connection, if_exists='replace')

df = pd.read_csv('data/top_city_salary.csv')
df.index.rename('id', inplace=True)
df.columns = ['city', 'salary']
df.to_sql(name='CSharpProgrammer_statistictopsalarycity', con=connection, if_exists='replace')

df = pd.read_csv('data/top_city_count.csv')
df.index.rename('id', inplace=True)
df.columns = ['city', 'count']
df.to_sql(name='CSharpProgrammer_statistictopcountcity', con=connection, if_exists='replace')

df = pd.read_csv('data/top_skills_by_year.csv')
df.index.rename('id', inplace=True)
df.columns = ['year', 'skill', 'count']
df.to_sql(name='CSharpProgrammer_topskills', con=connection, if_exists='replace')

connection.commit()


import re
import matplotlib.pyplot as plt
from matplotlib.ticker import IndexLocator
import pandas as pd


def generate_images():
    vacancy_statistic = pd.read_csv('data/statistic_by_year_CSharp.csv')
    salary_city = pd.read_csv('data/top_city_salary.csv')
    count_city = pd.read_csv('data/top_city_count.csv')

    create_salary_image(vacancy_statistic)
    create_count_image(vacancy_statistic)
    create_top_salary_city_image(salary_city)
    create_vacancy_ratio_image(count_city)


def create_salary_image(df):
    fig, ax = plt.subplots()
    ax.set_title("Уровень зарплат по годам")
    w = 0.4
    ax.bar([val - w / 2 for val in range(len(df.iloc[:, 0]))], df.iloc[:, 1], width=w, label="средняя з/п")
    ax.bar([val + w / 2 for val in range(len(df.iloc[:, 0]))], df.iloc[:, 3], width=w, label="з/п C# Программист")
    ax.set_xticks(range(len(df.iloc[:, 0])), df.iloc[:, 0], rotation="vertical")
    ax.legend()
    ax.yaxis.set_major_locator(IndexLocator(base=20000, offset=0))
    plt.tight_layout()
    plt.savefig("../static/CSharpProgrammer/images/salary_by_year.png")
    plt.show()


def create_count_image(df):
    fig, ax = plt.subplots()
    ax.set_title("Количество ваканский по годам")
    w = 0.4
    ax.bar([val - w / 2 for val in range(len(df.iloc[:, 2]))], df.iloc[:, 2], width=w, label="Количество ваканксий")
    ax.bar([val + w / 2 for val in range(len(df.iloc[:, 4]))], df.iloc[:, 4], width=w,
           label="Количество ваканксий\nC# Программист")
    ax.set_xticks(range(len(df.iloc[:, 0])), df.iloc[:, 0], rotation="vertical")
    # ax.tick_params(axis="both", labelsize=8)
    ax.legend(loc='upper left')
    ax.yaxis.set_major_locator(IndexLocator(base=40000, offset=0))
    plt.tight_layout()
    plt.savefig("../static/CSharpProgrammer/images/count_by_year.png")
    plt.show()


def create_top_salary_city_image(df):
    fig, ax = plt.subplots()
    ax.set_title("Уровень зарплат по городам")
    y_pos = range(len(df.iloc[:, 0]))
    cities = [re.sub(r"[- ]", "\n", c) for c in df.iloc[:, 0]]
    ax.barh(y_pos, df.iloc[:, 1])
    ax.set_yticks(y_pos, cities)
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("../static/CSharpProgrammer/images/city_top_salary.png")
    plt.show()


def create_vacancy_ratio_image(df):
    df.loc[len(df.index)] = ['Другие', round(1 - df.iloc[:, 1].sum(), 4)]
    df = df.sort_values(by=['Доля вакансий'], ascending=False)
    fig, ax = plt.subplots()
    ax.set_title("Доля вакансий по городам")
    ax.pie(df.iloc[:, 1], labels=df.iloc[:, 0])
    plt.savefig("../static/CSharpProgrammer/images/city_top_count.png")
    plt.show()


generate_images()

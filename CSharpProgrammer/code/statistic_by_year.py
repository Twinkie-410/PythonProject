import pandas as pd

pd.set_option("display.max_columns", False)
pd.set_option("expand_frame_repr", False)


def get_dataframe(file, vacancy):
    """
    Создает датафрейм со статистикой по годам.
    :param file: Файл с вакансиями
    :param vacancy: Название вакансии
    :return: DataFrame
    датафрейм со статистикой по годам
    """
    vacancies = pd.read_csv(file)
    vacancies = vacancies[vacancies['salary'].notna()]
    vacancies['Год'] = vacancies['published_at'].str[:4]
    vacancies_salary = round(vacancies[['Год', 'salary']].groupby('Год').mean())
    vacancies_count = vacancies.groupby('Год')['name'].count()
    sharp_vacancy = vacancies.query('name.str.lower().str.contains("c#".lower()) or '
                                    'name.str.lower().str.contains("c sharp".lower()) or '
                                    'name.str.lower().str.contains("шарп".lower())')
    vacancy_salary = round(sharp_vacancy[['Год', 'salary']].groupby('Год').mean())
    vacancy_count = sharp_vacancy.groupby('Год')['name'].count()
    statistic_vacancies = pd.merge(vacancies_salary, vacancies_count, how='left', on='Год')
    statistic_vacancies.rename(columns={'salary': 'Средняя зарплата', 'name': 'Количество вакансий'}, inplace=True)

    # statistic_vacancies.rename(columns={'Год': 'year', 'salary': 'middle_salary', 'name': 'count_vacancy'}, inplace=True)

    statistic_vacancy = pd.merge(vacancy_salary, vacancy_count, how='left', on='Год')
    statistic_vacancy.rename(columns={'salary': f'Средняя зарплата - {vacancy}',
                                      'name': f'Количество вакансий - {vacancy}'}, inplace=True)

    # statistic_vacancy.rename(columns={'salary': 'middle_salary_profession',
    #                                   'name': 'count_vacancy_profession'}, inplace=True)

    statistic = pd.merge(statistic_vacancies, statistic_vacancy, how='left', on='Год').fillna(0).astype(int) \
        .reset_index(level=0)
    return statistic


# def get_pdf(dataframe):
#     """
#     Создает html-страницу с датафреймом и конвертирует ее в пдф.
#     :param dataframe: Датафрейм со статистикой
#     """
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('statisticPandas.html')
#     pdf_template = template.render({'table': dataframe.to_html(index=False)})
#     config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
#     pdfkit.from_string(pdf_template, 'statisticPandas.pdf',
#                        configuration=config, options={"enable-local-file-access": ""})


if __name__ == '__main__':
    file_path = "data/vacancies_with_skills_middle_salary.csv"
    vacancy = "C# Программист"
    statistic = get_dataframe(file_path, vacancy)
    statistic.to_csv('../static/CSharpProgrammer/data/statistic_by_year_CSharp.csv', index=False)

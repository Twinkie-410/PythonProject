import pandas as pd


def get_dataframes(file, vacancy):
    """
    :param file: Файл с вакансиями
    :param vacancy: Название вакансии
    :return: датафреймы со статистикой по городам, по годам для определенной вакансии и региона
    """
    vacancies = pd.read_csv(file)
    vacancies = vacancies.dropna()
    # vacancies = vacancies.query('name.str.lower().str.contains("c#".lower()) or '
    #                             'name.str.lower().str.contains("c sharp".lower()) or '
    #                             'name.str.lower().str.contains("шарп".lower())')
    vacancies_salary_city = round(vacancies[['area_name', 'salary']].groupby('area_name').mean())
    vacancies_count_city = vacancies.groupby('area_name')['name'].count()

    vacancies_city = pd.merge(vacancies_salary_city, vacancies_count_city, how='left', on='area_name')
    vacancies_sum = len(vacancies)
    vacancies_city["name"] = round(vacancies_city["name"] / vacancies_sum, 4)
    vacancies_city = vacancies_city[vacancies_city['name'] >= 0.01]

    vacancies_salary_city_top = vacancies_city.reset_index(level=0)[['area_name', 'salary']].sort_values('salary',
                                                                                                         ascending=0).head(
        10)
    vacancies_salary_city_top.rename(columns={'area_name': 'Регион', 'salary': 'Средняя зарплата'}, inplace=True)

    vacancies_count_city_top = vacancies_city.reset_index(level=0)[['area_name', 'name']].sort_values('name',
                                                                                                      ascending=0).head(
        10)
    vacancies_count_city_top.rename(columns={'area_name': 'Регион', 'name': 'Доля вакансий'}, inplace=True)

    # vacancies['Год'] = vacancies['published_at'].str[:4]
    #
    # vacancy_salary = round(vacancies[(vacancies['name'].str.lower().str.contains(vacancy.lower())) & (
    #         vacancies['area_name'].str.lower() == area_name.lower())][['Год', 'salary']].groupby('Год').mean())
    # vacancy_count = vacancies[(vacancies['name'].str.lower().str.contains(vacancy.lower())) & (
    #         vacancies['area_name'].str.lower() == area_name.lower())].groupby('Год')['name'].count()
    # statistic_vacancy = pd.merge(vacancy_salary, vacancy_count, how='left', on='Год').fillna(0).astype(int) \
    #     .reset_index(level=0)
    # statistic_vacancy.rename(columns={'salary': f'Средняя зарплата',
    #                                   'name': f'Количество вакансий'}, inplace=True)
    # statistic_vacancy = pd.merge(pd.DataFrame({'Год': vacancies['Год'].unique()}), statistic_vacancy, how='left',
    #                              on='Год').fillna(0).astype(int)
    return [vacancies_salary_city_top, vacancies_count_city_top]


# def get_pdf(dataframes, vacancy, area_name):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('statistic_city_with_pandas.html')
#     pdf_template = template.render({'table0': dataframes[0].to_html(index=False),
#                                     'table1': dataframes[1].to_html(index=False),
#                                     'table2': dataframes[2].to_html(index=False),
#                                     'vacancy': vacancy, 'area_name': area_name})
#     config = pdfkit.configuration(wkhtmltopdf=r'D:\Проги\wkhtmltopdf\bin\wkhtmltopdf.exe')
#     pdfkit.from_string(pdf_template, 'statistic_city_with_pandas.pdf',
#                        configuration=config, options={"enable-local-file-access": ""})
if __name__ == '__main__':
    file_path = "data/vacancies_with_skills_middle_salary.csv"
    vacancy = 'C# программист'
    # area_name = 'Пермь'
    statistic = get_dataframes(file_path, vacancy)
    statistic[0].to_csv('../static/CSharpProgrammer/data/top_city_salary.csv', index=False)
    statistic[1].to_csv('../static/CSharpProgrammer/data/top_city_count.csv', index=False)

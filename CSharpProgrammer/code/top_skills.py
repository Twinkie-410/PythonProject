import pandas as pd
import csv

pd.set_option("display.max_columns", False)
pd.set_option("expand_frame_repr", False)


class DictYearSkills:
    def __init__(self):
        self.data_dict = {}

    def __str__(self):
        return self.data_dict.__str__()

    def add_data(self, year, skill):
        if year not in self.data_dict.keys():
            self.data_dict[year] = {skill: 1}
        else:
            if skill not in self.data_dict[year].keys():
                self.data_dict[year][skill] = 1
            else:
                self.data_dict[year][skill] += 1

    def get_top_skills_by_year(self):
        top_skills_by_year = {}
        for year, skills in self.data_dict.items():
            top_skills_at = dict(sorted(skills.items(), key=lambda item: item[1], reverse=True)[:10])
            top_skills_by_year[year] = top_skills_at
        return top_skills_by_year


def get_dataframe(file):
    vacancies = pd.read_csv(file)
    vacancies = vacancies[vacancies['key_skills'].notna()]
    vacancies['Год'] = vacancies['published_at'].str[:4]
    sharp_vacancy = vacancies.query('name.str.lower().str.contains("c#".lower()) or '
                                    'name.str.lower().str.contains("c sharp".lower()) or '
                                    'name.str.lower().str.contains("шарп".lower())')
    # vacancy_skills = sharp_vacancy[['Год', 'key_skills']]
    # print(vacancy_skills)
    # vacancy_skills['key_skills'].apply(lambda x: x.split())
    # print(vacancy_skills)
    # vacancy_skills = sharp_vacancy[['Год', 'key_skills']].groupby(['Год', 'key_skills'])
    # print(vacancy_skills)

    # vacancy_salary = round(sharp_vacancy[['Год', 'salary']].groupby('Год').mean())
    # vacancy_count = sharp_vacancy.groupby('Год')['name'].count()
    # statistic_vacancies = pd.merge(vacancies_salary, vacancies_count, how='left', on='Год')
    # statistic_vacancies.rename(columns={'salary': 'Средняя зарплата', 'name': 'Количество вакансий'}, inplace=True)
    # statistic_vacancy = pd.merge(vacancy_salary, vacancy_count, how='left', on='Год')
    # statistic_vacancy.rename(columns={'salary': f'Средняя зарплата - {vacancy}',
    #                                   'name': f'Количество вакансий - {vacancy}'}, inplace=True)
    # statistic = pd.merge(statistic_vacancies, statistic_vacancy, how='left', on='Год').fillna(0).astype(int) \
    #     .reset_index(level=0)
    return sharp_vacancy


def get_top_skills(file):
    with open(file, encoding='utf-8') as csv_file:
        vacancies = csv.reader(csv_file)
        year_skill_count = DictYearSkills()
        vacancies.__next__()
        for vacancy in vacancies:
            for skill in vacancy[1].split():
                year_skill_count.add_data(vacancy[5], skill)
        return year_skill_count.get_top_skills_by_year()


def write_to_csv(data_skills):
    with open('data/top_skills_by_year.csv', 'w', encoding='utf-8', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['Год', 'Навык', 'Количество'])
        for year, skills in data_skills.items():
            for skill, count in skills.items():
                writer.writerow([year, skill, count])


if __name__ == '__main__':
    # file_path = "data/vacancies_with_skills_middle_salary.csv"
    # statistic = get_dataframe(file_path)
    sharp_vacancy_file = 'data/Csharp_vacancy.csv'
    # statistic.to_csv(sharp_vacancy_file, index=False)
    top_skills = get_top_skills(sharp_vacancy_file)
    write_to_csv(top_skills)

from django.shortcuts import render
from CSharpProgrammer.models import *


# Create your views here.
def main_page(request):
    return render(request, 'CSharpProgrammer/main.html', {'tittle': 'Главная страница'})


def relevance(request):
    data = StatisticYear.objects.all()
    return render(request, 'CSharpProgrammer/relevance.html', {'tittle': 'Востребованность', 'data': data})


def geography(request):
    top_salary = StatisticTopSalaryCity.objects.all()
    top_count = StatisticTopCountCity.objects.all()
    return render(request, 'CSharpProgrammer/geography.html', {'tittle': 'География', 'top_salary': top_salary, 'top_count': top_count})


def skills(request):
    data = TopSkills.objects.all()
    dict_skills = {}
    for record in data:
        if record.year not in dict_skills.keys():
            dict_skills['year'] = [(record.skill, record.count)]
        else:
            dict_skills['year'] += [(record.skill, record.count)]
    return render(request, 'CSharpProgrammer/skills.html', {'tittle': 'Навыки', 'data': dict_skills})


def recent_vacancies(request):
    return render(request, 'CSharpProgrammer/recent_vacancies.html', {'tittle': 'Последние вакансии'})

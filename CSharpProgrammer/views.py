from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'CSharpProgrammer/main.html', {'tittle': 'Главная страница'})


def relevance(request):
    return render(request, 'CSharpProgrammer/relevance.html', {'tittle': 'Востребованность'})


def geography(request):
    return render(request, 'CSharpProgrammer/geography.html', {'tittle': 'География'})


def skills(request):
    return render(request, 'CSharpProgrammer/skills.html', {'tittle': 'Навыки'})


def recent_vacancies(request):
    return render(request, 'CSharpProgrammer/recent_vacancies.html', {'tittle': 'Последние вакансии'})

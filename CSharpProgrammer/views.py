from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'CSharpProgrammer/main.html')


def relevance(request):
    return render(request, 'CSharpProgrammer/main.html')


def geography(request):
    return render(request, 'CSharpProgrammer/main.html')


def skills(request):
    return render(request, 'CSharpProgrammer/main.html')


def recent_vacancies(request):
    return render(request, 'CSharpProgrammer/main.html')

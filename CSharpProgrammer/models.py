from django.db import models


class Profession(models.Model):
    name = models.CharField("Название", max_length=40)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"


class StatisticYear(models.Model):
    year = models.IntegerField("Год")
    middle_salary = models.IntegerField("Средняя зарплата")
    count_vacancy = models.IntegerField("Количество вакансий")
    middle_salary_profession = models.IntegerField("Средняя зарплата C# Программиста")
    count_vacancy_profession = models.IntegerField("Колличество вакансий C# Программист")


class StatisticTopSalaryCity(models.Model):
    city = models.CharField("Регоин", max_length=40)
    salary = models.FloatField("Средняя зарплата")


class StatisticTopCountCity(models.Model):
    city = models.CharField("Регоин", max_length=40)
    count = models.FloatField("Доля вакансий")

    def get_percent(self):
        return f'{round(self.count * 100, 2)}%'


class TopSkills(models.Model):
    year = models.IntegerField("Год")
    skill = models.CharField("Навык", max_length=80)
    count = models.IntegerField("Встречается столько раз")

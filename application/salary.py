def calculate_salary():
    income = 15000
    bonus = int(input(f'Сколько премий вы получили за месяц?\n'))
    print(f'Ваша зарплата:{income + bonus * 5000}')

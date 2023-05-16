'''
предсказать в зависимости от опыта работы оплачивает ли сотрудник аккаунт или нет
'''

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"
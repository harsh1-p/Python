from datetime import date

def age(birth_date):
    today = date.today()

    agee = today.year - birth_date.year - (
        (today.month, today.day) <
        (birth_date.month, birth_date.day)
    )

    return agee

birth_date = date(2006, 8, 23)

print(age(birth_date))
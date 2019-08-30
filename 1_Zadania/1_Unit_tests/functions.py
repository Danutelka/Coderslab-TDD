from datetime import datetime

# zad 1
#def div(a, b):
#    return a / b
# najpierw int później po kolejnych testach zmiana na float

def div(a, b):
    a = float(a)
    b = float(b)
    return a / b


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "female" if int(pesel[-2]) % 2 == 0 else "male"
    month = int(pesel[2:4])
    day = int(pesel[4:6]) 
    if month > 12:
        year = int("20" + pesel[0:2])
        month = month - 20
    else:
        year = int("19" + pesel[0:2])
    birth_date = datetime(year, month, day)
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result

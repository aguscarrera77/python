from datetime import datetime
import random

def saludar(nombre):
    hora=datetime.now().hour
    if hora<12:
        return f"Buenos dias {nombre}"
    elif hora<18:
        return f"Buenas tardes {nombre}"
    else:
        return f"Buenas noches {nombre}"

def lucky_number():
    return random.randint(1,12)



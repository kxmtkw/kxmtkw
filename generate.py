from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

def age() -> str:
    birthday = datetime(2008, 7, 8)
    today = datetime.now()

    span = relativedelta(today, birthday)

    return f"{span.years} Years, {span.months} Month{'s' if span.months != 1 else ''}, {span.days} Day{'s' if span.days != 1 else ''}"


_data: dict | None = None
def getData() -> dict:
    global _data

    if _data: return _data

    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError, json.JSONDecodeError:
        print("data.json does not exist or is corrupted!")
        exit(1)

    _data = data

    return data
    

def expertise() -> list[str]:
    return getData().get("expertise", [])


def hobbies() -> list[str]:
    return getData().get("hobbies", [])


def technologies() -> list[str]:
    return getData().get("technologies", [])


def contactInfo() -> dict[str, str]:
    return getData().get("contactInfo", {})







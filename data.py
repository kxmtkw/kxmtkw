from datetime import datetime
from dateutil.relativedelta import relativedelta
import json


_data: dict | None = None
def getData() -> dict:
	global _data

	if _data: return _data

	try:
		with open("data.json") as file:
			data = json.load(file)
	except (FileNotFoundError, json.JSONDecodeError):
		print("data.json does not exist or is corrupted!")
		exit(1)

	_data = data

	return data

def name() -> str:
	return getData().get("name", "Unknown")


def location() -> str:
	return getData().get("location", "Unknown")


def role() -> str:
	return getData().get("role", "Unknown")


def age() -> str:
	birthday_raw = getData().get("birthday", [0, 0, 0])
	birthday = datetime(birthday_raw[0], birthday_raw[1], birthday_raw[2])
	today = datetime.now()

	span = relativedelta(today, birthday)

	return f"{span.years} Years, {span.months} Month{'s' if span.months != 1 else ''}, {span.days} Day{'s' if span.days != 1 else ''}"


def expertise() -> list[str]:
	return getData().get("expertise", [])


def hobbies() -> list[str]:
	return getData().get("hobbies", [])


def technologiesOS() -> str:
	return getData().get("technologies.os", [])


def technologiesLanguages() -> list[str]:
	return getData().get("technologies.languages", [])


def technologiesTools() -> list[str]:
	return getData().get("technologies.tools", [])


def contactInfo() -> dict[str, str]:
	return getData().get("contactInfo", {})


		
		  

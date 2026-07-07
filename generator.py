from datetime import datetime
import subprocess
from dateutil.relativedelta import relativedelta
import json

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import SvgFormatter


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
    except (FileNotFoundError, json.JSONDecodeError):
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


def makeReadme(content: str, svg: str, readme: str):
		
	formatter = SvgFormatter(style="monokai", font_family="iosevka", font_size=18, line_height=1)

	with open(svg, "w") as f:
		highlight(content, PythonLexer(), formatter, f)
		
	height = content.count('\n') * 21
	width = max(len(h) for h in content.splitlines()) * 10
     
	readme_content = f'<img src="{svg}" width="{width}" height="{height}" alt="Github Profile">'

	with open(readme, "w") as f:
		f.write(readme_content)
          

def pushToGithub():
	subprocess.run("git add .", shell=True, capture_output=True)
	subprocess.run(f"git commit -m 'Manual'", shell=True, capture_output=True)
	subprocess.run("git push", shell=True, capture_output=True)
from datetime import datetime
import time
from pathlib import Path

from pygments import highlight
from pygments.lexers.data import YamlLexer
from pygments.formatters import SvgFormatter

import data


def generateReadmeContent() -> str:

	print(f"* Making readme...")

	hobbies = "\n".join(f"    - {h}" for h in data.hobbies())
	expertise = "\n".join(f"    - {e}" for e in data.expertise())

	os = data.technologiesOS()
	languages = f"{', '.join(data.technologiesLanguages())}"
	tools = f"{', '.join(data.technologiesTools())}"

	contacts_dict = data.contactInfo()
	longest_contact_key = max(len(key) for key in contacts_dict.keys()) + 2
	contacts = "\n".join(
		f"    {f'{key}:':<{longest_contact_key}} {val}" for key, val in contacts_dict.items()
	)

	today = datetime.now().strftime("%d-%B-%Y %I:%M %p")

	readme = f"""# About me
profile:
    - name:      {data.name()}
    - age:       {data.age()}
    - location:  {data.location()}
    - role:      {data.role()}

	
# Stuff I do for fun
hobbies:
{hobbies}


# I can do these
expertise:
{expertise}


# I use these
technologies:
    - os:         {os}
    - languages:  {languages}
    - tools:      {tools}

	
# If you want to get in contact with me for some reason
contacts:
{contacts}


# Last updated at: {today}"""

	return readme


def generateReadmeSVG(readme: str, svg: str):

	print(f"* Generating svg...")

	formatter = SvgFormatter(style="monokai", fontfamily="Iosevka", fontsize="16", line_height=1)

	with open(svg, "w") as f:
		highlight(readme, YamlLexer(), formatter, f)
		
	height = readme.count('\n') * 22
	width = max(len(h) for h in readme.splitlines()) * 10
		
	readme_content = f'<img src="{svg}" width="{width}" height="{height}" alt="If you see this, then the readme svg has not loaded yet. Please wait :)">'

	with open("README.md", "w") as f:
		f.write(readme_content)


def make():
	
	if not Path("profile").exists():
		Path("profile").mkdir()
	else:
		for item in Path("profile").iterdir():
			if item.is_file(): item.unlink()

	# ahhhh github does not update svgs instantly even if their content changes. 
	# this allows me to generate a completely unique svg name which github will HAVE to load
	current_time = time.time()
	svg = f"profile/{int(current_time)}.svg"

	readme = generateReadmeContent()

	print("-"*40)
	print(readme)
	print("-"*40)

	generateReadmeSVG(readme, svg)

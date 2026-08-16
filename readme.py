import time
from pathlib import Path

from pygments import highlight
from pygments.lexers.data import YamlLexer
from pygments.formatters import SvgFormatter

import data


def generateReadmeContent() -> str:

	hobbies = "\n".join(f"    - {h}" for h in data.hobbies())
	expertise = "\n".join(f"    - {e}" for e in data.expertise())

	os = data.technologiesOS()
	languages = f"[ {', '.join(data.technologiesLanguages())} ]"
	tools = f"[{', '.join(data.technologiesTools())}]"

	contacts_dict = data.contactInfo()
	longest_contact_key = max(len(key) for key in contacts_dict.keys())
	contacts = "\n".join(
		f"    {key:<{longest_contact_key}} : {val}" for key, val in contacts_dict.items()
	)

	readme = f"""# Profile
profile:
    - name     : {data.name()}
    - age      : {data.age()}
    - location : {data.location()}
    - role     : {data.role()}

# Hobbies
hobbies:
{hobbies}

# Focus & Skills
expertise:
{expertise}

# Stuff I use
technologies:
    - os        : {os}
    - languages : {languages}
    - tools     : {tools}

# Communications
contacts:
{contacts}
"""

	return readme


def generateReadmeSVG(readme: str, svg: str):

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
	print(readme)
	generateReadmeSVG(readme, svg)

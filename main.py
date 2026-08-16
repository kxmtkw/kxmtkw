import generator
hobbies = generator.hobbies()
expertise = generator.expertise()
techs = generator.technologies()
contacts = generator.contactInfo()

fmt_hobbies = "\n".join(f"    - {h}" for h in hobbies)
fmt_expertise = "\n".join(f"    - {e}" for e in expertise)
fmt_techs = "\n".join(f"    - {t}" for t in techs)

longest_contact_key = max(len(key) for key in contacts.keys())
fmt_contacts = "\n".join(
    f"  {key:<{longest_contact_key}} : {val}" for key, val in contacts.items()
)

readme = f"""# Profile
profile:
    name     : {generator.name()}
    age      : {generator.age()}
    location : {generator.location()}

# Hobbies
hobbies:
{fmt_hobbies}

# Focus & Skills
expertise:
{fmt_expertise}

technologies:
{fmt_techs}

# Communications
contacts:
{fmt_contacts}
"""

print(readme)

import time
from pathlib import Path

if not Path("profile").exists():
	Path("profile").mkdir()
else:
	for item in Path("profile").iterdir():
		if item.is_file(): item.unlink()


time = time.time()
svg = f"profile/{int(time)}.svg"

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
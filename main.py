import generator

age = generator.age()
hobbies = generator.hobbies()
expertise = generator.expertise()
techs = generator.technologies()
contacts = generator.contactInfo()

fmt_hobbies = "\n".join(f"  - {h}" for h in hobbies)
fmt_expertise = "\n".join(f"  - {e}" for e in expertise)
fmt_techs = "\n".join(f"  - {t}" for t in techs)

longest_contact_key = max(len(key) for key in contacts.keys())
fmt_contacts = "\n".join(
    f"  {key:<{longest_contact_key}} : {val}" for key, val in contacts.items()
)

readme = f"""# Profile
profile:
  name     : "A. Haseeb Khalid"
  age      : {age}
  location : Lahore, Pakistan

# Focus & Skills
expertise:
{fmt_expertise}

technologies:
{fmt_techs}

# Hobbies
hobbies:
{fmt_hobbies}

# Communications
contacts:
{fmt_contacts}
"""

import os 

if os.path.exists("profile1.svg"):
	os.remove("profile1.svg")
	svg = "profile2.svg"
elif os.path.exists("profile2.svg"):
	os.remove("profile2.svg")
	svg = "profile1.svg"
else:
	svg = "profile1.svg"

print(readme)

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
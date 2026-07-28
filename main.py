import generator


age = generator.age()
hobbies   = [str(h) for h in generator.hobbies()]
expertise = [str(e) for e in generator.expertise()]
techs     = [str(t) for t in generator.technologies()]


contact_dict = generator.contactInfo()
contact_rows = [f"CONTACT_{str(key).upper()}={str(val)}" for key, val in contact_dict.items()]

delimiter = ",\n            "
readme = f"""
haseeb@host $ whoami
haseeb

haseeb@host $ cat age.txt
{age}

haseeb@host $ ls hobbies
{'\n'.join(hobbies)}

haseeb@host $ ls technologies
{' '.join(techs)}

haseeb@host $ ls expertise
{'\n'.join(expertise)}

haseeb@host $ printenv | grep CONTACT
{'\n'.join(contact_rows)}
	"""

print(readme)
import os

if os.path.exists("profileA.svg"):
	os.remove("profileA.svg")
	svg = "profileB.svg"
else:
	svg = "profileA.svg"

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
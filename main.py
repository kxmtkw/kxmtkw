import generator


age = generator.age()
location = generator.location()
hobbies   = [f"- {str(h)}" for h in generator.hobbies()]
expertise = [f"- {str(e)}" for e in generator.expertise()]
techs     = [str(t) for t in generator.technologies()]


contact_dict = generator.contactInfo()
longest_key = max([len(key) for key in contact_dict.keys()])
contact_rows = [
    f'CONTACT_{str(key).upper():<{longest_key}} = {val}'
    for key, val in contact_dict.items()
]

delimiter = ",\n            "
readme = f"""
$ whoami
haseeb

$ cat /etc/age
{age}

$ tree ~/.hobbies"
hobbies
{'\n    ├──'.join(hobbies)}

$ echo $technologies
{' | '.join(techs)}

$ printenv | grep CONTACT
{'\n'.join(contact_rows)}
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
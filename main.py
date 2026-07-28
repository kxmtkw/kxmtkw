import generator


age = generator.age()
location = generator.location()
hobbies   = [f"- {str(h)}" for h in generator.hobbies()]
expertise = [f"- {str(e)}" for e in generator.expertise()]
techs     = [str(t) for t in generator.technologies()]


contact_dict = generator.contactInfo()
contact_rows = [f"CONTACT_{str(key).upper()}={str(val)}" for key, val in contact_dict.items()]

delimiter = ",\n            "
readme = f"""
$ whoami
haseeb

$ cat info.txt
Age:       {age}
Location:  {location}

haseeb@host $ ls -1 hobbies
{'\n'.join(hobbies)}

haseeb@host $ ls technologies
{' '.join(techs)}

haseeb@host $ ls expertise
{'\n'.join(expertise)}

haseeb@host $ printenv | grep CONTACT
{'\n'.join(contact_rows)}
	"""


import os

if os.path.exists("profileA.svg"):
	os.remove("profileA.svg")
	svg = "profileB.svg"
else:
	svg = "profileA.svg"

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
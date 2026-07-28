import generator


age = generator.age()
location = generator.location()
hobbies   = [str(h) for h in generator.hobbies()]
expertise = [str(e) for e in generator.expertise()]
techs     = [str(t) for t in generator.technologies()]


contact_dict = generator.contactInfo()
contact_rows = [f"CONTACT_{str(key).upper()}={str(val)}" for key, val in contact_dict.items()]

delimiter = ",\n            "
readme = f"""
$ whoami
haseeb

$ cat info.txt
Age:       "{age}
Location:  {location}

$ ls -1 hobbies
{'\n'.join(hobbies)}

$ ls -1 expertise
{'\n'.join(expertise)}

$ echo "${{technologies[@]}}"
{' '.join(techs)}

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

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
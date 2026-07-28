import generator

age = generator.age()
hobbies   = [repr(h) for h in generator.hobbies()]
expertise = [repr(e) for e in generator.expertise()]
techs     = [repr(t) for t in generator.technologies()]


contact_dict = generator.contactInfo()
longest_contact_key = max(len(key) for key in contact_dict.keys())
contact_rows = [f"{repr(key):<{longest_contact_key + 2}} : {repr(val)}" for key, val in contact_dict.items()]

delimiter = ",\n            "
readme = f"""
from organisms import Human
from countries import Pakistan


class Haseeb(Human):


    def __init__(self):
        self.name     = "A. Haseeb Khalid"
        self.age      = "{age}"
        self.location = Pakistan.Lahore

        
    def hobbies(self) -> list[str]:
        return [
            {delimiter.join(hobbies)}
        ]


    def expertise(self) -> list[str]:
        return [
            {delimiter.join(expertise)}
        ]


    def technologies(self) -> list[str]:
        return [
            {delimiter.join(techs)}
        ]


    def contactInfo(self) -> dict[str, str]:
        return {{
            {delimiter.join(contact_rows)}
        }}


def main():
    haseeb = Haseeb()

if __name__ == "__main__":
    main()
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
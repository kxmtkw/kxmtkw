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
from universe.organisms import Human
from universe.planets.earth import Pakistan


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
    haseeb.live()


if __name__ == "__main__":
    main()
	"""

import os

if os.path.exists("profileA.svg"):
	svg = "profileB.svg"
else:
	svg = "profileA.svg"

generator.makeReadme(readme, svg, "README.md")	
generator.pushToGithub()
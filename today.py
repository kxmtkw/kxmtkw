import subprocess
from datetime import datetime
import generate
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import SvgFormatter


age = generate.age()
hobbies   = [repr(h) for h in generate.hobbies()]
expertise = [repr(e) for e in generate.expertise()]
techs     = [repr(t) for t in generate.technologies()]


contact_dict = generate.contactInfo()
longest_contact_key = max(len(key) for key in contact_dict.keys())
contact_rows = [f"{repr(key):<{longest_contact_key + 2}} : {repr(val)}" for key, val in contact_dict.items()]


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
			{',\n			'.join(hobbies)}
		]


	def expertise(self) -> list[str]:
		return [
			{',\n			'.join(expertise)}
		]


	def technologies(self) -> list[str]:
		return [
			{',\n			'.join(techs)}
		]


	def contactInfo(self) -> dict[str, str]:
		return {{
			{',\n			'.join(contact_rows)}
		}}


def main():
	haseeb = Haseeb()
	haseeb.live()


if __name__ == "__main__":
	main()
"""


formatter = SvgFormatter(style="monokai", font_family="monospace", font_size=10, line_height=1.4)

with open("profile_code.svg", "w") as f:
	highlight(readme, PythonLexer(), formatter, f)
	
print(">> Written Readme")

print(">> Pushing to github")


subprocess.run("git add .", shell=True, capture_output=True)
subprocess.run(f"git commit -m {datetime.now().strftime('%d/%m/%y')}", shell=True, capture_output=True)
subprocess.run("git push", shell=True, capture_output=True)
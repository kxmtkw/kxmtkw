
from universe.organisms import Human
from universe.planets.earth import Pakistan


class Haseeb(Human):

	def __init__(self):
		self.name     = "A. Haseeb Khalid"
		self.age      = "17 Years, 11 Months, 29 Days"
		self.location = Pakistan.Lahore

	def hobbies(self) -> list[str]:
		return [
			'Learning about computers',
			'Losing in chess',
			'Procrastinating'
		]


	def expertise(self) -> list[str]:
		return [
			'Low level programming',
			'Systems design and architecture',
			'Automating stuff because I am lazy'
		]


	def technologies(self) -> list[str]:
		return [
			'c',
			'c++',
			'python',
			'linux',
			'git'
		]


	def contactInfo(self) -> dict[str, str]:
		return {
			'mail'    : 'abdulhaseeb.8j@gmail.com',
			'discord' : 'kxmtkw',
			'insta'   : 'haseebolall'
		}


def main():
	haseeb = Haseeb()
	haseeb.live()


if __name__ == "__main__":
	main()

import subprocess
import readme

def pushToGithub():
	commit = input("> Enter Commit Message: ")

	print("* Pushing to github...")

	subprocess.run("git pull", shell=True, capture_output=True)
	subprocess.run("git add .", shell=True, capture_output=True)
	subprocess.run(f"git commit -m '{commit}'", shell=True, capture_output=True)
	subprocess.run("git push", shell=True, capture_output=True)
	print("* Successfully pushed to github.")

def main():
	readme.make()
	pushToGithub()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n* Aborted")
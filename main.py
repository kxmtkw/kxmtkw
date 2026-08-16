import subprocess
import readme

def pushToGithub():
	subprocess.run("git pull", shell=True, capture_output=True)
	subprocess.run("git add .", shell=True, capture_output=True)
	subprocess.run(f"git commit -m 'Manual'", shell=True, capture_output=True)
	subprocess.run("git push", shell=True, capture_output=True)

def main():
	readme.make()
	pushToGithub()


if __name__ == "__main__":
	main()
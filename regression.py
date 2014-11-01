import subprocess

subprocess.check_call(["coverage", "run", "--source", "toyplot", "-m", "nose"])
subprocess.check_call(["coverage", "run", "--append", "--source", "toyplot", "-m", "behave"])
subprocess.check_call(["coverage", "report"])

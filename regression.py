import subprocess

subprocess.check_call(["coverage", "run", "--source", "toyplot", "--omit", "toyplot/testing.py", "-m", "nose"])
subprocess.check_call(["coverage", "run", "--append", "--source", "toyplot", "--omit", "toyplot/testing.py", "-m", "behave"])
subprocess.check_call(["coverage", "report"])
subprocess.check_call(["coverage", "html", "--directory", ".cover"])

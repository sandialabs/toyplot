import subprocess

subprocess.call(["coverage", "run", "--source", "toyplot",
                 "--omit", "toyplot/testing.py", "-m", "nose", "--exclude-dir", "toyplot"])
subprocess.call(["coverage", "run", "--append", "--source",
                 "toyplot", "--omit", "toyplot/testing.py", "-m", "behave"])
subprocess.call(["coverage", "report"])
subprocess.call(["coverage", "html", "--directory", ".cover"])

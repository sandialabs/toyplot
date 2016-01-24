# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import subprocess

subprocess.call(["coverage", "run", "--source", "toyplot",
                 "--omit", "toyplot/testing.py", "-m", "nose", "--exclude-dir", "toyplot"])
subprocess.call(["coverage", "run", "--append", "--source",
                 "toyplot", "--omit", "toyplot/testing.py", "-m", "behave"])
subprocess.call(["coverage", "report"])
subprocess.call(["coverage", "html", "--directory", ".cover"])

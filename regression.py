# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import argparse
import subprocess

parser = argparse.ArgumentParser("Run all Toyplot regression tests.")
parser.add_argument("--show-diff", action="store_true", help="Display differences between failed tests and references.")
arguments = parser.parse_args()

subprocess.call(["coverage", "run", "--source", "toyplot", "-m", "nose", "--exclude-dir", "toyplot"])
subprocess.call(["coverage", "run", "--append", "--source",
                 "toyplot", "-m", "behave", "-D", "show_diff=True" if arguments.show_diff else "show_diff=False"])
subprocess.call(["coverage", "report"])
subprocess.call(["coverage", "html", "--directory", ".cover"])

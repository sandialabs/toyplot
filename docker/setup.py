import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("command", nargs="?", default="build", choices=["build", "push"])
arguments = parser.parse_args()

images = ["supervisord", "buildbot"]

if arguments.command == "build":
  for image in images:
    subprocess.check_call(["docker", "build", "-t", "toyplot/%s" % image, image])

if arguments.command == "push":
  for image in images:
    subprocess.check_call(["docker", "push", "toyplot/%s" % image])


# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

import argparse
import os
import subprocess
import tempfile
import xml.dom.minidom

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", help="One or more files to compare.")
arguments = parser.parse_args()

if len(arguments.files) == 1:
    paths = [os.path.join("tests/failed", arguments.files[0]),
             os.path.join("tests/reference", arguments.files[0])]
else:
    paths = arguments.files

#subprocess.check_call(["qlmanage", "-p"] + paths)

directory = tempfile.mkdtemp()
comparison_paths = []
for index, path in enumerate(paths):
    extension = os.path.splitext(path)[1]
    if extension == ".svg":
        dom = xml.dom.minidom.parse(path)
        with open(os.path.join(directory, "%s.svg" % index), "wb") as file:
            file.write(dom.toprettyxml(encoding="UTF-8", indent="  "))
        comparison_paths.append(os.path.join(directory, "%s.svg" % index))
    elif extension == ".html":
        html = open(path, "rb").read()
        with open(os.path.join(directory, "%s.html" % index), "wb") as file:
            file.write(html)
        comparison_paths.append(os.path.join(directory, "%s.html" % index))

subprocess.check_call(["vimdiff"] + comparison_paths)

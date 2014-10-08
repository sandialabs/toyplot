import datetime
import pprint
import xmlrpclib

client = xmlrpclib.ServerProxy("https://pypi.python.org/pypi")

total = 0
for release in sorted(client.package_releases("toyplot", True)):
  print "Version %s" % release
  for url in client.release_urls("toyplot", release):
    print "  %s - %s => %s" % (datetime.datetime.strptime(url["upload_time"].value, "%Y%m%dT%H:%M:%S").strftime("%B %d, %Y"), url["filename"], url["downloads"])
    total += url["downloads"]
print "Total => %s" % total

import os
import logging

def main():
  path = os.environ["PATH_INFO"]
  qs = os.getenv("QUERY_STRING")
  if qs:
    path += "?" + qs
  referer = os.environ.get("HTTP_REFERER")
  if referer:
    logging.info("Request %s from %s", path, referer)
  else:
    logging.info("Request %s", path)
  for key, value in sorted(os.environ.iteritems()):
    logging.debug("%s=%r", key, value)
  print "Status: 404 Not found"

if __name__ == '__main__':
  main()

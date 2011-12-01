# Usage: 
#
# sec2time infield=<input field name> outfield=<output field name>
#
#
# Copyright (C) 2011 Ove Ruben R Olsen Laerk. 
# See LISENCE.txt for more information.
#
import sys
import splunk.Intersplunk

from time import strftime, gmtime, time

def sec2time(seconds):
    if (seconds > 86400):
      time_string = strftime("%j %H:%M:%S", gmtime(seconds))
    else:
      time_string = strftime("%H:%M:%S", gmtime(seconds))
    return time_string



try:

  keywords,options = splunk.Intersplunk.getKeywordsAndOptions()

  if not options.has_key('infield'):
     splunk.Intersplunk.generateErrorResults("no field specified")
     exit(0)

  field = options.get('infield', None)
  output = options.get('outfield', None)

  results,dymmy,settings = splunk.Intersplunk.getOrganizedResults()
  for r in results:
    if field not in r:
      continue

    r[output] = sec2time(int(r[field]))

  splunk.Intersplunk.outputResults(results)



except Exception, e:
	results = splunk.Intersplunk.generateErrorResults(str(e))

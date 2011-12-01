# Usage: 
#
# sec2time infield=<input field name> outfield=<output field name>
#
#
# Copyright (C) 2011 Ove Ruben R Olsen Laerk
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
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

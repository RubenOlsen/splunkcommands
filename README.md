# Splunk custom search command
This repository contains custom Splunk search commands.

# sec2time infield=_<fieldname>_ outfield=_<new field name>_
This function will convert a integer entry in the infield (if exists) to a ISO-8601 formatted value (i.e. variants of _24 13:45:56_ - where "24" is the number of days), and put the result into a field name given in outfield.

## Search example usage
    |metadata type=sources |eval LastSeen=now()-recentTime | sec2time infield=LastSeen outfield=LastSeen | rename totalCount as Count recentTime as "Last Update" LastSeen as "Last Seen" | table source Count "Last Update" "Last Seen" | fieldformat "Last Update"=strftime('Last Update', "%Y-%m-%d %T")



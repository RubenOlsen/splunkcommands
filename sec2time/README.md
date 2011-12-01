# sec2time infield=_\<fieldname\>_ outfield=_\<new field name\>_

This function will convert a integer entry in the fieldname given by _infield_ (if exists) to a ISO-8601 formatted value (i.e. variants of _24 13:45:56_ - where "24" is the number of days), and put the result into a field name given in outfield.

As of version 4.2 of Splunk, the various use of strftime() is unfortunately epoch based, thus they are not suitable to give you a correct time representation of a given number of seconds. 

# Usage example in search 
    |metadata type=sources |eval LastSeen=now()-recentTime | sec2time infield=LastSeen outfield=LastSeen | rename totalCount as Count recentTime as "Last Update" LastSeen as "Last Seen" | table source Count "Last Update" "Last Seen" | fieldformat "Last Update"=strftime('Last Update', "%Y-%m-%d %T")


# Maitenance and bugreporting
The latest version of this code is found at https://github.com/RubenOlsen/splunkcommands
This is also the place where you can report bugs.

# Installation

1. Copy the content of the _bin_ directory into $SPLUNK_HOME/etc/apps/search/bin/.
2. Copy the content of the file(s) found in the _local_ directory into the corresponding files in $SPLUNK_HOME/etc/apps/search/local/





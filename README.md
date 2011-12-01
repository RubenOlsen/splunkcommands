# Splunk custom search commands
This repository contains custom Splunk search commands.

# Commands
## sec2time infield=_\<fieldname\>_ outfield=_\<new field name\>_
This function will convert a integer entry in the infield (if exists) to a ISO-8601 formatted value (i.e. variants of _24 13:45:56_ - where "24" is the number of days), and put the result into a field name given in outfield.


# Maitenance and bugreporting
The latest version of this code is found at https://github.com/RubenOlsen/splunkcommands
This is also the place where you can report bugs.


# Installation
For each of the commands you want to install, you should follow the following procedure:

1. Copy the content of the _bin_ directory into $SPLUNK_HOME/etc/apps/search/bin/.
2. Copy the content of the file(s) found in the _local_ directory into the corresponding files in $SPLUNK_HOME/etc/apps/search/local/

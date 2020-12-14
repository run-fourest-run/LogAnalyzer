Application: Python Log Analyzer 

Author: Alexander Fournier - alexander.fournier@getmanta.com

Reference Links:

* Project Business Request: https://mantatools.atlassian.net/wiki/spaces/MT/pages/1842315319/HD-2493




Description: 

This python program reads a MANTA log file and derives key performance indicators,summary statistics & attributes based on the text within the files.
Each log file can be thought of as a hierarchal structure. At the highest level there is the log file. Next there are the individual messages written to each log file
Finally there is the thread number of each message.

Attributes:
Attributes of each member of the hierarchy should be exposed. 

Log File:  
* Log File Name
* Source System
* Configuration Setting (timeout, edgelimit)
* Date of Run


Message:
* Phase (Extraction or Analysis)
* Message Name



Thread:
* Thread Number
* Message Name


Key Performance Indicators/Summary Statistics:

Log Files:
* Total time of Execution
* Total time of Execution by Phase (Extraction,Analysis)
* Aggregated Edged connected
* Aggregated Number of direct edges


Message:
* Total time of execution (per message)
* number of edge limits
* number of filter edges dropped
* number of timeouts




Thread:
*











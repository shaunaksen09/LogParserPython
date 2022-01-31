# Python log parser

Simple python script to parse the logfile and calculate the % of 5xx errors broken down by domain, for a given timeframe


## Output: 

Between time 1493969101.638 and time 1493969101.679 in file log_sample.txt:
player.vimeo.com returned 61.53846153846154% 5xx errors
vimeo.com returned 30.76923076923077% 5xx errors
video_vimeo.com returned 7.6923076923076925% 5xx errors

Between time 1493969101.638 and time 1493969101.679 in file xyz.txt:
No 5xx errors were logged


## Assumptions
1: Python 3 is already installed on the machine. This script is python 3 compatible.

2: Specify full path for the file or the script will only look in the working directory.

3: Log line format remains unchanged.

## Error Handling: 

1. In progress

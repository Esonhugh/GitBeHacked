# GitBeHacked

## A Lab of Funny idea for Git dir leak hack tools hack back

## idea came from [there](https://twitter.com/drivertomtt/status/1422806890254200835?s=19)

# Usage :

```
$ sudo python3 GitBeHacked.py -h

              ____ _ _   ____       _   _            _            _ 
             / ___(_) |_| __ )  ___| | | | __ _  ___| | _____  __| |
            | |  _| | __|  _ \ / _ \ |_| |/ _` |/ __| |/ / _ \/ _` |
            | |_| | | |_| |_) |  __/  _  | (_| | (__|   <  __/ (_| |
             \____|_|\__|____/ \___|_| |_|\__,_|\___|_|\_\___|\__,_|
                                                                        
usage: GitBeHacked.py [-h] [-D OUTPUTDIRECTORYNAME] [--user USER] [--os OS] [--method METHOD] [--badfilename BADFILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -D OUTPUTDIRECTORYNAME, --outputDirectoryName OUTPUTDIRECTORYNAME
                        your repo with contain in this directory default is test
  --user USER           target username
  --os OS               os version [ win, linux ] default is linux
  --method METHOD       attack method [ cron, start, rcfile ]
  --badfilename BADFILENAME
                        badfile in cron mode name

```

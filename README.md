# GitBeHacked

## A Lab of Funny idea for Git dir leak hack tools hack back


# Usage :

```

              ____ _ _   ____       _   _            _            _ 
             / ___(_) |_| __ )  ___| | | | __ _  ___| | _____  __| |
            | |  _| | __|  _ \ / _ \ |_| |/ _` |/ __| |/ / _ \/ _` |
            | |_| | | |_| |_) |  __/  _  | (_| | (__|   <  __/ (_| |
             \____|_|\__|____/ \___|_| |_|\__,_|\___|_|\_\___|\__,_|
                                                                        
[?] create a repo which contains the file at parent dict and hack back the "githack" like tools
                                                                        
usage: GitBeHacked.py [-h] [-D OUTPUTDIRECTORYNAME] [-u USER] [-o {win,linux}] [-m {cron,start,rcfile,msg}] [-B BADFILENAME] [-p ATPATH]

optional arguments:
  -h, --help            show this help message and exit
  -D OUTPUTDIRECTORYNAME, --outputDirectoryName OUTPUTDIRECTORYNAME
                        your repo with contain in this directory default is test
  -u USER, --user USER  target username
  -o {win,linux}, --os {win,linux}
                        os version [ win, linux ] default is linux
  -m {cron,start,rcfile,msg}, --method {cron,start,rcfile,msg}
                        attack method [ cron, start, rcfile, msg ]
  -B BADFILENAME, --badfilename BADFILENAME
                        badfile in cron mode name
  -p ATPATH, --atpath ATPATH
                        bad file you want located at path such as ../../../
  -c, --clean           it will used like file clean to delete file we generate or overwrite add it to confirm

```

## method 1
rcfile need username option to gen bad file like ../../../../home/{username}/.bashrc according to the bashrc template.

## method 2
start and cron need badfilename option target has root and it will gen file like ../../../../etc/{init.d,cron.d}/{badfilename}.

## method 3
msg is just like messages ,it will read the badpayload {badfilename option} at current dir and gen a file at {atpath}.
finally, add to the git repo. so it is more general and simple.

# Aims
You can use the git repo you gen at your honeypot website.
It will let the gitHack / dumpAll -like tool occur the folder transfer.
The hacker will got funny file your add in.

# idea came from [there](https://twitter.com/drivertomtt/status/1422806890254200835?s=19)

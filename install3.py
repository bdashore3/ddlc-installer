#Installation script for DDLC mods
#(c) Brian Dashore, alias: kingbri

import os
import shutil
import distutils.dir_util
import ddlc_downloader

def download(mac):
    print ("Downloading...")
    if mac==True:
        link = ddlc_downloader.get_ddlc_url(mac)
        ddlc_downloader.download_file(link, "ddlc_mac.zip")
    else:
        link = ddlc_downloader.get_ddlc_url(mac)
        ddlc_downloader.download_file(link, "ddlc_pc.zip")

def extract(mac):
    print ("Extracting....")
    if mac == True:
        cwd = os.getcwd()
        shutil.unpack_archive("ddlc_mac.zip", extract_dir="mac", format="zip")
        os.chmod(cwd + "/mac/DDLC.app/Contents/MacOS/ddlc", 0o775)
        os.chmod(cwd + "/mac/DDLC.app/Contents/MacOS/lib/darwin-x86_64/ddlc", 0o775)
        os.remove("ddlc_mac.zip")
    else:
        cwd = os.getcwd()
        shutil.unpack_archive("ddlc_pc.zip", extract_dir=cwd, format="zip")
        os.remove("ddlc_pc.zip")

def install(os_choice):
    print ("Installing mod...")
    cwd = os.getcwd()
    if os_choice == "mac" or os_choice == "Mac":
        os.remove(cwd + "/mac/DDLC.app/Contents/Resources/autorun/game/scripts.rpa")
        distutils.dir_util.copy_tree("game", cwd + "/mac/DDLC.app/Contents/Resources/autorun/game")
    elif os_choice == "windows" or os_choice == "Windows":
        os.remove(cwd + "\DDLC-1.1.1-pc\game\scripts.rpa")
        distutils.dir_util.copy_tree("game", cwd + "\DDLC-1.1.1-pc\game")
    elif os_choice == "linux" or os_choice == "Linux":
        os.remove(cwd + "/DDLC-1.1.1-pc/game/scripts.rpa")
        distutils.dir_util.copy_tree("game", cwd + "/DDLC-1.1.1-pc/game")

print ("The mod is offered in two choices, standalone or computer-dependent")
print ("....")
print ("Standalone means that you can run the mod in a cross-platform setting")
print ("with all files saved")
print ("....")
print ("Computer-dependent means your saves will be stored on your computer and")
print ("the mod will run only on your OS")
print ("........")
print ("Mod Dir")
print ("")
print ("....")
while True:
    os_choice = input("Please enter your OS ")
    choice = "computer-dependent"
    if choice == "computer-dependent":
        if os_choice == "mac" or os_choice == "Mac":
            mac=True
            download(mac)
            extract(mac)
            install(os_choice)
            break
        elif os_choice == "windows" or os_choice == "Windows" or os_choice == "linux" or os_choice == "Linux":
            mac=False
            download(mac)
            extract(mac)
            install(os_choice)
            break
print ("Installation finished! Enjoy the mod!")

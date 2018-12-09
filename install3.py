#Installation script for DDLC mods
#(c) Brian Dashore, alias: kingbri

import os
import shutil
import distutils.dir_util
import ddlc_downloader
import standalonelogic
import time
import mod_download

def download(mac):
    if mac==True:
        print ("Downloading Mac...")
        link = ddlc_downloader.get_ddlc_url(mac)
        ddlc_downloader.download_file(link, "ddlc_mac.zip")
    else:
        print ("Downloading PC...")
        link = ddlc_downloader.get_ddlc_url(mac)
        ddlc_downloader.download_file(link, "ddlc_pc.zip")

def extract(mac):
    if mac == True:
        print ("Extracting Mac....")
        cwd = os.getcwd()
        shutil.unpack_archive("ddlc_mac.zip", extract_dir="mac", format="zip")
        os.chmod(cwd + "/mac/DDLC.app/Contents/MacOS/ddlc", 0o775)
        os.chmod(cwd + "/mac/DDLC.app/Contents/MacOS/lib/darwin-x86_64/ddlc", 0o775)
        os.remove("ddlc_mac.zip")
    else:
        print ("Extracting PC....")
        cwd = os.getcwd()
        shutil.unpack_archive("ddlc_pc.zip", extract_dir=cwd, format="zip")
        os.remove("ddlc_pc.zip")

def install(os_choice, standalone, folder):
    def os_install(os_choice):
        if os_choice == "mac" or os_choice == "Mac":
            os.remove(cwd + "/mac/DDLC.app/Contents/Resources/autorun/game/scripts.rpa")
            distutils.dir_util.copy_tree(folder + "/game", cwd + "/mac/DDLC.app/Contents/Resources/autorun/game")
        elif os_choice == "windows" or os_choice == "Windows":
            os.remove(cwd + "\DDLC-1.1.1-pc\game\scripts.rpa")
            distutils.dir_util.copy_tree(folder + "\game", cwd + "\DDLC-1.1.1-pc\game")
        elif os_choice == "linux" or os_choice == "Linux":
            os.remove(cwd + "/DDLC-1.1.1-pc/game/scripts.rpa")
            distutils.dir_util.copy_tree(folder + "/game", cwd + "/DDLC-1.1.1-pc/game")
    print ("Installing mod...")
    cwd = os.getcwd()
    if os_choice == "Mac" or os_choice == "mac" and standalone == True:
        os_choice = "Linux"
        os_install(os_choice)
    else:
        os_install(os_choice)

print ("\n" * 100)
print ("Welcome to the DDLC:TSC installer")
time.sleep(4)
print ("The mod is offered in two choices, standalone or computer-dependent")
time.sleep(4)
print ("....")
print ("Standalone means that you can run the mod in a cross-platform setting")
print ("with all files saved")
time.sleep(4)
print ("....")
print ("Computer-dependent means your saves will be stored on your computer and")
print ("the mod will run only on your OS")
time.sleep(4)
print ("........")
while True:
    os_choice = input("Please enter your OS - ")
    choice = input("Do you want standalone or computer-dependent? - ")
    if choice == "standalone" or choice == "Standalone":
        cwd = os.getcwd()
        standalone = True
        mac = True
        download(mac)
        extract(mac)
        mac = False
        download(mac)
        extract(mac)
        standalonelogic.move_mac()
        standalonelogic.standalone_run()
        os.mkdir("DDLC-1.1.1-pc/game/saves")
        mod_download.download_file("https://github.com/DDLC-TSC/TSC-code/archive/master.zip", "TSC.zip")
        mod_download.extract_mod("TSC.zip", cwd)
        install(os_choice, standalone, "TSC-code-master")
        os.remove("TSC.zip")
        shutil.rmtree("TSC-code-master")
        break
    elif choice == "computer-dependent" or choice == "Computer-dependent" or choice == "Computer Dependent" or choice == "computer-Dependent":
        if os_choice == "mac" or os_choice == "Mac":
            standalone = False
            mac=True
            download(mac)
            extract(mac)
            mod_download.download_file("https://github.com/DDLC-TSC/TSC-code/archive/master.zip", "TSC.zip")
            mod_download.extract_mod("TSC.zip", cwd)
            install(os_choice, standalone, "TSC-code-master")
            os.remove("TSC.zip")
            shutil.rmtree("TSC-code-master")
            break
        
        elif os_choice == "windows" or os_choice == "Windows" or os_choice == "linux" or os_choice == "Linux":
            standalone = False
            mac=False
            download(mac)
            extract(mac)
            mod_download.download_file("https://github.com/DDLC-TSC/TSC-code/archive/master.zip", "TSC.zip")
            mod_download.extract_mod("TSC.zip", cwd)
            install(os_choice, standalone, "TSC-code-master")
            os.remove("TSC.zip")
            shutil.rmtree("TSC-code-master")
            break
print ("Installation finished! Enjoy the mod!")

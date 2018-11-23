#Installation script for DDLC mods
#(c) Brian Dashore, alias: kingbri

import os
import shutil
import distutils.dir_util

print ("Welcome to the installer for DDLC:TSC")
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
    dir_loc = input("Please enter the mod dir (absolute path) ")
    choice = input("Do you want standalone or computer-dependent?")
    if choice == "standalone":
        print ("The standalone mod is my work where I have merged both PC and Mac versions of DDLC to coexist as one.")
        print ("This also keeps the saves in the folder so you could use the mod with multiple computers")
        if os_choice == "mac" or os_choice == "Mac" or os_choice == "Linux" or os_choice == "linux":
            try:
                os.mkdir(dir_loc + "/standalone")
            except OSError:
                shutil.rmtree(dir_loc + "/standalone", ignore_errors=True)
                os.mkdir(dir_loc + "/standalone")
            dir_loc=dir_loc + "/standalone"
            distutils.dir_util.copy_tree("standalone-mod", dir_loc)
            os.remove(dir_loc + "/game/scripts.rpa")
            distutils.dir_util.copy_tree("game", dir_loc + "/game")
            break
        elif os_choice == "Windows" or os_choice == "windows":
            try:
                os.mkdir(dir_loc + "\standalone")
            except OSError:
                shutil.rmtree(dir_loc + "\standalone", ignore_errors=True)
                os.mkdir(dir_loc + "\standalone")
            dir_loc=dir_loc + "\standalone"
            distutils.dir_util.copy_tree("standalone-mod", dir_loc)
            os.remove(dir_loc + "\game\scripts.rpa")
            distutils.dir_util.copy_tree("game", dir_loc + "\game")
            break
    elif choice == "computer-dependent":
        print ("DDLC is Dan Salvato's work, we are just adding our mod in")
        if os_choice == "mac" or os_choice == "Mac":
            try:
                os.mkdir(dir_loc + "/mac-mod")
            except OSError:
                shutil.rmtree(dir_loc + "/mac-mod", ignore_errors=True)
                os.mkdir(dir_loc + "/mac-mod")
            dir_loc = dir_loc + "/mac-mod"
            distutils.dir_util.copy_tree("ddlc-mac", dir_loc)
            os.remove(dir_loc + "/DDLC.app/Contents/Resources/autorun/game/scripts.rpa")
            distutils.dir_util.copy_tree("game", dir_loc + "/DDLC.app/Contents/Resources/autorun/game")
            break
        elif os_choice == "windows" or os_choice == "Windows":
            try:
                os.mkdir(dir_loc + "\win-mod")
            except OSError:
                shutil.rmtree(dir_loc + "\win-mod", ignore_errors=True)
                os.mkdir(dir_loc + "\win-mod")
            dir_loc = dir_loc + "\win-mod"
            os.remove(dir_loc + "game\scripts.rpa")
            distutils.dir_util.copy_tree("ddlc-pc", dir_loc)
            distutils.dir_util.copy_tre("game", dir_loc + "\game")
            break
        elif os_choice == "linux" or os_choice == "Linux":
            try:
                os.mkdir(dir_loc + "/linux-mod")
            except OSError:
                shutil.rmtree(dir_loc + "/linux-mod", ignore_errors=True)
                os.mkdir(dir_loc + "/linux-mod")
            dir_loc = dir_loc + "/linux-mod"
            os.remove(dir_loc + "game/scripts.rpa")
            distutils.dir_util.copy_tree("ddlc-pc", dir_loc)
            distutils.dir_util.copy_tre("game", dir_loc + "/game")
            break
print ("Installation finished! Enjoy the mod!")

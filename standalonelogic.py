import os
import distutils.dir_util
import shutil

def move_mac():
    distutils.dir_util.copy_tree("mac/", "DDLC-1.1.1-pc")
def standalone_run():
    print("Making the mod standalone")
    print("This is my method of making the mod standalone, be sure to credit me")
    print("Or else...")
    os.chdir('DDLC-1.1.1-pc')
    cwd = os.getcwd()
    f = open(cwd + '/DDLC.py','r')
    lines = f.readlines()
    replace_text= '        return gamedir + "/saves" \n'
    delete_text=''
    lines[49] = replace_text
    lines[50] = delete_text
    f.close()
    f = open('DDLC.py','w')
    f.writelines(lines)
    f.close()
    os.chdir('../')
    cwd = os.getcwd()
    shutil.rmtree(cwd + "/mac")
    shutil.rmtree(cwd + "/DDLC-1.1.1-pc/DDLC.app/Contents/Resources/autorun")

if __name__=='__main__':
    standalone_run()




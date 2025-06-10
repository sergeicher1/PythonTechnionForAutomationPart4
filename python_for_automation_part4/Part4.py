# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | https://www.zero-to-hero.dev/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                                   maintaining your code will be a violent
#                                                       psychopath who knows where you live”
# -- Language                                 | Python
# -- Version                                  | 3.09
# -- Description                              | # This is a sample Python script for Learning Modules #
# -- Modules                                  | # os,time, datetime, shutil,subprocess #
# Usage Example
# For fast show uncomment and run the program
# ------------------------------------------------------------------------------------------------


import os,time, datetime, shutil,subprocess
import ManualModules
from ManualModules import *
from ManualModules import print_hello_world as show_print

''' Functions'''

# Creates, removes, and updates the folder and files and operates with processes
def show_os():
    # /f: Forces termination of the process(es), even if they don’t respond.
    # /im means specify the process by its image name (i.e., the executable filename).

    os.system("taskkill /f /im cmd.exe")
    os.mkdir("c:\shai")
    os.rmdir("c:\shai")
    os.rename("c:\shai","c:\shaiNew")
    os.remove("c:\shai\pingRes.txt")
    os.path.exists("c:\shaiNew")

# Shows start sleeps 5 seconds and shows the end
def show_time():
    print("Start")
    time.sleep(5)
    print("End")


# Shows the time
def show_datetime():
    print(f"The time is: '{datetime.datetime.now()}")


# Operates with files and folders
def show_shutil():
    shutil.copy("c:\\shai\\perf.exe","c:\\data\\perf2.exe")
    shutil.copytree("c:\\shai", "c:\\shai2")
    shutil.rmtree("c:\\shai222")

# Operates with programs and processes
def show_subprocess():
    subprocess.run("ping 8.8.8.8", shell=True)


'''Main Program that calls all the functions'''
if __name__ == '__main__':
    # show_os()
    show_datetime()
    show_time()
    # show_shutil()
    # show_subprocess()
    # ManualModules.print_hello_world()
    # show_print()

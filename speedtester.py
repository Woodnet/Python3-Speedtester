#Speedtest for Windows
#Python 3.7.2 / 2020 /
#Prompt

#Author:
    #Pulsar

import speedtest
import os,time
from colorama import *

os.system("cls")

speedtester = speedtest.Speedtest()
print(Fore.RED + "<" + Fore.YELLOW + "====" + Fore.RED + ">" + Fore.YELLOW + "Speedtest " + Fore.RED + "<" + Fore.YELLOW + "====" + Fore.RED + ">")
print(" ")
print(Fore.RED + "<" + Fore.GREEN + "[01]" + Fore.RED + "> "+ Fore.YELLOW + "Download")
print(Fore.RED + "<" + Fore.GREEN + "[02]" + Fore.RED + "> "+ Fore.YELLOW + "Upload")
print(Fore.RED + "<" + Fore.GREEN + "[03]" + Fore.RED + "> "+ Fore.YELLOW + "Download and Upload")   
print(" ")
print(" ")
usercommand = input(Fore.RED + "<<<Number>>>" + Fore.YELLOW + " ")
print(" ")
print(" ")
print(Fore.YELLOW + "[*]" + Fore.GREEN +" Get best Server..")
speedtester.get_best_server()

if (usercommand != "1" and usercommand != "01" and usercommand != "3" and usercommand != "03" and usercommand != "2" and usercommand != "02"):
    print(Fore.RED + "haha funny.")
    quit()


if (usercommand == "1" or usercommand == "01"):
    speedtester = speedtest.Speedtest()
    print(" ")
    print(Fore.YELLOW + "[*]" + Fore.GREEN +" Testing Download..")
    downloadbytes = speedtester.download()
    downloadmegabytes = downloadbytes / 1048576
    if (downloadmegabytes < 30):
        print(Fore.GREEN + "[" + Fore.RED + "!" + Fore.GREEN + "]" + Fore.YELLOW + " Viel zu wenig DOWNLOAD : " + Fore.RED + "%s Mbps :"%(downloadmegabytes))
    else:
        print(Fore.GREEN + "[+]" + Fore.YELLOW + " DOWNLOAD: " + Fore.GREEN + "%s "%(downloadmegabytes) + Fore.YELLOW + "Mbps")

if (usercommand == "2" or usercommand == "02"):
    print(" ")
    print(Fore.YELLOW + "[*]" + Fore.GREEN +" Testing Upload..")
    uploadbytes = speedtester.upload()
    uploadmegabytes = uploadbytes / 1048576
    if (uploadmegabytes < 10):
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.YELLOW + " Viel zu wening UPLOAD! : " + Fore.RED + "%s Mbps :"%(uploadmegabytes))
    else:
        print(Fore.GREEN + "[+]" + Fore.YELLOW + " UPLOAD: " + Fore.GREEN + "%s "%(uploadmegabytes) + Fore.YELLOW + "Mbps")

if (usercommand == "3" or usercommand == "03"):
    print(" ")
    print(Fore.YELLOW + "[*]" + Fore.GREEN +" Testing Download and Upload..")
    uploadbytes = speedtester.upload()
    uploadmegabytes = uploadbytes / 1048576
    if (uploadmegabytes < 10):
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.YELLOW + "]" + Fore.YELLOW + " Viel zu wening UPLOAD! : " + Fore.RED + "%s Mb :"%(uploadmegabytes))
    else:
        print(Fore.GREEN + "[+]" + Fore.YELLOW + " UPLOAD: " + Fore.GREEN + "%s "%(uploadmegabytes) + Fore.YELLOW + "Mbps")        


    downloadbytes = speedtester.download()
    downloadmegabytes = downloadbytes / 1048576
    if (downloadmegabytes < 30):
        print(Fore.YELLOW + "[" + Fore.RED + "!" + Fore.GREEN + "]" + Fore.YELLOW + " Viel zu wenig DOWNLOAD : " + Fore.RED + "%s Mb :"%(downloadmegabytes))
    else:
        print(Fore.GREEN + "[+]" + Fore.YELLOW + " DOWNLOAD: " + Fore.GREEN + "%s "%(downloadmegabytes) + Fore.YELLOW + "Mbps")

print(" ")
print(" ")
print(Fore.GREEN + "Test abgeschlossen")
print(" ")
print(" ")
enter = input("Press Enter to Exit: ")

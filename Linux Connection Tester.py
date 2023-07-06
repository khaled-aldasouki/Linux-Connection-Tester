#!/usr/bin/env python3


"""
Written By Khaled Aldasouki
Poste   d July 7th 2023
"""


import os #used to run ping commands and clear outputs
from time import sleep #used to give time in between command calls to allow the user time to read output
import subprocess #used to find the default gateway
from sys import platform
def main():

    #will run until the user enters an exit command
    while True:
        
        #ask the uder to choose which service they want to use
        os.system("clear")
        choice = input('\033[96m\
         ***************************************************** \n \
        *****Welcome to the connection test application!***** \n \
        ***************************************************** \n \
            \033[0m1. Default Gateway Test \n \
            2. DNS Resolution Test \n \
            3. Remote Connectivity Test \n \
            4. Display Gateway \n \n \
        Choose one of the options (1-4) or type "q/Q" to quit:  ' ).strip()
        
        #DG test
        os.system("clear")
        if choice == "1":
            print("Testing Default Gateway...")
            sleep(2.0)
            print(check_gateway())

        #DNS test 
        elif choice == "2":
            print("Testing DNS Resolution...pinging www.google.com")
            sleep(2.0)
            print(check_dns())

        #Remote test
        elif choice == "3":
            print("Testing Remote Connectivity...using 129.21.3.17")
            sleep(2.0)
            print(check_remote())

        #quit 
        elif choice == "4":
            print(get_gateway())
        elif choice.upper() == "Q":
            exit()

        #Invalid Choice
        else:
            print("Invalid input, please try again.")
        
        #Give time for the user to read the output 
        sleep(2.0)


def check_gateway():
    #Runs a ping command to check if the gateway can be reached

    DG = subprocess.check_output("ip route | awk '{print $3}' | head -n 1",shell=True).decode('utf-8').strip()
    
    if DG != "virbr0":
        ping = os.system(f"ping -c 1 {DG}> /dev/null")
        if ping == 0:
            return "The connection test to the default gateway\033[96m PASSED"
    return "The connection test to the default gateway\033[93m FAILED"

def check_dns():
    #Runs a ping command to check if the DNS resolution is working
    
    ping = os.system("ping -c 1 www.google.com > /dev/null 2>&1")
    if ping == 0:
        return "The DNS connection test\033[96m PASSED"
    return "The DNS connection test\033[93m FAILED"

def check_remote():
    #Runs a ping command on the RIT DNS server to test remote connectivity
    
    ping = os.system("ping -c 1 129.21.3.17 > /dev/null 2>&1")
    if ping == 0:
        return "The remote connection test\033[96m PASSED"
    return "The remote connection test\033[93m FAILED"

def get_gateway():
    #returns a message dispalying the users default gateway
    DG = subprocess.check_output("ip route | awk '{print $3}' | head -n 1",shell=True).decode('utf-8')

    if  DG.strip() == "virbr0":
        return "You are not connected to a default gateway."
    return f"""Your defualt gateway is {DG}"""

        
if __name__ == '__main__':
    if platform == 'win32':
        print("This tool is designed for Linux systems and cannot be used on Windows")
        sleep(5)
    else:
        main()
            

            

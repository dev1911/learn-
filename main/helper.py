import time
f = open("log.txt","r")
while True:
    time.sleep(0.1)
    linelist = f.readlines()
    print(linelist[-1])
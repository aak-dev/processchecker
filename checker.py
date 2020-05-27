import subprocess
import os
import telegram_send
import time



    
def check_process(name):
    output = []
    cmd = "ps -aef | grep -i '%s' | grep -v 'grep' | awk '{ print $2 }' > /tmp/out"
    os.system(cmd % name)
    with open('/tmp/out', 'r') as f:
        line = f.readline()
        while line:
            output.append(line.strip())
            line = f.readline()
            if line.strip():
                output.append(line.strip())

    return output
while(1):
    p = ["chrome", "Firefox", "Safari"]
    lenght = len(p)
    for i in range(lenght):
        c = check_process(p[i])
        print(c)
        a=[]
        if c <= a:
            print("no bueno"' '+p[i])
            telegram_send.send(messages=["no bueno"' '+p[i]])
        else:
            print("is running"' '+p[i])
            telegram_send.send(messages=["is running"' '+p[i]])
    time.sleep(36)

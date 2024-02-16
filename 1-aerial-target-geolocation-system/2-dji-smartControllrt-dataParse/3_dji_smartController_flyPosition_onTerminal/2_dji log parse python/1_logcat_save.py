import subprocess
import time

while True:
    subprocess.run("adb logcat -d | findstr -i CurrentLocation > idea.log", shell=True)
    time.sleep(1)
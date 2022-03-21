import ftpdeploy
import pycom

pycom.pybytes_on_boot(False)
pycom.heartbeat(False)

from LoRaMeshLibrary.MeshFacade import MeshFacade
from MeshTestConsole import MeshTestConsole
from view.CompositeView import CompositeView
from view.SerialConsoleView import SerialConsoleView
from LoRaMeshLibrary.PycomInterface import PycomInterface

import secrets

from network import WLAN
from MicropythonGitDeploy.gitDeploy import gitDeploy
from MicropythonGitDeploy.DeployServer import DeployServer
import time



wlan = WLAN()
wlan.connect(ssid=secrets.ssid, auth=(WLAN.WPA2, secrets.pwa))
print('connecting..',end='')
while not wlan.isconnected():
    time.sleep(1)
    print('.',end='')

print('connected' + str(wlan.ifconfig()[0]))


filesToKeep=["secrets.py"]
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf', 'LICENSE', "README.md", "OTADeploy.sh"]
gd = gitDeploy("dntoll", "LoRaMeshLoPyConsole", filesToKeep, ignoreUpload)
ds = DeployServer(gd, wlan, 80)

view = CompositeView()
#view.add(RGBView())
view.add(SerialConsoleView())

a = MeshTestConsole(view= view, hardwareInterface = PycomInterface(), meshFacade = MeshFacade(view, MeshTestConsole.callback))
a.run()

print("Release 3")



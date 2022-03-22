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
from MicropythonGitDeploy.wlanhelper import wlanhelper





view = CompositeView()
#view.add(RGBView())
view.add(SerialConsoleView())

a = MeshTestConsole(view= view, hardwareInterface = PycomInterface(), meshFacade = MeshFacade(view, MeshTestConsole.callback))
a.run()

print("Release 6")

#Git Deploy code
filesToKeep=["secrets.py"]
ignoreUpload=[".gitmodules", ".gitignore", 'pymakr.conf', 'LICENSE', "README.md", "OTADeploy.sh", "release_push.py"]
gd = gitDeploy("dntoll", "LoRaMeshLoPyConsole", filesToKeep, ignoreUpload)
wlan = wlanhelper()
ds = DeployServer(gd, wlan, 80)
print(wlan.ifconfig()[0])
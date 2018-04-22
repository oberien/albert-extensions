from albertv0 import *
import os, glob,sys

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Executables"
__version__ = "1.0"
__trigger__ = None
__author__ = "oberien"
__dependencies__ = []

def getExes(start):
    paths = os.environ["PATH"].split(":")
    exes = []
    for path in paths:
        for exe in glob.glob(os.path.join(path, start + "*")):
            if os.access(exe, os.X_OK):
                exes.append(exe)
    return exes

def handleQuery(query):
    if query.string == "":
        return []
    return [Item(
        id=__prettyname__,
        icon="/usr/share/icons/Adwaita/512x512/mimetypes/application-x-executable.png",
        text=os.path.basename(exe),
        subtext=exe,
        completion=os.path.basename(exe),
        urgency=ItemBase.Normal,
        actions=[ProcAction("Execute", [exe])],
    ) for exe in getExes(query.string)]

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from LGMT.utils import load_plugins
import logging
from telethon import events
from . import ALF

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "LGMT/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("LGExt started successfully")
print("Enjoy!")

if __name__ == "__main__":
    ALF.run_until_disconnected()

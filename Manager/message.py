import time
import os


class MessageManager:
    def follow(self):
        logfile = open(
            "C:\\Users\\"
            + os.getlogin()
            + "\.lunarclient\offline\multiver\logs\latest.log",
            "r",
        )
        logfile.seek(0, 2)
        while True:
            line = logfile.readline()

            if not line:
                time.sleep(0.1)
                continue
            if "[Client thread/INFO]: [CHAT]" in line and "BedWars" in line and "has joined" in line:
                yield line.replace("[Client thread/INFO]: [CHAT]", "").split()[3]

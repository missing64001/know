










from threading import Thread

import os

class RunJs(Thread):
    def run(self):
        cmd = r'node mysocket.js'
        os.chdir(r'F:\my\P031_my_blockchain_assets\API-master\sample\nodejs')
        os.system(cmd)

rj = RunJs()
rj.start()







print(1111)
##LINEtoken_kojin:4bgpTkohx371Aryz2hNBL6kKaz01rV0w0vz0zkfgs00
#LINEtoken_kazoku:S75GV3nMEeU4MM9z1hTOT71MXa08Laej2J7n2qwJV37
import requests
import time
import threading 
from socket import *
import numpy as np 
import matplotlib.pyplot as plt

prev_sensor = np. zeros (8)
colors = ['b','r','y','g','c','k','m','#e41a1c']
plot_num = 10 #plotされるセンサ値の数
plot_idx = 0

img_happy = '/home/pi/exp0603/ExpDir/imagefile/happy. JPG'
img_hungry = '/home/pi/exp0603/ExpDir/imagefile/hungry.JPG'

def send_message(msg, pic) :
    token = 'S75GV3nMEeU4MM9z1hIOT7IMXa88Laej237n2qwJV3Z'
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}

    payload = {'message': msg}
    files = {'imageFile' :open(pic, 'rb')}
    a = requests. post(url, headers=headers, params=payload, files=files)

class ReceiveThread(threading. Thread) :
    def __init__(self, PORT=12345) :
        threading. Thread.__init__(self)
        self. data = 'hoge'
        self.kill_flag = False
        # Line information
        self.HOST = "127.0.0.1"
        self.PORT = PORT
        self.BUFSIZE = 1024
        self.ADDR = (gethostbyname (self. HOST), self. PORT)
        # bind
        self.udpServSock = socket (AF_INET, SOCK_DGRAM )
        self.udpServSock. bind (self.ADDR)
        self.received = False

def get_data(self) :
    data_ary = []
    for i in reversed(range (8)):
        num = int(str(self.data[i*8:(i+1)*8]))
        data_ary.append (num/100000)
    self.received = False
    return data_ary

def run(self):
    while True:
        try:
            data, self.addr = self.udpServSock.recvfrom(self.BUFSIZE)
            self.data = data.decode()
            self.received = True
        ехсерсt:
            pass
    
if __name__ == '__main__':
    th = ReceiveThread()
    th. setDaemon (True)
    th. start()
    plt.ion()
    data_b = 0
    count = 0
    gohan = 60*60*12
    start = time. time()

    while True:
        if not th.data:
            break
    
    if th.received:
        senseor_data = th.get_data()
        data_f = sensor_data[3]

        if np.abs(data_f-data_b) > 1.0:
            count += 1
        elif count > 0:
            count -= 1
        
        if count > 3:
            send_message('itadakimasu!', img_happy)
            print ( 'itadakimasu!')
            time. sleep (120)
            count = 0
            start = time.time()
            gohan = 60*60*12

        end = time.time ()

        if (end - start) > gohan:
            send_message('onakasuita...', img_hungry)
            start = time. time()
            gohan = 60*60
            
        datab = data_f

time.sleep (1)

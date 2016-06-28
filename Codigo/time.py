import time, datetime


def timer():
    start = datetime.datetime.now()
    while True:
        tempo = str(datetime.datetime.now()-start)
        print(tempo[:7])
        time.sleep(0.8)

timer()

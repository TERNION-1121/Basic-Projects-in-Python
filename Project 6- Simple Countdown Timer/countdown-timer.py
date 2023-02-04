import time 
import winsound

def annoy():
        for i in range(2, 5):
            winsound.Beep(i * 800, 100)

def countdown(t):
    while t >= 0:
        min, sec = divmod(t, 60)
        print(f"{min:.2f} : {sec:.2f}", end = '\r')
        time.sleep(1)
        t -=1
    annoy()
    print("Time Up!    ")
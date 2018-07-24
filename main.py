import RPi.GPIO as GPIO
import time

# global variable
RIGHT    = 17
LEFT     = 27
FORWARD  = 22
BACKWARD = 5
UP       = 6
DOWN     = 13
RESET    = 19

# look up table
# input channel : output channel
lookup = { RIGHT    : 26,
           LEFT     : 18,
           FORWARD  : 23,
           BACKWARD : 24,
           UP       : 25,
           DOWN     : 12 }

def init():
  # 大家可以在這邊做三件事情
  # 1. setmode()
  # 2. setup()
  # 3. 註冊事件

def exit():
  # 這邊寫好了
  # 當程式要結束時，要記得呼叫這個函式。
  # 把每個腳位的設定回復
  GPIO.cleanup()

def reset():
  print('reset!')
  # 這個函式會把所有輸出都變成LOW，讓所有馬達停下來
  

def move_callback(button):
  print('button {} call back.'.format(button))
  # 這邊要把callback寫出來
  
    
def main():
  # 這邊都寫好了不用改，大家可以盡量看懂在幹嘛
  init()
  while(1):
    print('wait')
    GPIO.wait_for_edge(RESET, GPIO.RISING)
    timeout = GPIO.wait_for_edge(RESET, GPIO.FALLING, timeout=2500)
    if timeout is None:
      break
    reset()
  exit()
  
if __name__=='__main__':
  main()

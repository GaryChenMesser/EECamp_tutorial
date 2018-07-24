import RPi.GPIO as GPIO
import time

# 輸入腳位
RIGHT    = ?
LEFT     = ?
FORWARD  = ?
BACKWARD = ?
UP       = ?
DOWN     = ?
RESET    = ?

# 輸出腳位：大家自己定義

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

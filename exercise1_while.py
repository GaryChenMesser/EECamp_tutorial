import RPi.GPIO as GPIO
import time

# 這個練習沒有規定程式終止的條件，所以程式不會自己停下來
# 用來檢查事件的while可以每檢查一次就休息0.01秒，因為觸發按鈕的最短時間大概是1/10秒的數量級

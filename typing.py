# coding:utf-8

from selenium import webdriver
from time import sleep
import keyboard
from sys import stdout

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-error")
chrome_options.add_argument('--ignore-ssl-errors')

# 配置chromedriver.exe 路径
driver_path = "C:\\Users\\Lion\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe"
browser = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
browser.maximize_window()  # 全屏

browser.get('http://www.zaixiandazi.com')

# 默认打字速度
DEFAULTSPEED = [0.08, 0.13, 0.0893]  # 英文速度0.08 中文速度0.13 数字0.0893


# 菜单
def Menu():
    print("打字模式选择")
    print("1.英文")
    print("2.中文")
    print("3.数字")


# 调整打字速度
def AdjustSpeed(speed):
    if keyboard.is_pressed('up'):       # 上键
        speed -= 0.005
        print("已加快打字速度")
    elif keyboard.is_pressed('down'):   # 下键
        speed += 0.005
        print("已调低打字速度")
    return speed


# 开始打字
def Typing(key):
    print("打字中")
    print("按↑键加快打字速度")
    print("按↓键放慢打字速度")
    print("按q/Q键退出当前打字模式")
    print("切勿打字太快，否则网站会报错")

    speed = 0
    global DEFAULTSPEED

    while True:
        try:
            # 输出文本
            TextOut = browser.find_element_by_id("text-out").text
            # 输入文本
            TextInput = browser.find_element_by_id("text-ipt")

            for text in TextOut:

                TextInput.send_keys(text)

                stdout.flush()
                speed = AdjustSpeed(speed)

                if keyboard.is_pressed('q') or keyboard.is_pressed('Q'):
                    return

                # 控制打字速度
                sleep(DEFAULTSPEED[key - 1] + speed)

        except:
            break


if __name__ == '__main__':

    while True:
        Menu()
        stdout.flush()
        choice = int(input("请选择:"))
        stdout.flush()
        Typing(choice)
        print("打字结束")

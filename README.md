　　本项目是基于python实现的自动打字，测试的打字网链接如下:http://www.zaixiandazi.com/
## 环境依赖
python >= 3.7
浏览器:chrome
依赖 selenium和chromedriver ，第13行配置你的chromedriver路径
## 视频演示
请移步 <a href="https://www.bilibili.com/video/BV17p4y1s7dD">b站链接 </a>
## 已知的bug
1.按键有延迟，也有可能会失灵
2.有时候无法打字，原因不明
## 模式说明
不同的打字模式，我设置了不同的默认打字速度。即使你要打英文文章，选择中文模式或者数字模式，也是无所谓的，不影响。

## 命令行问题
如果在命令行模式下，运行此py文件，有可能会以下提示信息
```
 handshake failed; returned -1, SSL error code 1, net_error -100
```
但是这个不影响此脚本的运行，强烈建议在pycharm里面运行，这样就没有这个提示信息。

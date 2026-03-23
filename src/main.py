#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
个人智能助手小爱 - 跨平台版本
支持：Windows 10/11, Ubuntu 20.04/22.04
作者：Rikka914
"""

import os
import sys
import signal
from utils.platform_tools import get_platform_info,clear_screen

def signal_handler(sig, frame):
    """处理ctrl+C信号"""
    print("\n\n 感谢使用，再见！")
    sys.exit(0)

def main():
    """主程序入口"""
#注册信号处理(Linux需要，Windows可选)
    if get_platform_info()["is_linux"]:
        signal.signal(signal.SIGINT, signal_handler)

#清屏并显示欢迎信息
clear_screen()

print("=" * 50)
print("个人智能助手小爱-跨平台版")
print("=" * 50)
print(f"运行平台:{get_platform_info()['system']}{get_platform_info()['release']}")
print()

try:
    from modules.weather import WeatherAPI

    #初始化管理器
    weather_api=WeatherAPI()

    print("所有模块加载成功!")

except ImportError as e:
        print(f"模块加载失败:{e}")
        print("请确保已安装所有依赖：pip install -r requirements.txt")


#主循环
while True:
    print("\n" + "-" * 30)
    print("1. 🌤️  查看天气")
    print("2. 📝  待办事项")
    print("3. 📒  学习笔记")
    print("4. 💪  随机鼓励")
    print("5. ⚙️  系统信息")
    print("6. ❌  退出")
    print("-" * 30)

    try:
        choice = input("请选择功能 (1-6): ").strip()

    if choice == "1":
        city = input("请输入城市名称（默认北京）: ") or "北京"
        weather_info = weather_api.get_weather(city)
        print(f"\n{weather_info}")


    elif choice == "5":
        from utils.platform_tools import get_platform_info

        info = get_platform_info()
        print(f"\n系统信息：")
        print(f"操作系统：{info['system']} {info['release']}")
        print(f"架构：{info['machine']}")
        print(f"Python版本：{sys.version}")

    elif choice == "6":
        print("感谢使用，再见！")
        break

    else:
        print("无效选择，请重新输入！")

    except KeyboardInterrupt:
        print("\n\n检测到中断，正在退出...")
        break
    except Exception as e:
        print(f"发生错误：{e}")


if __name__ == "__main__":
    main()
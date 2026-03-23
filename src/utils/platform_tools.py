import os
import sys
import platform

def get_platform_info():
    """获取平台信息"""
    system = platform.system()
    release = platform.release()
    machine = platform.machine()
    return{
        "system": system,
        "release": release,
        "machine": machine,
        "is_windows":system=="Windows",
        "is_linux":system=="Linux",
        "is_mac":system=="Darwin",
    }

def get_config_path(config_type):
    """根据平台返回配置路径"""
    plat_info = get_platform_info()
    config_dir = os.path.join(os.path.dirname(__file__),"..","..","config")

    if plat_info["is_windows"]:
        return os.path.join(config_dir,f"windows_{config_type}.json")
    elif plat_info["is_linux"]:
        return os.path.join(config_dir,f"linux_{config_type}.json")
    else:
        return os.path.join(config_dir,f"default_{config_type}.json")


def clear_screen():
    """跨平台清屏"""
    plat_info = get_platform_info()
    if plat_info["is_windows"]:
        os.system("cls")
    elif plat_info["is_linux"]:
        os.system("clear")
    elif plat_info["is_mac"]:
        os.system("clear")  # macOS也使用clear
    else:
        print("不支持的平台，无法清屏")


def open_file_in_explorer(filepath):
    """在文件管理器中打开文件"""
    plat_info = get_platform_info()
    directory = os.path.dirname(filepath)
    if plat_info["is_windows"]:
        os.startfile(directory)
    elif plat_info["is_linux"]:
        os.system(f'xdg-open "{directory}"')
    elif plat_info["is_mac"]:
        os.system(f'open "{directory}"') #macOS使用open命令
    else:
        print(f'无法打开目录:{directory}')
import os
import sys
import platform

def get_paltform_info():
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

def get_config_path(filename):
    """根据平台返回配置路径"""
    plat_info = get_paltform_info()
    config_dir = os.path.join(os.path.dirname(__file__),"..","..","config")

    if plat_info["is_windows"]:
        return os.path.join(config_dir,"windows_config.json")
    elif plat_info["is_linux"]:
        return os.path.join(config_dir,"linux_config.json")
    else:
        return os.path.join(config_dir,"config_config.json")

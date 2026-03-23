import os
import json
from fileinput import filename

from src.utils.platform_tools import get_platform_info

def get_data_dir():
    """获取数据存储目录(平台相关)"""
    plat_info = get_platform_info()

    if plat_info["is_windows"]:
    #Windows:用户AppData目录
        base_dir = os.getenv('APPDATA')
        data_dir = os.path.join(base_dir,"PersonalAssistant")
    elif plat_info["is_linux"]:
    #Linux:用户.home目录
        base_dir = os.path.expanduser('~')
        data_dir = os.path.join(base_dir,"personal_assistant")
    else:
    #其他平台
        data_dir = os.path.join(os.path.dirname(__file__),"..","..","data")
    #创建目录(如果不存在)
        os.makedirs(data_dir, exist_ok=True)
    return data_dir

def save_json(data,filename):
    """保存json数据(自动处理路径)"""
    data_dir = get_data_dir()
    filepath = os.path.join(data_dir,filename)
    with open(filepath,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    return filepath

def load_json(filename,default=None):
    """加载json数据,如果不存在放回默认值"""
    data_dir = get_data_dir()
    filepath = os.path.join(data_dir,filename)

    if not os.path.exists(filepath):
    #如果文件不存在，就返回默认值；但如果没有指定默认值，就返回空字典
        return default if default is not None else {}

    with open(filepath,'r',encoding='utf-8') as f:
        return json.load(f)



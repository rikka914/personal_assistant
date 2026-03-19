import requests
import json

from src.utils.platform_tools import get_config_path

class WeatherAPI:
    def __init__(self):
        """加载平台特定配置"""
        config_file = get_config_path("weather_config")
        with open(config_file,'r',encoding='utf-8') as f:
            self.config = json.load(f)
            self.api_key = self.config.get("api_key","")
            self.base_url = self.config.get("base_url","https://devapi.qweather.com")
import requests
import json
from src.utils.platform_tools import get_platform_info
from src.utils.platform_tools import get_config_path

class WeatherAPI:
    def __init__(self):
        """加载平台特定配置"""
        config_file = get_config_path("weather_config")
        with open(config_file,'r',encoding='utf-8') as f:
            self.config = json.load(f)
            self.api_key = self.config.get("api_key","")
            self.base_url = self.config.get("base_url","https://devapi.qweather.com")

    def get_weather(self,city="北京"):
        """获取天气信息(支持Windows/linux不同API配置,支持中文城市名自动转ID"""
        try:
            #1.如果是中文名，先获取城市ID
            city_id = city
            if not city.isdigit():
                city_id = self._get_city_id(city)
                if not city_id:
                    return f"找不到城市 '{city}',请检查名称或使用城市ID"

            #2.获取天气(使用城市ID)
            url=f"{self.base_url}/v7/weather/now"
            params = {
                "location":city_id,
                "key":self.api_key
            }

            response = requests.get(url,params=params,timeout=10)
            data = response.json()

            if data["code"]=="200":
                return self._format_weather(data["now"],city)
            else:
                return f"获取天气失败:{data.get('message','未知错误')}"

        except requests.exceptions.Timeout:
            return"请求超时，请检查网络"
        except Exception as e:
            return f"获取天气出错: {str(e)}"

    def _get_city_id(self,city_name):
        """通过城市名获取城市ID"""
        try:
            search_url = f"{self.base_url}/geo/v2/city/lookup"
            params = {
                "location":city_name,
                "key":self.api_key,
                "range":"cn",
            }
            response = requests.get(search_url,params=params,timeout=10)
            data = response.json()
            if data["code"]=="200" and data.get("location"):
                #返回第一个匹配城市的ID
                return data["location"][0]["id"]
        except:
            pass
        return None
    def _format_weather(self,weather_data,city):
        """格式化天气信息(平台特定格式化)"""
        plat_info=get_platform_info()

        temp = weather_data["temp"]
        text = weather_data["text"]
        humidity = weather_data["humidity"]
        wind_dir = weather_data["windDir"]
        wind_scale = weather_data["windScale"]

        if plat_info["is_windows"]:
        #Windows使用cmd默认编码,可能需要调整
            return (f"{city}天气：\n"
                    f"温度：{temp}°C\n"
                    f"天气：{text}\n"
                    f"湿度：{humidity}%\n"
                    f"风力：{wind_dir} {wind_scale}级")
        else:
        # Linux终端支持更多Unicode字符
            return (f"🌤️  {city}天气\n"
                    f"🌡️  温度：{temp}°C\n"
                    f"☁️  天气：{text}\n"
                    f"💧 湿度：{humidity}%\n"
                    f"🍃 风力：{wind_dir} {wind_scale}级")
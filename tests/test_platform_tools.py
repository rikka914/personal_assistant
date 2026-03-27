import unittest
import sys
import os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from src.utils.platform_tools import get_platform_info,clear_screen

class TestPlatformTools(unittest.TestCase):
    def test_get_platform_info(self):
        """测试平台信息获取"""
        info = get_platform_info()

        #验证返回的数据结构
        self.assertIn('system',info)
        self.assertIn('release',info)
        self.assertIn('machine',info)
        self.assertIn('is_windows',info)
        self.assertIn('is_linux',info)
        self.assertIn('is_mac',info)

        #验证布尔值类型
        self.assertIsInstance(info['is_windows'],bool)
        self.assertIsInstance(info['is_linux'],bool)
        self.assertIsInstance(info['is_mac'],bool)

    def test_clear_screen_no_error(self):
        """测试清屏函数不报错"""
        try:
            clear_screen()
            self.assertTrue(True) #不报错即通过

        except Exception as e:
            self.fail(f"clear_screen()报错:{e}")

if __name__ == "__main__":
    unittest.main()


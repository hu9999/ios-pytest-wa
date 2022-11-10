# -*- coding: UTF-8 -*-
from uitrace.api import *
from time import sleep
import pytest


class TestClass:
    def setup_class(self):
        """
        每个测试类运行之前执行一次,初始化类
        """
        # 初始化设备驱动和环境，必填
        init_driver(workspace=os.path.dirname(__file__))

    def teardown_class(self):
        """
        每个测试类运行之后执行一次
        """
        # 断开driver
        stop_driver()
        

    def setup_method(self):
        """
        每个用例开始前初始化
        """
        # 启动应用，需要填写应用包名
        start_app("com.apple.Preferences")

    def teardown_method(self):
        """
        每个用例结束后执行
        """
        stop_app("com.apple.Preferences")


    def test_deviceinfo(self):
        slide(loc_from=[0.593,0.894], loc_to=[0.593,0.795], loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)
        click(loc="obj_1667979712317.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
        click(loc="//Cell[@name='关于本机' and @label='关于本机']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        sleep(5)
        
    def test_voice(self):
        click(loc="//StaticText[@name='Sounds' and @label='声音与触感']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        press(DeviceButton.VOLUME_UP)
        press(DeviceButton.VOLUME_UP)
        press(DeviceButton.VOLUME_UP)
        sleep(2)
        press(DeviceButton.VOLUME_DOWN)
        press(DeviceButton.VOLUME_DOWN)




if __name__ == "__main__":
    pytest.main(["-s","test_settings.py"])



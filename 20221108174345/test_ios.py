# -*- coding: UTF-8 -*-
import sys
print(sys.path)
from uitrace.api import *
from time import sleep
import pytest
logger = get_logger()


class TestClass:
    def setup_class(self):
        """
        每个测试类运行之前执行一次,初始化类
        """
        # 初始化设备驱动和环境，必填
        init_driver(workspace=os.path.dirname(__file__))
        start_event_handler()

    def teardown_class(self):
        """
        每个测试类运行之后执行一次
        """
        # 断开driver
        stop_driver()
        print("test class setup..")

    def setup_method(self):
        """
        每个用例开始前初始化
        """
        # press(DeviceButton.HOME)
        


    def teardown_method(self):
        """
        每个用例结束后执行
        """
        # stop_app("com.netease.cloudmusic")
        

    # def test_wy(self):
        # input_text('Secret Garden', xpath=None, timeout=30, depth=10)
        # 测试网易云音乐app
        # start_app("com.netease.cloudmusic")
        # search = click(loc="//NavigationBar[1]/Other[1]/Other[1]/Image[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        # assert search == True
        # sleep(3)
        # input_text('Secret Garden', xpath=None, timeout=30, depth=10)
        # sleep(3)
        # press(66)


    def test_slide(self):
        slide(loc_from=[0.800,0.548], loc_to=[0.085,0.548], loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)
        slide(loc_from=[0.085,0.548], loc_to=[0.800,0.548], loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)



if __name__ == "__main__":
    pytest.main(["-s","test_ios.py"])



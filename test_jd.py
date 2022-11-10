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
        start_app("com.360buy.jdmobile")
        


    def teardown_method(self):
        """
        每个用例结束后执行
        """
        stop_app("com.360buy.jdmobile")
        

    def test_search(self):
        search = click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Other[3]/Image[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        assert search == True
        sleep(3)
        input_text('小米手机', xpath=None, timeout=30, depth=10)
        search = find(loc="//StaticText[@name='搜索' and @label='搜索']", by=DriverType.UI, timeout=5)
        if search is not None:
            click(loc="//StaticText[@name='搜索' and @label='搜索']", by=DriverType.UI, offset=None, timeout=10, duration=0.05, times=10)
        sleep(2)


    def test_slide(self):
        slide(loc_from=[0.926,0.382], loc_to=[0.043,0.382], loc_shift=None, by=DriverType.POS, timeout=30, down_duration=0, up_duration=0, velocity=0.01)
        car = find(loc="obj_1667977766061.jpg", by=DriverType.CV, timeout=20)
        assert car is not None
        sleep(10)
        


if __name__ == "__main__":
    pytest.main(["-s","test_jd.py"])



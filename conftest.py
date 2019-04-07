import pytest
from util.httpUtil import HttpUtil
from common.commonData import CommonData
http=HttpUtil()

@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path="/sys/login"
    data={"userName":CommonData.mobile,"password":CommonData.password}
    resp_login=http.post(path, data)
    CommonData.token=resp_login['object']['token']
    # print("开始测试")

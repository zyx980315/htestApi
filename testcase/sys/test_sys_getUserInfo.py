from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('获取用户信息模块')
class Test_getUserInfo():
	def test_getUserinfo(self):
		data={
		}
		resp=http.post('/sys/getUserInfo',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'获取信息成功')
from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('退出模块')
class Test_Logout():
	def test_login_success(self):
		data={
		'userName':CommonData.mobile,
		'password':CommonData.password
		}
		resp=http.post('/sys/logout',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],"退出成功")
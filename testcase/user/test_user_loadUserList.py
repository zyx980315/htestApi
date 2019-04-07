from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('加载用户列表模块')
class Test_Loaduserlist():
	def test_login_success(self):
		data={
		'userName':CommonData.mobile,
		'password':CommonData.password
		}
		resp=http.post('/sys/login',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		assert resp['object']['userId'] == 115
		print(resp['code'],resp['msg'])
	def test_load_userInfo(self):
		data={
		'pageSize': '30',
		'pageCurrent': '1',
		'nickName': 'zyx',
		'userName':CommonData.mobile
		}
		resp=http.post('/user/loadUserList',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'加载用户信息成功')
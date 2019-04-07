from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('登录模块')
class Test_Login():
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
	def test_login_error_password(self):
		data={
		'userName':CommonData.mobile,
		'password':"123456789"
		}
		resp=http.post('/sys/login',data)
		assert resp['code'] == 410
		assert resp['msg'] == '用户名或密码错误'
		print(resp['code'],resp['msg'])
	def test_login_nouser(self):
		data={
		'userName':"",
		'password':"123456789"
		}
		resp=http.post('/sys/login',data)
		assert resp['code'] == 3010
		assert resp['msg'] == '此账户禁止登录'
		print(resp['code'],resp['msg'])
	def test_login_longuser(self):
		data={
		'userName':"1593515789654123",
		'password':"123456789"
		}
		resp=http.post('/sys/login',data)
		assert resp['code'] == 301
		assert resp['msg'] == '用户不存在'
		print(resp['code'],resp['msg'])

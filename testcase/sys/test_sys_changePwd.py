from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('还原密码模块')
class Test_ChangPwd():
	@allure.feature('修改密码模块')
	def test_changpwd(self):
		data={
		'userId':115,
		'userName':CommonData.mobile,
		'oldPwd':CommonData.password,
		'password':'456789'
		}
		resp=http.post('/sys/changePwd',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'修改密码成功')


	def test_changpwd2(self):
		data={
		'userId':115,
		'userName':CommonData.mobile,
		'oldPwd':'456789',
		'password':'123456'
		}
		resp=http.post('/sys/changePwd',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'密码还原成功')
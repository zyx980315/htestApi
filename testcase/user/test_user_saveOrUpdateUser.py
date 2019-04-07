from common.commonData import CommonData
from conftest import http
import random
import allure
@allure.feature('注册用户模块')
class Test_saveOrUpdateUser():
	def test_saveOrUpdateUser(self):
		nickname = str(random.randint(10000000, 100000000))
		mobile = '159' + nickname
		data={
		'nickName':nickname,
		'userName':mobile,
		"telNo": "",
        "email": "",
        "address": "",
        "roleIds": "",
        "regionId": 1,
        "regionLevel": 1
		}
		resp=http.post('/user/saveOrUpdateUser',data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'注册成功')
		login_data={'userName':mobile,'password':CommonData.password}
		resp=http.post('/sys/login',login_data)
		assert resp['code'] == 200
		assert resp['msg'] == '操作成功'
		print(resp['code'],resp['msg'],'新用户登录成功')

	# def test_load_userInfo(self):
	# 	data={
	# 	'pageSize': '30',
	# 	'pageCurrent': '1',
	# 	'nickName': 'zyx',
	# 	'userName':CommonData.mobile
	# 	}
	# 	resp=http.post('/user/loadUserList',data)
	# 	assert resp['code'] == 200
	# 	assert resp['msg'] == '操作成功'
	# 	print(resp['code'],resp['msg'],'加载用户信息成功')
	#
	# def test_getUserinfo(self):
	# 	data={
	# 	}
	# 	resp=http.post('/sys/getUserInfo',data)
	# 	assert resp['code'] == 200
	# 	assert resp['msg'] == '操作成功'
	# 	print(resp['code'],resp['msg'],'获取信息成功')
"""
if，else等分支语句练习
"""
username = input('请输入用户名： ')
password = input('请输入密码：   ')
#用户名是sunyanxin 密码是dashuaibi则验证成功
if username == 'sunyanxin' and password == 'dashuaibi':
#注意if与else中的‘：’
    print('身份认证成功，欢迎回来，主人')
else:
    print('给爷爪巴')


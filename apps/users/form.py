# -*- coding: utf-8 -*-
# @Time    : 2018/7/11 15:35
# @Author  : dengwangpan
# @File    : form.py
# @Software: PyCharm
# users/forms.py

from django import forms

# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)
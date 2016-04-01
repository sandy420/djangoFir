#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"


class User:
    def __init__(self, username, password, age, sex):
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex

    def tell(self):
        print('UserContext:Name:%s,Pass:%s,Age:%s,Sex:%s' % (self.username, self.password, self.age, self.sex))


class Member(User):
    def __init__(self, username, password, age, sex, user_id):
        User.__init__(self, username, password, age, sex)
        self.user_id = user_id
        print('(AdminUser:%s)' % self.username)

    def tell(self):
        User.tell(self)
        if self.user_id == 1:
            print('This is Administrator!')
        else:
            print('This is User')


t = Member('admin', '123456', '18', '男', 1)
s = Member('jack', '2222', '19', '男', '0')
user_member = [t, s]
for m_user in user_member:
    m_user.tell()

#!/usr/bin/env python3.4
# -*- coding:utf-8 -*-
__author__ = "sandy heng"

class AddressBookEntry(object):
    version = 0.1

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def update_phone(self, phone):
        self.phone = phone


class EmployeeAddress(AddressBookEntry):
    def __init__(self, name, phone, id, social):
        AddressBookEntry.__init__(self, name, phone)
        self.empid = id
        self.ssn = social

if __name__ == '__main__':
    john = AddressBookEntry('john Doe', '400-123-4567')
    print(john.phone)
    john.update_phone('400-888-888-8')
    print(john.phone)
    john.tt = 'mom'
    print(john.tt)

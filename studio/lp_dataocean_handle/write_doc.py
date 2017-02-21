# -*- coding:utf-8 -*-
"""
    License SYPH-L.
    Copyright (c) 2013- SYPH, All Rights Reserved.
    -----------------------------------------------------------
    Author: M.K
    Date: 2017/01/18
    Change Activity:
"""
<<<<<<< HEAD
=======

>>>>>>> 93eae5a35dfbc9189db8c57ec4bcfb3d4da864cd
import os


def get_file_list():
    return os.listdir(os.getcwd())


def write_doc(files_list):
<<<<<<< HEAD
    k = open('../doc.txt', 'w+')
=======
    k = open('../doc.txt', 'a+')
>>>>>>> 93eae5a35dfbc9189db8c57ec4bcfb3d4da864cd
    for file_name in files_list:
        if '__init__' in file_name\
                or '.pyc' in file_name\
                or '.txt' in file_name\
                or 'write_doc' in file_name:
            continue
        base_doc = open(file_name, 'r').read()
        index = base_doc.find('handle(self)')
        temp_doc = base_doc[index:]
        index = temp_doc.find('"""')
        temp_doc = temp_doc[(index + 3):]
        index = temp_doc.find('"""')
        temp_doc = temp_doc[:index]
        useful_doc = ''.join(temp_doc.split(' '))
        head = file_name + '    Document   ----------\n'
        length = len(head)
        k.write('-' * length + '\n')
        k.write(file_name + '    Document   ----------\n')
        k.write(useful_doc + '\n\n')

<<<<<<< HEAD

=======
>>>>>>> 93eae5a35dfbc9189db8c57ec4bcfb3d4da864cd
if __name__ == '__main__':
    file_list = get_file_list()
    write_doc(file_list)

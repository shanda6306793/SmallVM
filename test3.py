#!/usr/bin/env python
# -*- coding: utf-8 -*-

tmp = []
for i in xrange(0,50):
    tmp.append('1')
    
print tmp[0]


a="%x"%(int('a',16)+int('1',16))
print a

tmp_string='tmp12'
print int(tmp_string.split('tmp')[1])

# 函数传值测试，传列表名相当与传递指针
examplelist=[]
examplelist.append(1)


def change(example):
    example[0] = 2
    
change(examplelist)
print examplelist[0]

print 3%4

# coding:utf-8
"""
去重操作，列表，字典，字典嵌套，列表嵌套
"""

# 去除列表内重复的字典，并且输出新列表
a = [{"id":0,"name":"kkk"},{"id":0,"name":"kkk"},{"id":1,"name":"kkk2"},{"id":1,"name":"kkk2"}]
new_a = [dict(t) for t in set([tuple(d.items()) for d in a])]

# 列表去重：并且排序
ids = [1,4,3,3,4,2,3,4,5,6,1]
news_ids = list(set(ids))
news_ids.sort()
# print(news_ids)

# 字典去重，并且按key值排序
t1 = [{'a':1}, {'a':2}, {'a':2}]
# dict([d.items()[0] for d in t1]).items()之外的部分纯粹是把列表内还原成一个字典
t2 = [{value:key} for key, value in dict([d.items()[0] for d in t1]).items()]

# 去重字典内嵌套的列表，输出
t3 = {"a":[1,2,3,4,5,6,2,3,4,2,1,2]}
# print({"a":list(set(t3["a"]))})


# 指定dict值去重：
message_list = [{'count': 1, 'severity': u'WARNING',
                 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes',
                 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1',
                 'latest_time': u'1537950317.31', 'time': u'1537950317.31',
                 'module_name': u'cluster', 'description': u'1/3 mons down, quorum node2,node1'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9', 'time': u'1537950467.9',
                 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950467.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9', 'time': u'1537950467.9',
                 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950437.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'},
                {'count': 1, 'severity': u'WARNING', 'hostname': 'node1', 'latest_time': u'1537950467.9',
                 'time': u'1537950447.9', 'module_name': u'nodes', 'description': u' storage node (node3) is down'}]
l4=[]
# print(message_list[0])
l4.append(message_list[0])
for dict in message_list:
    k=0
    for item in l4:
      if dict['description'] != item['description']:
        k=k+1
      else:
        break
      if k == len(l4):
        l4.append(dict)
print "l4: ",l4
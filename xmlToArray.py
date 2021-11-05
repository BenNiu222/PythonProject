import xml.dom.minidom as xmldom
import os

# strings_dictionary
xmlfilepath = os.path.abspath("strings_dictionary.xml")
# 得到文档对象
domobj = xmldom.parse(xmlfilepath)
# 得到元素对象
elementobj = domobj.documentElement
#获得子标签
subElementObj = elementobj.getElementsByTagName("string-array")
# 获得标签属性值
for obj in subElementObj:
   print (" static  List<MenuItem> get "+obj.getAttribute("name")+"{")
   itemlist = obj.getElementsByTagName('item')
   print("return toMenus(<String> [")
   for item in itemlist:
       print("\""+item.firstChild.data+"\",")

   print("]);")
   print("}")




#
# # -*- coding: UTF-8 -*-
# # 从文件中读取数据
# import xml.etree.ElementTree as ET
#
# # 全局唯一标识
# unique_id = 1
#
#
# # 遍历所有的节点
# def walkData(root_node, level, result_list):
#     global unique_id
#     temp_list = [unique_id, level, root_node.tag, root_node.attrib]
#     result_list.append(temp_list)
#     unique_id += 1
#
#     # 遍历每个子节点
#     children_node = list(root_node)
#     if len(children_node) == 0:
#         return
#     for child in children_node:
#         walkData(child, level + 1, result_list)
#     return
#
#
# # 获得原始数据
# # out:
# # [
# #  #ID, Level, Attr Map
# #  [1, 1, {'ID':1, 'Name':'test1'}],
# #  [2, 1, {'ID':1, 'Name':'test2'}],
# # ]
# def getXmlData(file_name):
#     level = 1  # 节点的深度从1开始
#     result_list = []
#     root = ET.parse(file_name).getroot()
#     walkData(root, level, result_list)
#
#     return result_list
#
#
# if __name__ == '__main__':
#     file_name = 'strings_dictionary.xml'
#     R = getXmlData(file_name)
#     for x in R:
#         print(x)
#     pass
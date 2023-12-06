# 数据类型  6种数据类型
# Number     数值
#      int
#      float
# boolean    布尔
# string     字符串
# list       列表
# tuple      元组
# dict       字典


# 变量类型的基本使用
# Number     数值
#      int
money = 5000
#      float
money1 = 1.2

print(money, money1)

# boolean    布尔
# 流程控制语句
# 性别的变量
# 性别在实际的企业级开发中 使用的单词是sex  gender
# 男  True
sex = True
gender = False
if sex:
    print("sex为", sex)


# string     字符串
# 字符串 使用的是单引号 或者双引号
s = '苍茫的大海上有一只海燕 你可长点心吧'
s1 = "嘀嗒嘀嗒嘀"
print(s, s1)
# 不允许一单一双 屌丝写法
# s2 = '哈哈哈"
# s3 = "呵呵呵'

# 单引号和双引号的嵌套
s4 = '"嘿嘿嘿"'
print(s4)
s5 = "'嘿嘿'"
print(s5)


# list  列表
# 应用场景：当获取到了很多个数据的时候 那么我们可以将他们存储到列表中 然后直接使用列表访问
name_list = ['周杰伦', '科比']
print(name_list)

# 空列表
list1 = []
# 新增元素
list1.append("hello")
list1.append("  ")
list1.append("world")
print(list1)

# 删除元素,两种删除方式
# list1.remove("hello")
# print(list1)
# del list1[0]
# print(list1)

# 遍历list
for i in list1:
 print("序号：%s   值：%s" % (list1.index(i) + 1, i))



# tuple 元组
age_tuple = (18,19,20,21)
print(age_tuple)

# 声明元祖
name_tuple = (1,2,3,4,5,6,7,8)
# name_tuple = (1,)
print(name_tuple)
print(name_tuple[5])
for i in name_tuple:
    print(i)



# dict  字典
# 应用场景：scrapy框架使用
# 格式：变量的名字 = {key:value,key1:value1}
person = {'name':'红浪漫','age':18}
print(person)

# 声明字典,添加元素
name = {}
name["sun"] = person
name["li"] = 3
print(name)

# 删除元素
print(name.get("sun"))
del name["sun"]
print(name)

#遍历元素
name["a"] = 4
name["b"] = 5
name["c"] = 6
for key in name:
    print(key, ":", name[key])


for key in name.keys():
    print(key, '-->', name[key])

for k,v in name.items():
    print(k,">>",v)





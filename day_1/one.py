import math

# 调用数学函数math
print(math.sin(1))

# 返回数值类型
print(type(1))

# 空值类型
dudada=None
dudada="1234564654664"

# 字符串长度（这里整形不能同字符串同时打印）
print("字符串长度"+ str(len(dudada)))
# 字符串索引
print(dudada[5])
print(dudada)

# 多行输出
print("""
      君不见黄河之水天上来，
      奔流到海不复回。
      君不见高堂明镜悲白发
      ........
""")

# input、if\else输入语句
age=int(input("请输入你的年龄:"))
print("你的年龄为="+str(age))
if age >= 18:
    print("已成年")
else:
    print("未成年")





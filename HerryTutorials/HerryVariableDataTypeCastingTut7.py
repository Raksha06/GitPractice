"""
Type is used for pring type of variable
Variable is lika a container for store value
"""
Var1="Raksha"
Var2=7
Var3=32.7
Var4="Test Engineer"
Var5="21"
print(type(Var2))
print(Var2+Var3)
# print(Var1+Var3)
print(Var1+Var4)
print(Var1+Var5)
#typecasting
print(Var2 +int(Var5)) #String Value will convert in int
print(10* "Test Engineer\n")
print(10*str(Var2 +int(Var5)))

# output will display <class 'str or int or float'> for print(type(Var2))
# output will display 39.7 for print(Var2+Var3)
# output will display TypeError: can only concatenate str (not "float") to str for print(Var1+Var3)
# output will display Raksha Test Engineer for print(Var1+Var4)
# output will display Taksha 21 for print(Var1+Var5)
# output will displya 28 for print(Var2 +int(Var5))
# output will display 10 time Test Engineer with new line for print(10* "Test Engineer\n")
# output will display 10 time 28 in str

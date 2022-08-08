# leasso3
name1, name2 = list(input("Введите текс из двух слов:").split())
name1 = str(name1)
name2 = str(name2)
name3 = "{1} {0}".format(name1,name2)
name4 = "{1} {0}".format(name1.upper(),name2.title())
name5 = f"!{name1} {name2}?"
print(name3)
print(name4)
print(name5)
name6=open("tex.txt", "w")
print(f"{name1}<<<>>>{name2}<<<>>>{name3}<<<>>>{name4}<<<>>>{name5}", file=name6)
name6.close()
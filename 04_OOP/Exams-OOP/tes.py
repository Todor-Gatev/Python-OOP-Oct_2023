# from sys import path
#
# print(*path, sep="\n")

# a = 0
# print(a)
# a = 0.0
# print(a)

# a = []
# print(a[-1])

# txt = "     banana     "
#
# print(txt.lstrip())  # banana     "
# print(txt.rstrip())  # "     banana
# print(txt.strip())   # "banana"
# print(txt)           # "     banana     "

# class TestA:
#     def __init__(self):
#         pass
#
#
# test_lst = []
#
# for i in range(7):
#     test_lst.append(TestA())
#
# print(test_lst[1])
# # t = TestA(12)
# # test_lst[1] = t
# print(test_lst)
# # print(t)
# #
# # for obj in test_lst:
# #     if obj == t:
# #         print("yes")

# # b = [1, 2, 3]
# b = []
# a = ["a", *b, "c"]
# print(a)  # ['a', 'c']
# r = "\n".join(str(x) for x in a)
# print(r)

# b = (1, 2, 3)
# print(type(b))
# a = ["a", "c", 'd', 'f']
# a.extend(b)
# print(a)
# c = a[:2]
# print(c)

available_cargos = {'a': 14, 'b': 11, 'c': 3}
# # available_cargos = {}
# cargo_location = max(available_cargos, key=available_cargos.get)
# print(cargo_location)  # b
products = {'z': 100, 'a': 100}
new = {'a': 12}
new.update(available_cargos)
print(new)  # {'a': 10, 'b': 11, 'c': 3}
new.update(products)
print(new)  # {'a': 100, 'b': 11, 'c': 3, 'z': 100}

a = "asd"
b = "jjasdiii"

print(a in b)

z = []
print(z or "None")  # None
z = [12]
print(z or "None")  # [12]

r = [1, 2]
e = [2, 3]
z = (r + e)
print(z)


# fruits = ['apple', 'banana', 'cherry']
# x = fruits.pop(1)
# print(x)  # banana

def test(my_list):
    return (f"asd\n"
            f"asd\n"
            f"back: \n{', '.join(str(x) for x in my_list) or 'none'}")


print(test([1, 2, 3]))
print(test([]))

print(round(1.234, 1))
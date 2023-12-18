# class C(object):
#     classattr = "attr on class"
#     def f(self):
#         return  "function f"
# c = C()
# print(c.__dict__)
# print(c.classattr is C.__dict__['classattr'])
# print(c.f is C.__dict__['f'])


# def foo(): pass
# print(foo.__class__) # покажет класс  к которому принадлежит foo
# print(foo.__dict__) # словарь объекта функции
# # print((42).__dict__) # выдаст ошибку т.к. обект типа int  не имеет атрибута
# print((42).__class__) # но посмотрел класс можно понять какой это тип
#
# class A(object): # созданный класс наследованный от объекта А
#     qux = 'A'
#     def __init__(self, name):
#         self.name = name
#     def foo(self):
#         print('foo')
# a = A('a') #  создание инстанса класса А
# print(a.__dict__)
# print(a.__class__)
# print(type(a))
# print(a.__class__ is type(a))

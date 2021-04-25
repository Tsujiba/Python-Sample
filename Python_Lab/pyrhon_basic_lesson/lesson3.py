"""
#################################################
lesson:Object and Class
"""

"""
class definition
"""
# # (object) or () or nothing
# class Person(object):
#
#     # constractor
#     def __init__(self, name):
#         self.name = name
#
#     def say_something(self):
#         print("My name is {}.".format(self.name))
#         self.run(10)
#
#     def run(self, num):
#         print('run' * num)
#
#     # destructor
#     def __del__(self):
#         print('GoodBye')
#
# person = Person('Yu Tsujibayashi')
# person.say_something()
#
# print("##################################")
#
# del person


"""
class inheritance
super() is parent class
@propaty: getter
@[parameter].setter : setter
*** No _ is acceceble 
*** _ is acceble but indicate you must not access parameter directpry
*** __ is not acceccble out of class but you can acceess in that class or in case of you use getter or setter. 
"""
#
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#
#     def run(self):
#         print('{} run'.format(self.model))
#
#
# class ToyataCar(Car):
#     def __init__(self, model='Lexus', spped='fast'):
#         super().__init__(model)
#         self.speed = spped
#
#     def run(self):
#         print('{} run {}'.format(self.model, self.speed))
#
# class TeslaCar(Car):
#     def __init__(self,
#                  model='Tesla',
#                  enable_auto_run=False,
#                  passwd=123):
#         super().__init__(model)
#         self._enable_auto_run = enable_auto_run
#         self.passwd = passwd
#
#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run
#
#     @enable_auto_run.setter
#     def enable_auto_run(self, is_enable):
#         if self.passwd == '246':
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError
#
# print('###########################')
# car = Car('fit')
# car.run()
# print('###########################')
#
# print('###########################')
# t_car = ToyataCar()
# t_car.run()
# print('###########################')
#
# print('###########################')
# s_car = TeslaCar('Model_S', passwd='246')
# print(s_car._enable_auto_run)
# s_car.enable_auto_run = True
# print(s_car._enable_auto_run)
# print('###########################')

"""
abstract class
1.import abc
2.class AAA(metaclass=ABC.Meta)
3.abstract methood is @abc.abstractmethod
"""
#
# import abc
#
#
# class Person(metaclass=abc.ABCMeta):
#     def __init__(self, age=1):
#         self.age = age
#
#     @abc.abstractmethod
#     def drive(self):
#         pass
#
#
# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
#     def drive(self):
#         raise Exception('No drive!')
#
#
# baby = Baby(2)
# baby.drive()

"""
Multipul inheritance 
"""

# class Person(object):
#
#     def __init__(self, age=18):
#         self.age = age
#
#     def talk(self):
#         print('My age is {}'.format(self.age))
#
# class Car(object):
#     def __init__(self):
#         pass
#
#     def run(self):
#         print('Car run')
#
# # multipul inheritance
# class PersonCarRobot(Person, Car):
#     def __init__(self, age=18):
#         super().__init__(age)
#         pass
#
#     def fly(self):
#         print('fly!')
#
# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()

"""
class variable
class method
static method
"""
#
# class Person(object):
#
#     # class variable(common variable among each object)
#     kind = 'human'
#     my_list = []
#
#     def __init__(self, age=15):
#         self.age = age
#
#     def talk(self):
#         print('My age is {}, and I am {}'.format(self.age, self.kind))
#
#     @classmethod
#     def cls_method_talk(cls):
#         print('Hey', cls.kind)
#
# p1 = Person(18)
# p1.talk()
# p1.my_list.append(1)
# p1.my_list.append(2)
# print(p1.my_list)
# p2 = Person(16)
# p2.talk()
# p2.my_list.append(3)
# p2.my_list.append(4)
# print(p1.my_list)
#
# p3 = Person
# print(p1, p3)
# print(p3.kind)
# p3.cls_method_talk()

"""
special method
"""

# class Person(object):
#
#     def __init__(self, text='AAA'):
#         self.text = text
#
#     def __str__(self):
#         return "I AM HUMAN!!"
#
#     def __len__(self):
#         return len(self.text)
#
# p = Person('BBB')
# print(p)
# print(len(p))

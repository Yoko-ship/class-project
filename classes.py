from typing import Any


class Point:
    color = "red"
    x = 5
    coord = 100

    @classmethod
    def validate(cls,arg):
        return cls.x <= arg <= cls.coord    #? Validate метод может обращаться к атрибутам класса но не к self 
    

    @staticmethod
    def math(x,y):
        return x * x + y * y        #? Это такой вспомогательная функция но внутри класса

    def __init__(self,a,x,y):
        self.a = a   #* атрибут - public
        # self._x = x #*_attribute - protected можем обращаться внутри класса и дочерные элементы (мы все ещё можем обращаться из вне,это некая предупреждения)
        # self.__y = y #* __attribute - private можем обращаться только внутри класса
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls,x): #? Private method
        return type(x) in (int,float)
    

    def set_values(self,x,y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Значение должны быть числами")
    def get_values(self):
        return (self.__x,self.__y)

    def get_print(self):
        return (self.x,self.y)
    

    def __getattribute__(self,item):
        if item == "x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self,item)
        
    def __getattr__(self,item): #* Вызывается тогда когда экземпляр вызывает несуществующий атрибут(таким образом можно избежать error Try Exception)
        return False
a = Point(5,10,12)
a.set_values(4,2)
print(a.get_values())
test = a.color
print(test)


# test = a.validate(10)
# mathem = a.math(10,10)
# print(a.__y) - Ошибка


# print(hasattr(Point,"x")) #? Проверяет на наличие атрибута name в obj
# print(getattr(Point,"color")) #? Возвращает значение атрибута  объекта if not exist => error
# setattr(Point,"car","expensive") #? Задает значение атрибута(Если атрибут не существует он создается)
# delattr(Point,"car") #? Удаляет атрибут


# class Database:
#     __instance = None

#     def __new__(cls,*args,**kwargs): #? Все экземпляры это одно и тоже
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
    
#     def __del__(self):
#         Database.__instance = None

#     def __init__(self,name,user,psw,port):
#         self.name = name
#         self.user = user
#         self.password = psw
#         self.port = port

#     def connect(self):
#         print(f"Успешно подключились к базе данных {self.name}")\
        
    

#     def read(self):
#         return (self.name,self.user,self.password,self.port)
    

# db = Database("Alisa","someone",123,5424)
# db2 = Database("Alisas","someone",123,45424)
# print(db2.read())
# print(db.read())
# print(id(db),id(db2))


# #* Моносостояния
# class MonoThread:
#     __shared_atts = {
#         "data":{},
#         "name":"test"
#     }

#     def __init__(self):
#         self.__dict__ = self.__shared_atts

# class Test:
#     values = {
#         "name":"something"
#     }


# thread = MonoThread()
# thread.name = "testing"
# print(thread.name)
# something = MonoThread()
# print(something.name) #* Моносостояния это когда мы меняя значение в одном из экземпляром, меняем везде(в самом классе)


#? Propery
class Person:
    def __init__(self,name,old):
        self.__name = name
        self.__old = old


    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def get_name(self,name):
        self.__name = name


    def __repr__(self):
        return f"{self.__class__}: {self.__name}"
    

    def __str__(self):
        return f"{self.__name}"
    
    def __len__(self):
        return len(self.__name) #* Создаем метод функции len()'а

    # name = property(get_name,set_name)


person = Person("anya",35)
# print(len(person))
# print(abs(person))
# person.get_name = "someone"

# * Наследования

class Geom:
    name = "geom"

    def set_coords(self,x1,x2,y1,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_coords(self):
        return self.x1,self.x2,self.y1,self.y2
class Line(Geom): #? Наследуем класс Geom(Этот класс теперь является родительский)
    def draw(self):
        print("Drawing")

    

line = Line()
# line.draw()
# line.set_coords(12,12,11,11)
print(issubclass(Line,Geom)) #* Проверка на то является ли класс дочерним другого класса(1ый параметр дочерний элемент,2 родительский)
# print(line.get_coords())



    
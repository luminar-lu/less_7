class Value:
    def __init__(self, num, size = 0,hight = 0):
        self.num = num
        self.hight = hight
        self.size = size
        self.quantity = 0
        
    @property
    def Quantity(self):
        return self.__quantity
        
    @Quantity.setter
    def Quantity(self,num):
        if num == 1:
            self.__quantity = self.size / 6.5 + 0.5
        elif num == 2:
            self.__quantity = self.hight * 2 + 0.3
            
    def get_quantity(self):
        return f'Понадобится {self.quantity}  м. ткани.'
# пальто 1, костюм 2
test_1 = Value(1,size = 45)
test_2 = Value(2,hight=190)
print(test_1.get_quantity())
print(test_2.get_quantity())

# класс Auto
##class Auto:
    # конструктор класса Auto
#     def __init__(self, year):
#         # Инициализация свойств.
#         self.year = year
# 
#     # создаем свойство года
#     @property
#     def year(self):
#         return self.__year
# 
#     # сеттер для создания свойств
#     @year.setter
#     def year(self, year):
#         if year < 2000:
#             self.__year = 2000
#         elif year > 2019:
#             self.__year = 2019
#         else:
#             self.__year = year
# 
#     def get_auto_year(self):
#         return f"Автомобиль выпущен в {str(self.year)} году"
# 
# a = Auto(2090)
# print(a.get_auto_year())

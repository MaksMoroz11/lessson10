class Cat:
    __color = 'Red'

    def get_color(self):
        return self.__color


cat1 = Cat()
print(cat1.get_color())
cat1._Cat__color = 1
print(cat1.get_color())
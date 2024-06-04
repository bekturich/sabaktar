"""
person = []
name = input(':')
age = input(':')

person.append(name) #append кошуп коет эки элементти        #клиент жазган эки нерсени кошуп коюю
person.append(age)

print(person)
"""



"""
cars = ['tesla', 'honda', 'byd', 'bmw', 'audi']

name_of_car = input(":")

if name_of_car in cars:            # ичинде бар же жок экенин таап берет
    print('bar')                   #клиент жазган нерсе бар болсо бар деп чыгат жок болсо жок деп чыгат
else:
    print("jok")
"""



"""
# cars = ['tesla', 'honda', 'byd', 'bmw', 'audi']
#
# name_of_car = input(":")
#
# if name_of_car in cars:                  # ичинде бар же жок экенин таап берет
#     cars.remove(name_of_car)             #remove элементти аты менен очурот
#     print(cars)                          #бул клиент жазган элементти очуруп салат, эгерде туура эмес жазса андай элемент жок деп чыгат
# else:
#     print("andai mashina jok")
"""



"""
cars_1 = ('audi', 'tesla', 'honda', 'byd', 'bmw', 'porsche')
cars_2 = ('tesla', 'hyndai', 'byd', 'audi', 'porsche')
                                                      #эки сеттеги окшош нерселер канча болсо ошончо деп чыгарат
total = set(cars_1).intersection(cars_2)    

print(f'окшош машина {len(total)}')
"""



"""
words = ['potato', 'tomato', 'carrot', 'apple', 'banana']
                                        #листтин ичиндеги элементти жазса ошол элемент канчанчы местада турганын индекси боюнча таап берет
w = input(':')                          #эгерде листте жок элементти жазса андай жок деп чыгат

if w in words:                           # ичинде бар же жок экенин таап берет
    print(words.index(w))                #index канчанчы местада экенин чыгарып берет индекс менен
else:
    print('jok')
"""



"""
numbers_one = [4, 5, 8, 1]
numbers_two = [9, 6, 0, 3]

numbers_one.extend(numbers_two)    #эки листти бириктирип сандарды сорттоп тескерисинен чыгарып койду
numbers_one.sort(reverse=True)
print(numbers_one)
"""



"""
word = input(':').split()            #split ар бир созду озунчо кылып болуп чыгат
print(len(word[-1]))                 #len канча тамгадан турушун санайт -1 тексттеги акыркы санды алат, канча тамга экенин чыгарып берет
"""



"""
word = input(':')

if word == word[::-1]:                          #== барабар болсо            #::-1 тескерисинен чыгарат
    print('polindrom')
else:
    print('polindrom emes')
"""



"""
number = int(input('write number: '))

if number % 2 == 0:                     #эгерде ошол санды экиге болсок, калдыгы нолго барабар болсо жуп сан болот
    print('jup')                        #клиент сан жазса ошол жазылган сан так же жуп экенин чыгарып берет
else:
    print('tak san')
"""



"""
amounts = [600, 455, 544, 545, 223]
                                                  #листтин ичиндеги сандарды кошуп орточо санды табуу
print(sum(amounts)/len(amounts))                  #sum кошуп суммасын чыгарды, len канча элемент бар экенин таап койд
"""



"""
fruits = ['apple', 'banana', 'cherry', 'blueberry']

number = int(input(":"))
if number < len(fruits):               #клиент индекс жазса листтин ичиндеги ошол элементти индекси боюнча очуруп салуу
    del fruits[number]
    print(fruits)
else:
    print('error')
"""



"""
first = [1, 4, 6, 7, 7, 5]
second = [1, 2, 5, 7]             #эки листти бириктирип чонунан кичинекейине карап чыгарып коет
first.extend(second)
print(sorted(list(set(first)), reverse=True))
"""



"""
word1 = input()
word2 = input()
                                           #клиент жазган текст анаграмма же анаграмма эмес экенин табуу
if sorted(word1) == sorted(word2):
    print('анаграмма')
else:
    print('анаграмма эмес')
"""


"""
car_store = {'car_name': 'audi', 'price': 500}
name = input(':')

if name in car_store:                 #эгерде клиент жазган ключ бар болсо ошонун маанисин чыгарып кой
     print(car_store[name])
else:
     print("error")                   #жок болсо жок
"""



"""
summa = float(input("Айландыруу учун сумманы киргизиниз: "))
valuta_kg = input("Баштапкы валютаны киргизиниз(USD, EUR, RUB): ")
valuta_us = input("Максаттуу валютаны киргизиниз (USD, EUR, RUB): ")

valuta = {'USD': 89, 'EUR': 93, 'RUB': 0.94}       
                                                          #мини калькулятор
num = summa / valuta[valuta_us]

print(f"{num}")
"""



"""
baza = { 'ФИО':'', 'Группа':'', 'математика':'', 'история':'' , 'физика':'' }

baza['ФИО'] = input('ФИО:')
baza['Группа']= input('Группа:')
baza['математика']= input('Введите оценку по математике:')
baza['история']= input('Введите оценку по истории:')
baza['физика']= input('Введите оценку по физике:')

print('Студенттин профили')
                                                          #cтуденттин профили
print('ФИО:',baza['ФИО'])
print('Группа студента:',baza['Группа'])
print("Математика:",baza['математика'])
print("История:",baza['история'])
print("Физика:",baza['физика'])
"""



"""
colors = ["красный", "зеленый", "синий"]

for x in colors:                            #ар бир созду алат дагы чонойтуп коет
    print(x.upper())
"""



"""
numbers = [5,6,7,3,5,67,8, 5]

new_list = []

for i in numbers:
    if i == 5:                    #эгерде бизге келген сан барабар болсо 5ке to жаны листке ошол санды кошуп коебуз
        new_list.append(i)
print(new_list)
"""



"""
new_list = []
for i in numbers:
    if i < 0:
        new_list.append(i)                       #0 го барбар же болбосо 0дон кичине сандарды чыгаруу
    elif i == 0:
        new_list.append(i)
print(new_list)
"""



"""
num = int(input(': '))
                                                 #таблица умножения
for i in range(1, 11):
    print(f'{i} * {num} = {i * num}')
"""



"""
    numbers = [6, 7, 3, 65, 23, 8]

    max_number = 0
                                                 #max колдонбой эн чон санды табуу цикл менен
    for i in numbers:
        if i > max_number:
            max_number = i
    print(f"max = {max_number}")
"""



"""
numbers = [6, 7, 3, 65, 23, 8]

min_number = numbers[0]
                                              #min колдонбой эн кичине санды табуу цикл менен
for i in numbers:
    if i < min_number:
        min_number = i
print(f"min = {min_number}")
"""



"""
number = int(input('number: '))                 #10 деп жазсак
                                                #start
print('start')                                  #10
while number != -1:                             #9
     print(number)                              #8
     number -= 1                                #...
else:                                           #0
     print('TheEnd')                            #The End
"""



"""
number = [8, 6, 4, 32]

sum_number = 0
number_index = 0                         #sum колдонбой суммасын табуу цикл менен

while number_index < len(number):
    sum_number += number[number_index]
    number_index += 1
print(f'sum: {sum_number}')
"""



"""
sum_numbers = 0
while True :
     num = int(input(': '))
     sum_numbers += num                    #клиент ар кандай сандарды жазып анан 0 жазса кодду токтотуп анан 0го чейинки сандарды кошуп коет
     if num == 0:
          break
print(sum_numbers)
"""



"""
numbers = [6, 7, 4, 34, -1, 5]

min_number = numbers[0]
i = 1                                            #min колдонбой кичине санды табуу цикл whilе менен

while i < len(numbers):
    if numbers[i] < min_number:
        min_number = numbers[i]
    i += 1

print(f"min: {min_number}")
"""



"""
numbers = [6, 7, 4, 34, -1, 5]

max_number = numbers[0]
i = 1                                            #max колдонбой кичине санды табуу цикл whilе менен

while i < len(numbers):
    if numbers[i] > max_number:
        max_number = numbers[i]
    i += 1

print(f"max: {max_number}")
"""



"""
number = int(input(": "))
total_sum = 0
for i in range(1, number + 1):           #клиент жазган сан 4 болсо ошого чейинки сандарды кошуп суммасын чыгарып коет
    total_sum += i                       #For menen
print(f"Итого: {total_sum}")


number = int(input(": "))
total_sum = 0
i = 1
                                         #клиент жазган сан 4 болсо ошого чейинки сандарды кошуп суммасын чыгарып коет
while i <= number:                       # While menen
    total_sum += i
    i += 1

print(f'Итого: {total_sum}')
"""



"""
word = input('text: ')
number = int(input('number: '))

count = 0                                #клиент текст жазат анан канча жолу чыгышын жазса ошончо жолу чыгат
while count < number:
    print(word)
    count += 1
"""



"""
number1 = int(input('1: '))
number2 = int(input('2: '))

if number1 > number2:
    print(number1)
    while number1 != number2:
        number1 -= 1                         # эгерде клиент 10 анан 1 деп жазса тескерисинен 10дон 1ге чейин жазат
        print(number1)

elif number1 < number2:
    print(number1)
    while number1 != number2:
        number1 += 1
        print(number1)

else:
    print(number1)
"""



"""
import random

one = int(input("Диапазондун томонку чегин киргизиниз: "))
two = int(input("Жогорку диапазонду киргизиниз: "))
randomNum = random.randint(one, two)
sum = 1

while True:
    num = int(input(f'{one} санынан {two} санына чейинки санды табыныз:'))
    if num < randomNum:
        print("Табышмактуу сан чонураак, дагы кайталап корунуз!")
        sum += 1
    elif num > randomNum:
        print("Табышмактуу сан азыраак, дагы кайталап корунуз!")
        sum += 1
    elif num == randomNum:
        print(f'Куттуктайбыз! Сиз {randomNum} санын {sum} аракетте таптыныз')
        break
    else:
        print("Ката жаздыныз")
"""



"""
number1 = int(input('1: '))
number2 = int(input('2: '))

if number1 > number2:
    print(number1)
    while number1 != number2:                 #эгерде 1----5 деп жазса 1ден 5ке чейин санап чыгарат
        number1 -= 1                          #если 6------1 десе обратно санайт
        print(number1)                        #эгерде экоо барабар болсо озун чыгарып коет

elif number1 < number2:
    print(number1)
    while number1 != number2:
        number1 += 1
        print(number1)

else:
    print(number1)
"""



"""
def sum_list(nums,n):
    nums.extend(n)
    return sum(nums)
                                           #эки листти бириктирип бири бирине кошуп суммасын чыгарып коет

print(sum_list([6,7,4,], [4,5,4]))
"""



"""
def check_polindrom(word):
    if word == word[::-1]:
        return 'Polindrom'                 #полиндром же полиндром эмес экенин табуу функция менен
    else:
        return 'Polindrom emes'

print(check_polindrom('LAPTOP'))
"""



"""
def check_numbers(nums):
    return max(nums)
                                              #эн чон санды табуу функция колдонуп

print(check_numbers([6,7,4,745]))
"""



"""
def sort_words(a):
    a = a.split()
    a.sort()
    return a                                             #текстти лист кылып болуп алфавит менен сорттоп коет


print(sort_words('my name is marlen')) # ['is', 'marlen', 'my', 'name']
"""



"""
def delete_duplicate(numbers):
    return list(set(numbers))
                                                       #дубликаттарды очуруп чыгарат

print(delete_duplicate([5, 4, 5, 3, 2, 4, 2]))
"""



"""
def two_numbers(a,b):
    if a > b:
        return f'max: {a}'
    elif a < b:
        return f'max: {b}'
    else:                                    #эн чон санды чыгаруу функция колдонуп, экоо тен болсо анда бироосун чыгарып коет
        return f'max: {a}'

print(two_numbers(7,8))
print(two_numbers(9,9))
print(two_numbers(17,3))
"""



"""
def split_numbers(nums):
    tak =[]
    jup =[]
    for i in nums:
        if i % 2 == 0:                                  # так жана жуп сандарды болуп чыгаруу функция колдонуп
            jup.append(i)
        else:
            tak.append(i)
    return f'Так сандар:{tak}, жуп сандар:{jup}'

print(split_numbers([1,4,5,74,34,64,22,34,10]))
"""


"""
def check_list(numbers):
    if numbers[0] < 0:
        return 0
    elif min(numbers) >= 0:
        return 'Ters san jok'
    
    total = 1                               # эгерде терс сан жок болсо терс жок деп чыгат, бар болсо ошол терс санга чейинки сандарды кобойтуп чыгат, биринчи чыкса 
    for n in numbers:
        if n < 0:
            break
        total *= n
    return total
    
print(check_list([4,5,3,5,2,8,9,0]))
print(check_list([4,5,-3,5,2,8,9,0]))
print(check_list([-4,5,3,5,2,8,9,0]))
"""


"""
def multiply(numbers):
    result = []                            #пустой список
    for i in range(len(numbers)):          
        result.append(i * numbers[i])      #2-тапшырма умножаем элемент на его индекс
    return result
print(multiply([1,2,3,4,5]))
"""



"""
def elements(list1, list2):
    count = 0
    for i in list1:
        if i in list2:                          #3-тапшырма эки листтин ичиндеги окшошторду чыгаруу
            count += 1
    return count

list1 = [1,2,3,7]
list2 = [3,7,4,5]
print(elements(list1, list2))
"""



"""
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}'

class Employer:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}'

person1 = Person('Asan', 33, 'Bishkek', 'KG')
employer1 = Employer('Aidanek', 22, 'Naryn', 'KG')

print(person1.get_info())
print(employer1.get_info())
"""



"""
class Computer:
    def __init__(self, RAM, CPU, Storage):
        self.RAM = RAM
        self.CPU = CPU
        self.Storage = Storage

    def print_data(self):
        return f'RAM: {self.RAM}, CPU: {self.CPU}, Storage: {self.Storage}'

class Laptop(Computer):
    def __init__(self, RAM, CPU, Storage,Model):
        super().__init__(RAM, CPU, Storage)
        self.Model = Model

    def print_data(self):
        return f'RAM: {self.RAM}, CPU: {self.CPU}, Storage: {self.Storage}, Model: {self.Model}'

class Desktop(Computer):
    def __init__(self, RAM, CPU, Storage, Size, Price, count_desk):
        super().__init__(RAM, CPU, Storage)
        self.Size = Size
        self.Price = Price
        self.count_desk = count_desk

    def print_data(self):
        return f'RAM: {self.RAM}, CPU: {self.CPU}, Storage: {self.Storage}, Size: {self.Size}, Price: {self.Price}, count_desk: {self.count_desk}'

    def total_sum(self):
        return f'{self.Price * self.count_desk}'

computer1 = Computer(8,'Intel i3', 256)
laptop1 = Laptop(16, 'Intel i5', 512, 'Acer')
desktop1 = Desktop(32, 'Ryzen 7', 1024, 17, 40000, 6)

print(computer1.print_data())
print(laptop1.print_data())
print(desktop1.print_data())
print(desktop1.total_sum())
"""



"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f'Name: {self.name}, Age: {self.age} '


class Manager(Employee):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def get_data(self):
        return f'Name: {self.name}, Age: {self.age}, Department: {self.department}'

    def check_department(self):
        if self.department == "IT":
            return "COOL"
        else:
            return "NOT COOL"


class Intern(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_data(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

    def total_salary(self):
        return f'{self.salary * 12} som'


employee1 = Employee('Aidana', 22)
manager1 = Manager('Aidar', 32, 'Marketing')
intern1 = Intern('Aibek', 29, 40000)

print(manager1.get_data())
print(employee1.get_data())
print(intern1.get_data())
print(intern1.total_salary())
print(manager1.check_department())

"""



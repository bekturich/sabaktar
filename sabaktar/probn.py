'''
Select * from Customers
Where country = 'USA'           #Америкалыктардын списогу


Select * from Customers
Where age > 25                 #жашы 25тен чондорду чыгаруу


Select * from orders
where customer_id = 3          #ID 3 бардык заказдары


Select * from orders
where item = 'Mouse'           #


select * from customers
where first_name like 'R%n'           #клиенттердин ичинде аты баш тамгасы Р башталып Н буткон адамды табуу

'''


'''
Insert into customers(customer_id, first_name, last_name, age, country)
values(1, 'John', 'Doe', 31, 'USA')
(2, 'Robert', 'Luna', 22, 'USA')
(3, 'David', 'Robinson', 22, 'UK')
(4, 'John', 'Reinhardt', 25, 'UK')
(5, 'Betty', 'Doe', 28, 'UAE')
'''


'''
def polindrom(word):
    if word == word[::-1]:
        return 'Полиндром'
    else:
        return 'Полиндром эмес'

print(polindrom('МАДАМ'))


def sum_list(nums):
    return sum(nums)

print(sum_list([5, 5, 5, ]))


def max_list(nums):
    return max(nums)

print(max_list([4, 55, 6, 7, 8]))
'''
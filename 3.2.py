name = input('enter name: ')
surname = input('enter surname: ')
year = int(input('enter year: '))
city = input('enter city: ')
email = input('enter email: ')
telephone = int(input('input telephone: '))
def my_func (name, surname, year, city, email, telephone):
     return ' '.join(str(x) for x in [name, surname, year, city, email, telephone])
print(my_func(name, surname, year, city, email , telephone))
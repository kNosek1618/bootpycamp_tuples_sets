
# Example of tuple
# tuple can not be changed / modified !!!
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print(type(months)) # <class 'tuple'>

for month in months:
    print(month)

print('\n')

i = len(months) - 1
while i >= 0 :
    print(months[i])
    i -= 1

tuple_in_tuple = (1,2,3,(4,5),6,7)
print(tuple_in_tuple)
# ACCESS TO TUPLE
print(tuple_in_tuple[3][1]) # 5


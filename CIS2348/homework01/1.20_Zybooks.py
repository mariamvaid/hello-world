#Mariam Vaid
#1477614
user_num = int(input('Enter integer:\n'))
print('You entered:' + str(user_num))

squa_num = user_num * user_num
cube_num = squa_num * user_num

print(str(user_num) + ' ' + ' squared is ' + ' ' + str(squa_num))
print('And' + str(user_num) + ' ' + ' cubed is ' + ' ' + str(cube_num) + '!!')

user2_num = int(input('Enter another integer:\n'))

addition = user_num + user2_num
multi = user_num * user2_num

print(str(user_num) + ' ' + ' + ' + str(user2_num) + ' ' + ' is ' + str(addition))
print(str(user_num) + ' ' + ' * ' + str(user2_num) + ' ' + ' is ' + str(multi))

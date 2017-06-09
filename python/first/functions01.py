def greet_user(isim):
    print("merhaba "+str(isim)+"!")
greet_user("ali")


def greet_user_fullname(firstname,lastname):
    print("Hello "+firstname+" "+lastname)
greet_user_fullname("cemal ","süreyya")


def user_dob(day, month, year):
    return str(day)+':'+str(month)+":"+str(year)
birthday = user_dob(day=12, year=1923, month='ocak')
print(birthday)   


# explicitly assigning values to function argument
def greet_user_fullname2(firstname,lastname):
    print("Hello "+firstname+" "+lastname)
greet_user_fullname2(firstname="cem", lastname="sadece")  # use same names of parameters in the function’s definition.


# add optional param by assigning it an empty string.
# optional param can only be listed last in the definition.
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
fullname = get_formatted_name('mehnet', 'neredek')
print(fullname)



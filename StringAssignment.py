"""
Ask the user how many days until their birthday
and print an approximate number of weeks util their birthday

Weeks is = 7 days
decimals within the return is allowed.
"""
days_until_birthday = int(input("How many days until your birthday? "))
print(round(days_until_birthday / 7, 2))

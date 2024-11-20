import keyword

# Allowed Character for defining python identifier
# a to z
# A to Z
# 0 to 9
# _

# Rule 1 : Identifier should not start with any digits
# 123Total // Invalid identifier

x = 10
y = 20
_xy = 30
print(x)
print(y)
print(_xy)

# Rule 2 : Identifier case-sensitive

total = 10
Total = 20
TOTAL = 30
print(total)
print(Total)
print(TOTAL)

# Rule 3 : No length limit for identifier

abcdefghijklmnopqrstwxyz = 100

# Rule 4 : No python reserved words should use as identifier
# def = 100
# 35 Reserved Words
# True, False, None  ==> Values / Reserved Literals
# and, or, not, is
# if, elif, else
# while, for, break, continue, return, in, yield
# try, except, finally, rise, assert
# import, from, as, class, def, pass, global, nonlocal, lambda, del, with
#  async, await

print(keyword.kwlist)

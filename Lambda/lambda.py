def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(10))



# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))
#1
def get_greeting():
  return "Hello from a function"

print(get_greeting())

#2
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


#3
def login_check(is_logged):
    if is_logged:
        return "Welcome!"
    else:
        return "Please login"

print(login_check(False))

#4
def calc(a,b):
   if a>b:
      return a
   else:
      return b
print(calc(5,4))
example_string1 = 'Hello bro'
print(example_string1[0:2], example_string1[7:9], sep='' )
example_string2 = 'jack Is My NAME'
print(example_string2.capitalize())
example_string3 = '*Get rid of stars please*'
print(example_string3.strip('*'))
example_string4 = 'hello my name is jack'
print(example_string4.capitalize().replace('j', 'J'))
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(var2.capitalize() + ', ' + var3.lower(), var1.capitalize())
byte_string = b"\316\273"
print(byte_string.decode())
example_string5 = "It cost me 1000.00$"
money = float(example_string5[11:18])
if money > 500:
    print(True)
elif money < 500:
    print(False)
else:
    print('They`re equal')

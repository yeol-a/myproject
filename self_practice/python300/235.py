def convert_int(string):
    a = string.split(',')
    print(a)
    b = "".join(a)
    print(b)
    
convert_int("1,234,567")
    

'''
def convert_int(string):
    return int(string.replace(',', ''))

print(convert_int("1,234,567"))
'''

from re import L


def print_reverse(string):
    for i in range(len(string)-1, 0, -1):
        print(string[i], end="")
        
print_reverse("python")


def print_reverse(string):
    print(string[::-1])
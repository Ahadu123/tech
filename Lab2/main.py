# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def zad1(text):
    dict = {}
    text = text.lower()
    i = 0
    for character in text:
        if not character in dict:
            dict[character] = 0
        dict[character] +=1
    return dict

def zad2(path):
    f = open(path, "r")
    line_count = 0
    text = ""
    for line in f:
        line1=line.strip("\n")
        text+=line1
    return zad1(text)

def zad3():
    list2 = [666,4,5,6]
    x = min(list2)
    return x



print(zad1("Mariusz to bardzo rzadkie imie"))
print(zad2("Lab2\plik.txt"))
print(zad3())



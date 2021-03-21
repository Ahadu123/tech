# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def lab2_string(text):
    dict = {}
    text = text.lower()
    print(type(dict))
    i = 0
    for character in text:
        if not character in dict:
            dict[character] = 0
        dict[character] +=1
    return dict

print(lab2_string("Mariusz to bardzo rzadkie imie"))


def lab2_file_count(path):
    f = open(path, "r")
    line_count = 0
    text = ""
    for line in f:
        line1=line.strip("\n")
        text+=line1
    print(lab2_string(text))



lab2_file_count("plik.txt")





hash_table = {}
hash_table2 = {}
index = int(0)
#message = input("wczytaj naglowek \n")
path = "Lab3\plik.txt"
f = open(path,"r")
print(f)
for line in f:
    hash_table = f.split("\n")
for i in range(len(hash_table)):
    if not(hash_table[i].startswith(" ")):
        hash_table2[index] = hash_table[i].split(':',1)
        index = index+1
print("Result: \n")
for i in range(index):
    print(hash_table2[i], end = '\n')


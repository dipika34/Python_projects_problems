n = int(input("Enter the elements:"))
my_list = []
search = False

print("Enter the elements of the list:")

for m in range(0,n):
    item = int(input())
    my_list.append(item)
print("The elements of the  list are")

for item in my_list:
    print(item)
target = int(input("Enter the element to search from the list:"))
for item in my_list:
    if(item==target):
        search = True
        break

if(search == True):
    print("Yes,Found",target)
else:
    print("No, Not found",target)

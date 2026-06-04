n = int(input("Enter the elements:"))
my_list = []


print("Enter the elements of the list:")

for m in range(0,n):
    item = int(input())
    my_list.append(item)
max=my_list[0]
print("The elements of the  list are")

for item in my_list:
    print(item)
for item in my_list:
    if(item>max):
        max=item
print("The largest element is",max)

n = int(input("Enter the elements:"))
my_list = []
sum = 0
print("Enter the elements of the list:")

for m in range(0,n):
    item = int(input())
    my_list.append(item)
print("The elements of the  list are")
for item in my_list:
    sum+=item
    print(item,end=" ")
print("\n")
print("The sum of elements of the list are",sum)

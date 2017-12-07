num = input("Enter the number")
count = 0
factor = (len(num) // 2)
for index,dig in enumerate(num):
    if(index < factor):
        if(num[index] == num[index + factor]):
            count += int(num[index])
    else:
        if(num[index] == num[index - factor]):
            count += int(num[index])
print(count)

shopping_list = ["apples", "bananas", "green beans", "turkey"]

with open("shopping_memo.txt", "w") as f:
    for i in range(len(shopping_list)):
        item = shopping_list[i] + "\n"
        f.write(str(i+1) + ": " + item)

with open("shopping_memo.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()) # strip() removes "\n"
        
        # name = input("Enter Your Name : ")
# age = input("Enter your age : ")
# height = input("Enter your Height : ")
# single = input("Are you married ? : ")


# print (str(name))
# print (int(age))
# print (float(height))
# print(bool(single))

# #if you want type should be in 
# print(type(str(name)))
# print(type(int(age)))
# print(type(float(height)))
# print(type(bool(single)))



#overWrite

a = 20
b=5
c= 4
result = a+ b + c + 100

#overwrite
result = a+b+c -100

# if you want integer use // when you divided the int
c = 2 
result = a // b // c   # 20 / 5 / 2 

#serial ### () , * or / which one is come first then  // + or - which come is first 
#()


result = 10 - 9 // 3 * 4 + 2 * 2 - 4
# 10 - 3 * 4 + 2 * 2 - 4
#10 - 12 + 4 - 4
#-2 +  0  === -2
print (result)

f = open('test_file.txt', 'w')
f.write('test text')
f.close()

# import csv

# f = open("employee.csv", "a" , newline="")
# tup1 = ("bob" , 20)
# writer = csv.writer(f)
# writer.writerow(tup1)
# tub2 = ("tun", 30)
# writer.writerow(tub2)
# f.close()

shopping_list = ["apples", "bananas", "green beans", "turkey"]

with open("shopping_memo.txt", "w") as f:
    for i in range(len(shopping_list)):
        item = shopping_list[i] + "\n"
        f.write(str(i+1) + ": " + item)

with open("shopping_memo.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip()) # strip() removes "\n"







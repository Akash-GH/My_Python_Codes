# sort() will print list in ascending order:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
print('\n')
print(colors)
print(num)
print('\n')
# sort(reverse = True) will print list in ascending order:
colors1 = ["voilet", "indigo", "blue", "green"]
colors1.sort(reverse=True)
print(colors1)
print('\n')
num1= [4,2,5,3,6,1,2,1,2,8,9,7]
num1.sort(reverse=True)
print(num1)
print('\n')
#reverse() reverses the order of list. 
colors2 = ["voilet", "indigo", "blue", "green"]
colors2.reverse()
print(colors2)
print('\n')
num2 = [4,2,5,3,6,1,2,1,2,8,9,7]
num2.reverse()
print(num2)
print('\n')
# index() will give the index number of the element put in parenthesis
colors3 = ["voilet", "green", "indigo", "blue", "green"]
print(colors3.index("green"))
print('\n')
num3 = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num3.index(3))
print('\n')
# count() will give the number of ocurrences of the element put in parenthesis.
colors4 = ["voilet", "green", "indigo", "blue", "green"]
print(colors4.count("green"))
print('\n')
num4 = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num4.count(2))
print('\n')
# copy()
colors5 = ["voilet", "green", "indigo", "blue"]
newlist = colors5.copy()
print(colors5)
print(newlist)
print('\n')
# append() elements added at the end
colors6 = ["voilet", "indigo", "blue"]
colors6.append("green")
print(colors6)
print('\n')
# insert() inserts value at particular index number
colors7 = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors7.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors7)
print('\n')
#Concatenating two lists
colors8 = ["voilet", "indigo", "blue", "green"]
colors9 = ["yellow", "orange", "red"]
print(colors8 + colors9)
#extend() add a list to a list
colors10 = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors10.extend(rainbow)
print(colors10)
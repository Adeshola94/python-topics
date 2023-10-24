old_list = [1,2,3,4,5]
new_list = [num + 5 for num in old_list]
print(new_list)

#The difference between json and dict

# Dictionary Comprehension
old_dict = {
    'Abel': 66,
    'Ben': 88, 
    'Caleb': 71
}

new_dict = {key:value + 10 for(key, value) in old_dict.items()}
print(new_dict)

oldDict = {
    'Abel':48,
    'Ben':52,
    'Caleb': 63,
    'David': 44
}
newDict = {key:value + 10 for (key,  value) in oldDict.items() if value >= 50}
print(newDict)

        


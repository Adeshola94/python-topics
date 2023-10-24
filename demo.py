import json
with open('Demo CV.txt', mode = 'w', encoding= 'utf-8')as Bio_info:
    
    Bio_info.write('Name: Bola Brent\nAge: 17\nNationality: Nigerian\nJob: Reverse Engineer\nYear: 2 years')
with open('Demo CV.txt', encoding = 'utf-8') as Bio_Info:
    print(Bio_Info.read())
Bio_Info.closed

bola = {
    'name' : 'john',
    'location' : 'ibadan',
    'strno' : 65
}
print(bola)
with open('Demo CV.txt', mode = 'w', encoding = 'utf-8')as Bio_info1:
    Bio_info1.write = {
    'Name' : 'Bola Brent',
    'Age' : '17',
    'Nationality' : 'Nigeria',
    'Job' : ' Reverse Engineering',
    'Year' : '2 years'
}
with open('Demo CV.txt', encoding = 'utf-8') as Bio_Info1:
    Bio_Info1.closed
    print(Bio_Info1)



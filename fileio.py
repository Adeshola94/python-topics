import json
# javascript object notation
with open('Work CV.txt', mode = 'w', encoding= 'utf-8')as Bio_info: #Bio_info is variable of file work CV.txt

    Bio_info.write('Name: olioxx Brent\nAge: 17\nNationality: Nigerian\nJob: Reverse Engineer\nYoE: 2 years')
with open('Work CV.txt', encoding = 'utf-8') as Bio_Info:
    print(Bio_Info.read())
Bio_Info.closed


with open('Management List.txt', mode='w', encoding='utf-8') as Tamid:
    Tamid.write('Manager: Adewale\nSec: Yetunde\nDriver: Opeyemi\nMarketer: Damilola')
with open('Management List.txt', encoding='utf-8') as Tamid:
    print(Tamid.read())
Tamid.closed

with open('Country Profiler.txt', mode='w', encoding='utf-8') as profiler:
    profiler.write('\nCountry: Norway \n Latitude: 17N 26E')
with open('Country Profiler.txt', encoding='utf-8') as profiler:
    print(profiler.read())
profiler.closed


name = {
        'first' : 'Bob',
        'second' : 'Smith'
    }
rec = {
    'name' : name,
    'job' : ['Dev', 'Mgr'],
    'age' : 40.5
}

print(rec)
#same as print(rec)
#python dictionary is similar to json
print(json.dumps(rec))
myjson = json.dumps(rec)
print(myjson)
ojson = json.loads(myjson)
print(ojson)

json.dump(rec, fp = open('testjson.txt','w'), indent=4)
print(open('testjson.txt').read)


my_dict1 = {'name' : 'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]}
my_dict2 = {
            'data1':{10,30,40},
            'data2':{2,5,6},
            'data3':{45,3,4},
            'data4':{ 'x':111,
                     'y':222
                     }
           }
        
# การเข้าถึงช้อมูลใดข้อมูลหนึง
print(my_dict1['name'])
print(my_dict1[555])
my_dict1['age'] = 50
print(my_dict1)
# อยากแสดงผล 20 ออกมาทำไง
print(my_dict1['wow'][1])
print(my_dict2['data4']['y'])
print(my_dict2)
my_dict2['data5'] = 5555555
print(my_dict2)

# การเข้าถึงทุกข้อมูล 
for xx in my_dict1 :
    print(xx)

print('=======================')
for xx in my_dict1.keyss() :
    print(xx)

print('=======================')
for xx in my_dict1.values() :
    print(xx)

print('=======================')
for xx,yy in my_dict1.items() :
    print(xx ,  '. ', yy)

# Dictionary Method
my_dict1.popitem()
my_dict1.popitem()
my_dict1.popitem()
print(my_dict1)
my_dict2.pop( 'data3')
print(my_dict2)
print(my_dict2.get('data2'))
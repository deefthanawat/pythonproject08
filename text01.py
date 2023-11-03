# ------- Set คือ ช้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้ (หากซ้ำถือว่าเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ และเพิ่ม ลดได้-------
my_set = (10, 20, True, 10, 'SAU', (20, 'IOT'))

# ไม่สามารถที่ จะเข้าถึงข้อมูลใดข้อมูลหนึง
# เข้าถึงทุกข้อมูลใน set 
for data in my_set :
    print (data) 

# การแก้ไข่ Set ทำได้เฉพาะทางเหมือน Tuple
my_list = list( my_set )
print (my_list)
my_list[2] = "Iot"
print(my_list)
my_set = set(my_list)
print(my_set)

# Set Method
my_set.add(999)
my_set.add('wow')
print(my_set)
my_set.pop()
print(my_set)
my_set2 = my_set.copy()
print(my_set2)
my_set.remove(999)
print(my_set)

# Set function
print(len(my_set))
# min(), max()
my_set3 = (10,30, 20 , 0  , 999)
print ( min (my_set3) )
print ( max (my_set3) )

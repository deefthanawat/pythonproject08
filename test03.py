# OP

class Deef_iot :
    # data/property/field/attribute
    major = "sau"
    name = ""



    # method (มันคือ Function แต่เราไม่เรียกฟังก์ชั่น)
    def showHi (self) :
        print('Hi....')

    def introduceMyself(self) :
        print(f'My name is (self.name)')
        print(f'My major is (self.major)')

# ------------
# สร้าง object
obA = Deef_iot( ) #เป็นการเรียกใฃ้ constructor ของคลาสให้ทำงาน (ถ้ามี)
obB = Deef_iot( )

# การใฃ้งาน data ชอง object เอาค่ามันมาใฃ้ หรือเปลี่ยนค่าให้มัน
print ( obA.major )
obA.major = 'move'
obA.name = 'hahaha'
obB.name = 'help!'

# การใฃ้งาน method ของ object คือตั้งให้แสดงผลของ object นั้นๆ
obA.introduceMyself ( )
obB.introduceMyself ( )


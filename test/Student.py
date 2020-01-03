class Student():
    name = ''
    age = 0
    sex = ''

    def print_file(self):
        print("name:" + self.name)

    def introduce(self):
        print("My name is " + self.name + " and my age is " + str(
            self.age) + "and i am a" + ("boy!" if self.sex == '男' else 'girl!'))

student1 = Student()
student1.name = "谢亚茹"
student1.age = 18
student1.sex = "女"

student2 = Student()
student2.name = "张林"
student2.age = 16
student2.sex = "男"


student1.introduce()
student2.introduce()
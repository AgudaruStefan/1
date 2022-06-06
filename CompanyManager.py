class Employee:

    def __init__(self, first_name, last_name, age, job, salary, bonus ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.salary = salary
        self.bonus = bonus

    def __str__(self):
        return f"{self.first_name}\n{self.last_name}\n{self.age}\n{self.job}\n{self.salary}\n{self.bonus}\n"

    def apply_bonus(self,x):
         self.bonus+=x

    def get_totalsalary(self):
        self.salary += self.bonus

class Department:
    def __init__(self, name):
        self.name = name
        self.users = []

    def __str__(self):
        return f"{self.name}\n{self.users}"

    def add_Employee(self,Employee):
        self.users.append(Employee)

    def delete_Employee(self, Employee):
        self.users.remove(Employee)

E1 = Employee('Stefan','Agudaru', 23, 'Python Developer', 3000 ,0)
depart1 = Department('Developers')
depart1.add_Employee(E1)
E1.apply_bonus(500)
E1.get_totalsalary()


print(E1)


print(depart1)
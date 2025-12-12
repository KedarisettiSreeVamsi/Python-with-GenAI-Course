class ChaiAge:
    def __init__(self,age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be between 1 and 5")

chai = ChaiAge(3)
print(chai.age)  # Accessing age using getter
chai.age = 4     # Setting age using setter
print(chai.age)
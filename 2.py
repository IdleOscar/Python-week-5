class Name:
    def __init__(self,first="U",second="R"):
        self.first = first
        self.second = second
    def whatisurname(self):
        print(self.first.capitalize())
        return (self.second.capitalize())
    def ur(self):
        print(self.first.capitalize(), self.second.capitalize())
        return self.first[0].upper() +" ." + self.second[0].upper()
n1 = Name('john','SMITH')
print(n1.whatisurname())
print(n1.ur())
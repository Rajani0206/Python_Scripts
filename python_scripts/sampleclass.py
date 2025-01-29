class example:
    def __init__(self, str1, str2):
        self.var1= str1
        self.var2= str2
        self.var3= "Devops"
   
    def print_value(self):
        print(self.var1, self.var2, self.var3)
	
var= example("Hello", "Welcome")
var.print_value()

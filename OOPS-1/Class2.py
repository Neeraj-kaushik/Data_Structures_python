class Temperature():
    def __init__(self,celcius,farenheit):
        self.celcius=celcius
        self.farenheit=farenheit
    def convertfarenheit(self,celcius):
        return (self.celcius*9/5)+32
    def convertcelcius(self,farenheit):
        return (self.farenheit-32)*5/9
    
celcius=int(input("enter the temperature in celcius"))
farenheit=int(input("enter the temperature in farenheit"))
t1=Temperature(celcius,farenheit)
print(t1.convertcelcius(celcius))
print(t1.convertfarenheit(farenheit))
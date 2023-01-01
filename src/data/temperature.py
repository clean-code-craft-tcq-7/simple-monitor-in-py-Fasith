class Temperature():
    def __init__(self, temperature_unit = "celcius"):
        self.assign_converter_function(temperature_unit)

    def assign_converter_function(self,temperature_unit):
        converter_function_name = f'convert_from_{temperature_unit}'
        converter_function = getattr(Temperature, converter_function_name)
        self.convert_to_celcius = converter_function

    def set_temperature(self,value):
        self.value = self.convert_to_celcius(value)

    @staticmethod
    def convert_from_celcius(value_in_celcius):
        return value_in_celcius

    @staticmethod
    def convert_from_fahrenheit(value_in_fahrenheit):
        value_in_celcius = (value_in_fahrenheit -32)*5/9
        return value_in_celcius

    @staticmethod
    def convert_from_kelvin(value_in_kelvin):
        value_in_celcius = value_in_kelvin - 273.15
        return value_in_celcius      
        

    def __str__(self):
        return f'temperature value in celcius: {self.value}'

    

if __name__ == "__main__":
    t = Temperature(10, 'celcius')
    print(t.value)
    print(t)
    t2 = Temperature(100,"kelvin")
    print(t2.value)
    print(t2)
    t3 = Temperature(100,"fahrenheit")
    print(t3.value)
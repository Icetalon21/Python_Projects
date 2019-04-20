#temp.py

def FahrenheittoCelsius():
    f = float(input("Enter a temperature in Fahrenheit: "))
    conversion = ((f - 32)/1.8)
    print("Temperature in Celsius: ", conversion)

FahrenheittoCelsius()

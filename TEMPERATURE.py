#TEMPERATURE CONVERSION

def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_reaumur(celsius):
    return celsius * 4 / 5


def reaumur_to_celsius(reaumur):
    return reaumur * 5 / 4

print("Temperature Conversion:")
print("1.celsius_to_kelvin")
print("2.kelvin_to_celsius")
print("3.celsius_to_fahrenheit")
print("4.fahrenheit_to_celsius")
print("5.celsius_to_reaumur")
print("6.reaumur_to_celsius")
choice = input("Enter choice (1/2/3/4/5/6): ")
if choice == '1':
    celsius = float(input("Enter temperature in celsius: "))
    kelvin= celsius_to_kelvin(celsius)
    print(f"{celsius}°C is equal to {kelvin:.2f}°K")
elif choice == '2':
    kelvin=float(input("Enter temperature in kelvin: "))
    celsius= kelvin_to_celsius(kelvin)
    print(f"{kelvin}°K is equal to { celsius:.2f}°C")
elif choice == '3':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
elif choice == '4':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
elif choice == '5':
    celsius = float(input("Enter temperature in Celsius: "))
    reaumur = celsius_to_reaumur(celsius)
    print(f"{celsius}°C is equal to {reaumur:.2f}°R")
elif choice == '6' :
    reaumur = float(input("Enter temperature in reaumur: "))
    celsius = reaumur_to_celsius(reaumur)
    print(f"{reaumur}°R is equal to {celsius:.2f}°C")
else:
    print("Invalid input")
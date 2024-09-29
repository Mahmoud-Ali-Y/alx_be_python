FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    temperature = input("Enter the temperature to convert: ")
    while temperature.isdigit() == False:
        print("Invalid temperature. Please enter a numeric value.")
        temperature = input("Enter the temperature to convert: ")
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    match type:
        case "C":
            fahrenheit = convert_to_fahrenheit(int(temperature))
            print(temperature, "°F is ", fahrenheit, "°F")
        case "F":
            celsius = convert_to_celsius(int(temperature))
            print(temperature, "°F is ", celsius, "°C")
    
if __name__ == "__main__":
    main()

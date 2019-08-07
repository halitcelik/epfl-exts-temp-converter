celsius = float(input("please enter the Celsius Value to convert: "))


def temp_converter(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return (
        str(celsius)
        + " degrees Celsius is equal to "
        + str(fahrenheit)
        + "  degrees Fahrenheit."
    )


print(temp_converter(celsius))

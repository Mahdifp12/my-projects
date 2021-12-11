
#? convert celsius to farenheit or farenheit to celsius

def convert_celsius_farenheit(celsius, farenheit):
    """
    This is fuction for convert celsius to farenheit and upside down: 
    
    for example : convert_celsius_farenheit(celsius number, farenheit number)
    """
    
    result_cels = (celsius * 1.8) + 32

    result_faren = (farenheit - 32) / 1.8

    return result_cels, result_faren

converted_cels, converted_faren = convert_celsius_farenheit(100, 212)

# print(f"farenheit: {converted_cels}\tcelsius: {converted_faren}")

help(convert_celsius_farenheit)
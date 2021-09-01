

def complexNumberMultiply(num1, num2):
    if '+-' in num1:
        num1 = num1.replace('+', '')
    num1 = num1.replace('i', 'j')
    if '+-' in num2:
        num2 = num2.replace('+', '')
    num2 = num2.replace('i', 'j')
    num1 = eval(num1)
    num2 = eval(num2)
    num = num1 * num2
    real, imag = int(num.real), int(num.imag)
    return '' + str(real) + '+' + str(imag) + 'i'
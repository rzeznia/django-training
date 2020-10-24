def bmicalculator(weight, length):
    """
    Print person BMI index and status.
    Args:
        weight: person weight in KG
        length: person length in CM
    """
    length /= 100
    bmi = round(weight / length ** 2, 2)
    print("bmi:", bmi)
    if bmi < 16:
        print("niedowaga")
    elif 18.5 <= bmi <= 24.99:
        print("optimum")
    elif 25 <= bmi <= 29.99:
        print("nadwaga")
    else:
        print("otylosc")
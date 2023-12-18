# bmi calculator taking input in feet and inch
print("BMI Calculator - input feet and inch separate")
kg = float(input("Enter your weight in Kgs : "))
feet = int(input("Input feet : "))
inch = float(input("Input inch : "))

#f_mtr = feet * 0.3048
#i_mtr = ( 1.0/12 ) * 0.3048 * inch
#in_meter = f_mtr + i_mtr
height_in_meter = (feet * 0.3048) + ((1.0/12) * 0.3048 * inch)

#bmi calculation
bmi = round((kg / height_in_meter ** 2), 2)
bmi = "{:.2f}".format(bmi)
print(f"Your BMI is : {bmi}")

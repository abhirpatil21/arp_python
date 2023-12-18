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
#bmi = "{:.2f}".format(bmi)
print(f"Your BMI is : {bmi}")

if bmi < 18.5:
    print(f"You are underweight with BMI : {bmi}")
elif bmi < 25:
    print(f"You are normal weight with BMI : {bmi}")
elif bmi < 30:
    print(f"You are slightly over weight with BMI : {bmi}")
else:
    print(f"You are obese with BMI : {bmi}")

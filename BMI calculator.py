# BMI Calculator with python
print("     BMI Calculator")
height = float(input("Enter your height in centimeters:"))
weight = float(input ("Enter your weight in Kgs :"))
height = height/100
BMI=weight/(height*height)
print("Your Body mass Index i: ",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are severely underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: print("You are severely overweight")
else: ("Enter valid details")
        
        
    




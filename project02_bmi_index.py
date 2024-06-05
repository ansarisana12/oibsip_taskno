h=float(input("enter your height in cm:"))
w=float(input("enter your weight in kg:"))
h=h/100

bmi=w/(h*h)
BMI='%2f'%bmi

print(f"your body mass index is:{BMI}")

if bmi>0:
      if bmi<=16:
          print("You are really underweight")
      elif bmi<=18.5:
          print("you are underweight")
      
      elif bmi<=25:
          print("you are healthy")
          
      elif bmi<=30:
          print("you are overweight")
      else:
         print("you are really overweight")
          
else:
    print("enter valid details")
      
  
# Iss program mein hum students ki ginti aur ek student
# ke kharche se hisaab se pure NavGurukul ka ek mahine ka kharcha nikalenge
# input ka use kar ke do values ka input lo:
# Number of students
# Ek student ka kharcha
# Iss ke hisaab se total kharcha nikalein.
# Agar total kharcha 50000 (50 hazar) ya usse kam hai toh print karein 
# "Hum budget ke andar hain" nahi toh print karo ki hum budg

expend=int(input("Enter the number:"))
number=int(input("Enter the number of students:"))
total=expend*number
if total>=50000:
    print("Your expenditure is",total)
else:
    print("It is under budget")

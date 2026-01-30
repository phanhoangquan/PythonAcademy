import math
print("Enter your annual salary: ", end="")
annual_salary = float(input())
print("Enter the percent of your salary to save, as a decimal: ", end="")
porttion_saved = float(input())
print("Enter the cost of your dream home: ", end="")
total_cost = float(input())
##gia tra truoc can nha
portion_down_payment = total_cost*0.25
##so thang
month=int(0)
portion_saved=porttion_saved*(annual_salary/12)
current_savings=portion_saved
monney_bank = float(0)
monney = float(0)
while monney>portion_down_payment:
     month+=1
     monney_bank = ((monney*0.04)/12)
     monney = monney + monney_bank + ((annual_salary/12)*porttion_saved)
print("Number of month: ", month)

    
    
    
    
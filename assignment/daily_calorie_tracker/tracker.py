# Name - Nisha Negi
# Date - 09-10-2025
# Title - Daily Calorie Tracker 

print("---------------------------------------------------------------------")
print("Welcome to Daily Calorie Tracker ")
print("This tool is used to monitor your daily calorie intake. ")

print()

meal_list=[]
calaorie_list=[]

meal=int(input("Enter the number of meals to you had today : "))
print("The meal name includes breakfast, lunch, snacks, dinner. ")

for i in range(meal):
    print()
    meal_name=str(input("Enter the meal name : "))
    calaorie=int(input("Enter the calaorie for the meal : "))
    meal_list.append(meal_name)
    calaorie_list.append(calaorie)
   
total_calaroie=sum(calaorie_list)
av_calaroie= total_calaroie/meal

print("Meal name\tCalaories" )
print("==========================")
for j in range(meal):
    print(f"{meal_list[j]}\t\t{calaorie_list[j]}")
    print()

print()
print(f'total\t\t{total_calaroie}')
print()
print(f'Average\t\t{av_calaroie}')
print()

if total_calaroie >= 1600 and total_calaroie <= 2000 :
    print("WARNING!!")
    print("You have high the calaorie intake. ")
elif total_calaroie >= 1200 and total_calaroie <1600 :
    print("You have the perfect calaorie intake. ")
else:
    print("WARNING!!")
    print("You have low perfect calaorie intake. ") 
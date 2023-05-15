#score = [98, 50, 25, 78, 92]

#print(max(score))
#print(min(score))

score = input("Zadejte skore jednotlivych studentu oddelene carkou a mezerou:\n")

score_list = score.split(", ")
print(score_list)

# prevedeni na cisla
score_list_number = []

for index in range(0, len(score_list)):
    #print(index)
    score_list_number.append (int(score_list[index]))
print(score_list_number)
   
#maximum
#maximum = 0
#for one_number in score_list_number:
    #if one_number > maximum:
        #maximum = one_number
#print(maximum)

#minimum
minimum = 100
for min_number in score_list_number:
    if min_number < minimum:
        minimum = min_number
print(minimum)







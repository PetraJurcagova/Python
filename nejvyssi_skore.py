#score = [98, 50, 25, 78, 92]

#print(max(score))
#print(min(score))

score = input("Zadejte skore jednotlivych studentu oddelene carkou a mezerou:\n")

score_list = score.split(", ")
print(score_list)


score_list_number = []

for index in range(0, len(score_list)):
    #print(index)
    score_list_number.append (int(score_list[index]))
print(score_list_number)
   









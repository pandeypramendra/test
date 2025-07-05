import json

with open('questions.json','r') as file:
    data = json.load(file)
correct_score=0
for i in data:
    print(i['question'])
    for x,y in enumerate(i["options"]):
        print(x+1, "-", y)
    user_input=int(input("Enter your choice: "))
    if user_input==i['correct_answer']:
        correct_score=correct_score+1
        print("great job")
    else :
        print("You choose wrong choice")
        percent_score=correct_score/len(data)*100
print(f"Total Score :{correct_score}/{len(data)}, {percent_score}% answers are correct!")

#print("Enhance your knowledge and take classes regularly")
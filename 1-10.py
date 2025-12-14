
test_results = [
    False, True, False, True, True, 
    True, True, False, True, True, 
    False, True, True, True, False 
]
question_number = len(test_results)
correct_answers = 0
for answer in test_results:
    if answer == True:
        correct_answers += 1

incorrect_answers = question_number - correct_answers
percentage_correct = (correct_answers / question_number) * 100

print('TEST STATISTICS')
print('===============')
print(f"Number of questions: {question_number}")
print(f"Number of correct answers: {correct_answers}")
print(f"Number of incorrect answers: {incorrect_answers}")
print(f"Percentage of correct answers: {percentage_correct:.2f}%")
import re

with open('input.txt','r') as file:
    text = file.read()

def correct_format(text):
    # mul(x,y)
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    return re.findall(pattern,text)
    
def Sum_Of_All(valid_input):
    result = 0
    for i,j in valid_input:
        result += int(i) * int(j)
    return result

valid_input = correct_format(text)

total_res = Sum_Of_All(valid_input)

# print(valid_input)
print(total_res)

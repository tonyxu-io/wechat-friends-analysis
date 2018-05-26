import itchat
import json
from json2table import convert

# Login to WeChat and Scan the QR Code
itchat.login()

# Get JSON reponse of WeChat friends
friends = itchat.get_friends(update=True)[0:]
# print(json.dumps(friends,indent=4))

# Define a function to get data, return list arr
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
Sex = get_var('Sex')

# Init and Count
male = female = other = 0
for sex in Sex:
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# Sum
total = len(friends)
maleRate = float(male)/total*100
femaleRate = float(female)/total*100
otherRate = float(other)/total*100
print('Male: %d, Percentage: %.2f%%' % (male, maleRate))
print('Female: %d, Percentage: %.2f%%' % (female, femaleRate))
print('Others: %d, Percentage:%.2f%%' % (other, otherRate))

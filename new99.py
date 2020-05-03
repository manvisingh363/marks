#!/usr/bin/python3
print("content-type: text/html")
print()
html = '''
<html>
<form>
<h3>Gender</h3>
<b> Male</b>
<fieldset id="group1">
    <input type="radio" value="value1" name="group1">Yes
    <input type="radio" value="value2" name="group1">No
</fieldset>

<b> female</b>
<fieldset id="group2">
    <input type="radio" value="value1" name="group2"> Yes  
    <input type="radio" value="value2" name="group2"> No
</fieldset>
<h3>Test Prepartion</h3>
<b> None</b>
<fieldset id="group3">
    <input type="radio" value="value1" name="group3">Yes
    <input type="radio" value="value2" name="group3">No
</fieldset>
<b> Complete</b>                                                                                                                                                <fieldset id="group4">
    <input type="radio" value="value1" name="group4">Yes                        
    <input type="radio" value="value2" name="group4">No 
</fieldset>
<h3> lunch</h3>
<b> Standard</b>                                                                                                                                                <fieldset id="group5">
    <input type="radio" value="value1" name="group5">Yes                            <input type="radio" value="value2" name="group5">No                         </fieldset>

<b>free/reduced</b>
<fieldset id=group6>    
    <input type="radio" value="value1" name="group6">Yes
    <input type="radio" value="value2" name="group6">No
</fieldset>    
<input type="submit" />
</form>
</html>
'''
print(html)

import cgi

data = cgi.FieldStorage()
#print(data)
#print("<br><hr><br>")

one = data['group1'].value
two = data['group2'].value
three= data['group3'].value
four = data['group4'].value
five= data['group5'].value
six = data['group6'].value

#print(one, two,three,four,five,six)

# for one
if one == 'value1':
    one = 0
elif one == 'value2':
    one = 1

#for two
if two == 'value1':
    two = 0
elif two == 'value2':
    two = 1
#for three
if three == 'value1':
    three = 0
elif three == 'value2':
    three = 1
#for four
if four == 'value1':
    four = 0
elif four == 'value2':
    four = 1
#for five    
if five == 'value1':
    five = 0
elif five == 'value2':
    five = 1
#for six
if six == 'value1':
    six = 0
elif six == 'value2':
    six = 1


# printing values
#print(one, two, three, four, five, six)

l = [one, two, three, four, five, six]
#print(l)
#load model
import joblib
#print(11223)
model = joblib.load("projectt.kpl")
#print(1234)
# predict from model
pred = model.predict([l])
#print(l)
#print the output
print(" Prediction", pred)


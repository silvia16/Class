
end=int(input ("enter the ending limit:"))

print ("kph\t mph")
print("--------------")
for kph in range (60,end+1,10):

    mph=kph * 0.6214

    print(kph,'\t', format(mph,'.0f'))

    

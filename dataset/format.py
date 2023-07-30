with open('HSK6.txt', 'r') as file:
    data = file.read() #.replace('', '')

#print(data)

array = list(data.strip())
#insert new line at start so logic will work
#print(array)


firstnewline = False
for i, s in enumerate(array):
    

    if s == "\n" and firstnewline:
        first = s = "\":\""
        last = "("
        count = 1
        while True:
            #print(array[i-count])
            if array[i-count] == "\n":
                break
            else:
                count = count + 1
                
            
        #print(count) amount of ch char is count-1
        
        count = count - 1
        
        mid = ""
        while count >= 1:
            mid = mid + array[i-count]
            count = count - 1
        #print(mid)
        array[i] = first + mid + last


        #s = "\":\""+array[i-1]+"("
        #print(s)
        firstnewline = False
    else:
        if s == "\n" and not firstnewline:
            firstnewline = True
            #array[i] = "\""
            #array[i+1] = array[i+1] + "\""
            


    if s == "\t":
        array[i] = "), "



#print(array)

string = "".join(str(x) for x in array)
array = string.split("\n")
for i, s in enumerate(array):
    array[i] = "\"" + array[i] + "\","
    
string = "\n".join(str(x) for x in array)
print(string)



sum = 0
input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
if a>0:
    for i in range(1,a+1):
        sum += i
elif a<=0:
    for i in range(1,a+1):
        sum+=i
output_data = open("output.txt","w")
data = output_data.write()
input_data.close()
output_data.close()

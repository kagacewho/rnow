input_data = open('input.txt', 'r') 
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
r = 0
if a>b and a>c:
    r=a
elif b>a and b>c:
    r=b
else:
    r=c
output_data = open('output.txt', 'w')
output_data.write(str(r))
input_data.close()
output_data.close()
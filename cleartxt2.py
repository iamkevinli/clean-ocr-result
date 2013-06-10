import sys
temp=sys.argv
filename = temp[1]
print temp
print filename

exit

f = open (filename,"r")

#Read whole file into data
data = f.read()

out = ""
laste = " "
string = "Special $#! characters   spaces 888323"
for e in data:
	if not e.isalnum():
		e = " "
	if e == " " and laste == " ":
		temp=""
	else:
		out += e
	laste = e

print out
# Close the file
f.close()
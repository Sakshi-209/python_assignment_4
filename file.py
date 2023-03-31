#using read
file=open("file.txt")
data=file.read()
print(data)
file.close()

#using readline
file=open("file.txt")
a=file.readline()
print(a)
file.close()

#write the file
file=open("file.txt",'w')
data=file.write("HI I AM SAKSHI")
print(data)
file.close()

#append the file
file=open("file.txt",'a')
file.write(" Welcome Onboard")
file.close()
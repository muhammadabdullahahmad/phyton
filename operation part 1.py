# open file and read its contents 
file = open ('condingal.txt','r')
print (file.read())
file.close()
#open file and read its begining 8 charctor
file = open ('condingal.txt','r')
print("/n read in parts /n")
print(file.read(8))
file.close()
# apend your name and age  in  the file
file = open ('condingal.txt','r')
file.write("hi! i am  penguin and i am ten yera old")

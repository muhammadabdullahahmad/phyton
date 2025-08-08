#open file in read mode
file = open ('condingal.txt','r')
print("file in read mode")
print(file.read())
file.close()
#file in write mode
file_write = open('condingal.txt','w')
file_write.write("file in write mode ")
file_write.write("hi iam a penguin iam in grade 3")
file.close()
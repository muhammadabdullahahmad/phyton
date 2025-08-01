file = open ('condingal.txt')
print (file.read())
file.close()
file_read = open ('condingal.txt','r')
print ("file in read mode -")
print ("file_read.read()")
file_read.close

file_write = open ('condingal.txt','w')
file_write.write("file in write mode")
file_write.write("hi ! my favourite animal is cat")
file_write.close

file_append = open ('condingal.txt','a')
file_append.write("file in append mode")
file_append.write("hi ! i am cat i am 3 months old")
file_append.close






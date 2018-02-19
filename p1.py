# # -*- coding: utf-8 -*-
# # @Author: surakum2






# # @Date:   2017-11-07 19:10:46
# # @Last Modified by:   surakum2




# # @Last Modified time: 2017-11-23 22:40:14
# # import io,os
# # print("hello, i am p1")
# # def generate_p2():
# # 	with io.FileIO("sk.py", "w") as file:





# # 		file.write(b"def say_hello(): \\n \\tprint('hello') \\ndef say_world(): \\n \\tprint('world') \\nif __name__ == '__main__': \\n \\tsay_hello() \\n \\tsay_world()")
# # if __name__ == '__main__':
# # 	generate_p2()
# # 	os.system("python sk.py")
# import io,array





# with open('p2.py','r') as f:
#     with open("p3.py", 'w+') as f1:
#         for line in f:
#         	b = bytearray()
# 			b.extend(map(ord, line))
#         	if 'tests/file/myword' in b:
#         		f1.write(line)

# # with open('out.py', 'a') as f1:
# #     for line in open('sk.py'):
# #         if 'tests/file/myword' in line:
# #             f1.write(line)


#open("out.py", "w").writelines([l for l in open("sk.py").readlines() if "tests/file/myword" in l])


# import io,os
# with open("p2.py") as f:
#     lines = f.readlines()
#     lines = [l for l in lines if "ROW" in l]
#     with open("p3.py", "w") as f1:
#         f1.writelines(lines)              
# i=1
# with open('p3.py', 'w+') as output, open('p2.py', 'r') as input:
#     while True:
#         data= input.readlines()
#         if data == '':  # end of file reached
#             break
#         print(i)
#         print(data)
#         i+=1
#         output.write(data) 
import re
with open('p3.py', 'w+') as output, open('p2.py', 'r') as f:
	while True:
		data = f.read(100000)
		if data == '': # end of file reached
			break
		output.write(data)
f.close()
output.close()
#with open('p3.py','w') as f:
for line in open('p3.py','r+'):
	print(type(line))
	line.replace('HelloWorld','NewPreviewPlugin')
	line.replace('IHelloworld','INewPreview')
	break
	#re.sub(['HelloWorld'], 'NewPreviewPlugin', line)
	#re.sub(['IHelloWorld'], 'INewPreview', line)
#text2 = f.readline()
#text2 = re.sub('IHelloWorld', 'INewPreview', text)
#with open('new01.py', 'wb') as newfile:


#vfdvfdvfdvfvfvfdvfdv
#vfdvfdvfvfdv
#vvcdvcdvcdv


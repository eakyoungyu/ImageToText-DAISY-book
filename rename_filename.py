# 이미지 파일을 renumbering함
import os

# 수정 해야함
input_path = os.path.join(os.path.join(os.path.dirname(__file__), "_image"), "seveneves2")
output_path = os.path.join(os.path.join(os.path.dirname(__file__), "_image"), "seveneves")

print(input_path)
print(output_path)

for file_name in os.listdir(input_path):
	if(len(file_name)==11):
		num = int(file_name[:3])
		sec_num = int(file_name[5:6])-4
		new_file_name = str(num*2+sec_num)+".jpg"
		print(new_file_name)
		os.rename(input_path+'\\'+file_name,
		 output_path+'\\'+new_file_name)
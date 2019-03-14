import io
import os
# 덮어쓰기(이어쓰기X)
def merge(outpath, page_dir, start, end):
	with io.open(outpath, 'w', encoding='UTF-8') as text_file:
		for file_name in range(start, end+1):
			page_path = os.path.join(page_dir, str(file_name)+".txt")
			with io.open(page_path, 'r', encoding='UTF-8') as page_txt:
				data = page_txt.read()
				# 빈 면 처리
				if data == "@@p"+str(file_name)+'\n':
					data+="빈 면\n"
				text_file.write(data)
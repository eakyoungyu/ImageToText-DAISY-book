# -*- coding:utf-8 -*-
import io
import os
import json
import sys

from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
from pykospacing import spacing


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
# 같은 이미지 파일에 대한 중복 요청이 없도록 함
def my_detect_document(input_path, output_path, page_num):
    if os.path.isfile(output_path):
        print("이미 존재하는 파일입니다")
        return
    else:
        print("api 호출")
        detect_document(input_path, output_path, page_num)

def detect_document(input_path, output_path, page_num):
    client = vision.ImageAnnotatorClient()
    with io.open(input_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.types.Image(content=content)
        # response: json
        response = client.document_text_detection(image=image)

    with io.open(output_path, 'w', encoding='UTF-8') as text_file:
        # 페이지 번호 표시
        text_file.write('@@p'+str(page_num)+'\n')
        print(response.full_text_annotation.text)
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    par_word = ''
                    prev_word = ''
                    is_lineWrappingBreak = False
                    for word in paragraph.words:
                        cur_word = ''
                        for symbol in word.symbols:
                            par_word+=symbol.text
                            cur_word+=symbol.text
                            break_type = symbol.property.detected_break.type
                            if break_type == 3:
                                is_lineWrappingBreak = True
                                prev_word = cur_word
                            elif break_type == 1:
                                if is_lineWrappingBreak == True:
                                    prev_idx = par_word.rfind(prev_word)
                                    unSpaced = par_word[prev_idx:]
                                    par_word = par_word[:prev_idx]
                                    cur_word = spacing(unSpaced)
                                    is_lineWrappingBreak = False
                                    par_word += cur_word
                                par_word += ' '
                    # 페이지 번호가 인식될 수 있다
                    if par_word != str(page_num):    
                        text_file.write(par_word)
                        text_file.write('\n')
def main():
	# 책 이름
	book_name = "testbook"

	# 시작 페이지, 마지막 페이지
	start_file = 13
	end_file = 17

	# 이미지 폴더
	IMG_DIR = os.path.join(os.path.dirname(__file__), "_image\\"+book_name)
	# 각 페이지 텍스트 파일을 저장할 폴더
	PAGE_DIR = os.path.join(os.path.dirname(__file__), "_txt_page\\"+book_name)
	# 책 전체 내용을 저장할 폴더
	BOOK_DIR = os.path.join(os.path.dirname(__file__), "_txt_book")
	# 책 전체 텍스트 파일 이름
	book_path = os.path.join(BOOK_DIR, book_name+".txt")

	for file_name in range(start_file, end_file+1):
		page_path = os.path.join(PAGE_DIR, str(file_name)+".txt")
		img_path = os.path.join(IMG_DIR, str(file_name)+".jpg")
		# GOOGLE VISION 호출
		my_detect_document(img_path, page_path, file_name)

	# 파일 합치기
	merge(book_path, PAGE_DIR, start_file, end_file)
	

os.system ('set GOOGLE_APPLICATION_CREDENTIALS=C:\\2K\\workspace\\python-workspace\\imagetotext\\key\\ImageToText-031ec8fa0132.json')
print('++++SET++++')
os.system('echo GOOGLE_APPLICATION_CREDENTIALS')
if __name__ == "__main__":
    main()
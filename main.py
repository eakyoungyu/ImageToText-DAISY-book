# -*- coding:utf-8 -*-
from img_to_txt import *
from merge_txt import *
import os

# 책 이름
book_name = "YOUR_BOOK_NAME"

# 시작 페이지, 마지막 페이지
start_file = 0
end_file = 999

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
	

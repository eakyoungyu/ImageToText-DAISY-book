# -*- coding:utf-8 -*-
import io
import os
import json

from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
from pprint import pprint
from pykospacing import spacing

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
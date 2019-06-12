# ImageToText-DAISY-book
시각 장애인을 위한 전자도서 제작봉사 프로그램

# 기능
책을 스캔한 이미지를 인식하여 텍스트 파일로 변환합니다.

# 사용한 API & Library
- Google Vision: https://cloud.google.com/vision/docs/ocr?hl=ko
- kospacing: https://github.com/haven-jeon/PyKoSpacing

# 개발 환경
- python 3.6.8
- tensorflow 1.6.0

tensorflow 1.6.0을 설치할 때, 아래의 두 가지 방법 중 하나를 선택
```
pip install tensorflow==1.6.0
pip install https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.6.0-cp36-cp36m-win_amd64.whl
```

kospacing & google vision 설치
```
pip install keras
pip install git+https://github.com/haven-jeon/PyKoSpacing.git
pip install --upgrade google-cloud-vision
```


# 제작 과정
https://y2k2.tistory.com/2

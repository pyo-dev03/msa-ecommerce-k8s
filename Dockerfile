# 1. 베이스 이미지 선택 (Python 3.8 슬림 버전)
FROM python:3.8-slim

# [추가] Python 로그가 버퍼링 없이 즉시 출력되도록 설정
ENV PYTHONUNBUFFERED = 1

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 파일을 컨테이너의 /app/으로 복사
COPY requirements.txt .

# 4. 복사된 파일을 이용해 라이브러리 설치
RUN pip install -r requirements.txt

# 5. 현재 폴더의 모든 파일을 컨테이너의 /app/으로 복사
COPY . .

# 6. 컨테이너가 시작될 때 실행할 명령어
CMD ["python", "app.py"]
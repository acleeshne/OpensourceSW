# 베이스 이미지 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일들을 복사
COPY requirements.txt /app/

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일들을 복사
COPY . /app/

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=mytodolist.settings
ENV PYTHONUNBUFFERED=1

# Django 서버 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


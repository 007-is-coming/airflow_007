# Airflow의 최신 이미지 기반
FROM apache/airflow:2.10.3

# root 사용자로 전환
USER root

# 필요한 패키지 설치 및 정리
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# airflow 사용자로 다시 전환
USER airflow

# 필요한 Python 패키지 설치
RUN pip install --no-cache-dir \
    psycopg2-binary \
    spotipy \
    apache-airflow==2.10.3 \
    pandas \ 
    csv
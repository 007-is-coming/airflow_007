# airflow의 가장 최근 이미지
FROM apache/airflow:2.10.3

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
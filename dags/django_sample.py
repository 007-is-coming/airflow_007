
'''
view.py
'''

from django.http import JsonResponse
from django.shortcuts import render
import requests

# Airflow API 설정
AIRFLOW_HOST = "http://localhost:8080"  # Airflow 웹 서버 URL
DAG_ID = "your_dag_id"  # 트리거할 DAG의 ID

def trigger_dag(request):
    if request.method == "POST":
        # Airflow API 엔드포인트에 POST 요청 보내기
        response = requests.post(
            f"{AIRFLOW_HOST}/api/v1/dags/{DAG_ID}/dagRuns",
            json={},  # 여기에 필요한 추가 파라미터나 데이터가 있다면 추가
            auth=("username", "password")  # 인증이 필요하다면 추가
        )

        if response.status_code == 200:
            return JsonResponse({"status": "success", "message": "DAG triggered!"})
        else:
            return JsonResponse({"status": "error", "message": response.text})
    return JsonResponse({"status": "error", "message": "Invalid request"})


'''
url.py
'''

from django.urls import path
from . import views

urlpatterns = [
    path('trigger-dag/', views.trigger_dag, name='trigger_dag'),
]


'''
trigger_dag.html
'''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trigger DAG</title>
    <script>
        function triggerDag() {
            fetch('/trigger-dag/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('DAG triggered successfully!');
                } else {
                    alert('Error: ' + data.message);
                }
            });
        }
    </script>
</head>
<body>
    <button onclick="triggerDag()">Trigger DAG</button>
</body>
</html>


'''
httphook
'''

from airflow.hooks.http_hook import HttpHook
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def call_api():
    http = HttpHook(method='GET', http_conn_id='my_http_connection')
    response = http.run('your_api_endpoint')  # 'your_api_endpoint'는 API 경로 
    '''
    Django에서 Airflow API를 호출하는 예시로 api_endpoint는 Airflow의 /api/v1/dags/{dag_id}/dagRuns 경로가 됩니다. 여기서 dag_id는 실행할 DAG의 ID로, 이를 동적으로 설정해야 합니다.
    '''
    print(response.text)  # API 응답 출력

with DAG('api_call_dag', start_date=datetime(2024, 11, 22), schedule_interval=None) as dag:
    task = PythonOperator(
        task_id='call_external_api',
        python_callable=call_api,
    )

'''
connections 설정 후 사용할 버전
'''
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

def process_api_response(response):
    if response.status_code == 200:
        data = response.json()
        # 응답 데이터 처리
    else:
        raise Exception("API 호출 실패")

with DAG('api_response_dag', start_date=datetime(2024, 11, 22), schedule_interval=None) as dag:
    api_task = SimpleHttpOperator(
        task_id='call_api_and_process',
        method='GET',
        http_conn_id='my_http_connection',
        endpoint='your_api_endpoint',
        response_check=lambda response: response.status_code == 200,  # 상태 코드 확인
        log_response=True,
    )

    process_task = PythonOperator(
        task_id='process_api_response',
        python_callable=process_api_response,
        op_kwargs={'response': api_task.output}  # api_task의 출력값을 처리
    )

    api_task >> process_task




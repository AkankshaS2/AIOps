from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def analyze_metrics():
    print("Python execution started: Analyzing operational metrics...")
    return "Metrics analyzed successfully!"

default_args = {
    'owner': 'aiops_user',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='python_bash_combined_pipeline',
    default_args=default_args,
    description='Pipeline demonstrating Python and Bash operators',
    schedule=timedelta(days=1), 
    start_date=datetime(2024, 1, 1), 
    catchup=False,
) as dag:

    python_task = PythonOperator(
        task_id='run_python_anomaly_detection',
        python_callable=analyze_metrics,
    )

    bash_task = BashOperator(
        task_id='run_bash_producer',
        bash_command='echo "Bash task triggered! Starting producer..." && python /workspaces/codespaces-blank/producer.py',
    )

    python_task >> bash_task
  

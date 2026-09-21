from airflow import DAG
# Based on your previous terminal output, use this specific BashOperator import
from airflow.providers.standard.operators.bash import BashOperator
# Standard import for the PythonOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# 1. Define the Python function to be executed
def analyze_metrics():
    print("Python execution started: Analyzing operational metrics...")
    # You can write any Python logic here (e.g., Anomaly Detection)
    # The output will show up in the Airflow task logs
    return "Metrics analyzed successfully!"

# 2. Define default arguments
default_args = {
    'owner': 'aiops_user',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# 3. Instantiate the DAG
with DAG(
    dag_id='python_bash_combined_pipeline',
    default_args=default_args,
    description='Pipeline demonstrating Python and Bash operators',
    schedule=timedelta(days=1), 
    start_date=datetime(2024, 1, 1), 
    catchup=False,
) as dag:

    # 4. PythonOperator Task
    # Runs the analyze_metrics function defined above
    python_task = PythonOperator(
        task_id='run_python_anomaly_detection',
        python_callable=analyze_metrics,
    )

    # 5. BashOperator Task
    # Runs a terminal command (can also run a .py file or .sh script)
    bash_task = BashOperator(
        task_id='run_bash_producer',
        bash_command='echo "Bash task triggered! Starting producer..." && python /workspaces/codespaces-blank/producer.py',
    )

    # 6. Set Dependencies (Execution Order)
    # The Python task runs first. If successful, it triggers the Bash task.
    python_task >> bash_task

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def greet():
    return "Greetings"

default_args = {

}

with DAG(
    dag_id="my_dag",
    start_date=datetime(2024, 2, 15),
    schedule="@daily"
) as dag:
    my_task = PythonOperator(
        task_id='MyFirstTask',
        python_callable=greet
    )

    my_task_2 = PythonOperator(
        task_id='MySecondTask',
        python_callable=greet
    )

    my_task_3 = PythonOperator(
        task_id='MyThirdTask',
        python_callable=greet
    )


    my_task >> my_task_2 >> my_task_3
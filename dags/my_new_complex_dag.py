from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def good_morning():
    return "Good Morning"
def good_evening():
    return "Good Evening"
def good_afternoon():
    return "Good Afternoon"


default_args = {

}

with DAG(
    dag_id="my_complex_dag",
    start_date=datetime(2024, 2, 15),
    schedule="@daily"
) as dag:
    my_task = PythonOperator(
        task_id='Greeting_Good_Morning',
        python_callable=good_morning
    )

    my_task_2 = PythonOperator(
        task_id='Greeting_Good_Evening',
        python_callable=good_evening
    )

    my_task_3 = PythonOperator(
        task_id='Greeting_Good_Afternoon',
        python_callable=good_afternoon
    )


    my_task  
    my_task_2 
    my_task_3
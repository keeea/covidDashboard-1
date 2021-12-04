from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from pathlib import Path
from pipeline_tools import run_transform_gbq

from . import extract_breakthrough
from . import extract_daily_summary
from . import extract_data_map
from . import extract_NYC_map
from . import extract_vac_ago
from . import extract_wk_all
from . import load_breakthrough
from . import load_daily_summary
from . import load_data_map
from . import load_NYC_map
from . import load_vac_ago
from . import load_wk_all
from . import transform_final_covid

with DAG(dag_id='data_pipeline',
         schedule_interval='@daily',
         start_date=datetime(2021, 10, 22),
         catchup=False) as dag:

    # EXTRACT TASKS ~~~~~

    extract_breakthrough_task = PythonOperator(
        task_id='extract_breakthrough',
        python_callable=extract_breakthrough.main,
    )
    extract_daily_summary_task = PythonOperator(
        task_id='extract_daily_summary',
        python_callable=extract_daily_summary.main,
    )
    extract_data_map_task = PythonOperator(
        task_id='extract_data_map',
        python_callable=extract_data_map.main,
    )
    extract_NYC_map_task = PythonOperator(
        task_id='extract_NYC_map',
        python_callable=extract_NYC_map.main,
    )
    extract_vac_ago_task = PythonOperator(
        task_id='extract_vac_ago',
        python_callable=extract_vac_ago.main,
    )
    extract_wk_all_task = PythonOperator(
        task_id='extract_wk_all',
        python_callable=extract_wk_all.main,
    )

    # LOAD TASKS ~~~~~

    load_breakthrough_task = PythonOperator(
        task_id='load_breakthrough',
        python_callable=load_breakthrough.main,
    )
    load_daily_summary_task = PythonOperator(
        task_id='load_daily_summary',
        python_callable=load_daily_summary.main,
    )
    load_data_map_task = PythonOperator(
        task_id='load_data_map',
        python_callable=load_data_map.main,
    )
    load_NYC_map_task = PythonOperator(
        task_id='load_NYC_map',
        python_callable=load_NYC_map.main,
    )
    load_vac_ago_task = PythonOperator(
        task_id='load_vac_ago',
        python_callable=load_vac_ago.main,
    )
    load_wk_all_task = PythonOperator(
        task_id='load_wk_all',
        python_callable=load_wk_all.main,
    )
    

    # TRANSFORM TASKS ~~~~~

    sql_dir = Path(__file__).parent / 'sql'

    transform_final_covid = PythonOperator(
        task_id='transform_final_covid',
        python_callable=run_transform_gbq,
        op_args=['staging', '', sql_dir],
    )

    # DEPENDENCIES ~~~~~

    extract_breakthrough_task >> load_breakthrough_task
    extract_daily_summary_task >> load_daily_summary_task
    extract_data_map_task >> load_data_map_task
    extract_NYC_map_task >> load_NYC_map_task
    extract_vac_ago_task >> load_vac_ago_task
    extract_wk_all_task >> load_wk_all_task

    load_tasks = DummyOperator(task_id='wait_for_loads')
    load_tasks << [
        load_breakthrough_task,
        load_daily_summary_task,
        load_data_map_task,
        load_NYC_map_task,
        load_vac_ago_task,
        load_wk_all_task,
    ]

    transform_final_covid << load_tasks
    
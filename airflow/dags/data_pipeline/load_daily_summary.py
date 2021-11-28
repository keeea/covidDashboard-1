from pipeline_tools import gcs_to_local_file, geopandas_to_gbq
import pandas as pd
import pandas_gbq

def main(ds):
    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/daily_summary.csv',
    )
    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.daily_summary')

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

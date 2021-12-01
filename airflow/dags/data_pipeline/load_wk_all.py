from pipeline_tools import gcs_to_local_file, geopandas_to_gbq
import pandas as pd
import pandas_gbq

def main(ds):
    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_case_age.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_case_age',if_exists='replace')

    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_case_race.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_case_race',if_exists='replace')

    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_death_age.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_death_age',if_exists='replace')

    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_death_race.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_death_race',if_exists='replace')

    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_hosp_age.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_hosp_age',if_exists='replace')

    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/wk_hosp_race.csv',
    )

    df = pd.read_csv(local_path)
    df.to_gbq(f'covid.wk_hosp_race',if_exists='replace')
    
    
    print('Done.')

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

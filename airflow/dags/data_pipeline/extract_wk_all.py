from pipeline_tools import http_to_gcs

def main(ds):
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-case-rate-age.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_case_age.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-case-rate-race.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_case_race.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-death-rate-age.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_death_age.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-death-rate-race.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_death_race.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-hosp-rate-age.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_hosp_age.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-hosp-rate-race.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/wk_hosp_race.csv',
    )


if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

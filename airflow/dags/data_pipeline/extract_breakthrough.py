from pipeline_tools import http_to_gcs

def main(ds):
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/trends/weekly-breakthrough.csv',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/breakthrough.csv',
    )

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

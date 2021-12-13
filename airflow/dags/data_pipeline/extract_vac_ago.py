from pipeline_tools import http_to_gcs

def main(ds):
    http_to_gcs(
        request_method='get',
        request_url='https://health.data.ny.gov/api/views/duk7-xrni/rows.csv',
        gcs_bucket_name='clementi_509_airflowcloud_bucket',
        gcs_blob_name=f'covid/{ds}/vac_ago.csv',
    )

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

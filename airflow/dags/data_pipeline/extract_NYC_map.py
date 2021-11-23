from pipeline_tools import http_to_gcs

def main(ds):
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/Geography-resources/MODZCTA_2010_WGS1984.geo.json',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/NYC_map.geojson',
    )

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today()-dt.timedelta(days=1))

from pipeline_tools import http_to_gcs

def main(ds):
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/latest/last7days-by-modzcta.csv',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/test_7d.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/latest/hosp_death_last28days-by-modzcta.csv',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/hosp_death_28d.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/coronavirus-data/master/totals/data-by-modzcta.csv',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/test_death_1d.csv',
    )
    http_to_gcs(
        request_method='get',
        request_url='https://raw.githubusercontent.com/nychealth/covid-vaccine-data/main/people/coverage-by-modzcta-allages.csv',
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/{ds}/vac_now_neigh.csv',
    )


if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

from pipeline_tools import gcs_to_local_file, geopandas_to_gbq
import geopandas as gpd

def main(ds):
    local_path = gcs_to_local_file(
        gcs_bucket_name='anranz_cloudservices',
        gcs_blob_name=f'covid/NYC_map.geojson'
    )

    print(f'Loading file {local_path} into a GeoDataFrame...')
    gdf = gpd.read_file(local_path)

    geopandas_to_gbq(
        geodataframe=gdf,
        dataset_name='covid',
        table_name='NYC_map'
    )

    print('Done.')

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

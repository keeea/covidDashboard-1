import geopandas as gpd
import pandas as pd
from pathlib import Path
from tempfile import NamedTemporaryFile
from jinja2 import Environment, PackageLoader
from pipeline_tools import local_file_to_gcs

def main(ds):
    # Get the data necessary for the report.
    wk_all_df = pd.read_gbq('SELECT * FROM final.wk_all')
    daily_summary_df=pd.read_gbq('SELECT * FROM covid.daily_summary')

    #download the map data
    covid_map_df = pd.read_gbq('SELECT * FROM final.covid_map')
    covid_map_df.geometry = gpd.GeoSeries.from_wkt(covid_map_df.geometry)
    covid_map_gdf = gpd.GeoDataFrame(covid_map_df, geometry='geometry')

    # Render the data into the templates.
    env = Environment(loader=PackageLoader('generate_report'))
    template = env.get_template('index_lab9.html')
    output = template.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        top_region=covid_map_df.to_dict('list'),
    )

    # Determine the folder to save the rendered report pages into; create it if
    # it doesn't already exist. E.g.: report_generator/_reports/2021-11-22/
    output_folder = Path(__file__).parent / '_reports' / ds.isoformat()
    output_folder.mkdir(parents=True, exist_ok=True)

    # Write the report to the local folder, and upload to GCS.
    with open(output_folder / 'index_lab9.html', 'w') as local_file:
        local_file.write(output)
        local_file_to_gcs(
            local_file_name=local_file.name,
            gcs_bucket_name='anranz_cloudservices',
            gcs_blob_name=f'{ds}/index_lab9.html',
            content_type='text/html,'
        )

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

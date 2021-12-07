import geopandas as gpd
import pandas as pd
from pathlib import Path
from tempfile import NamedTemporaryFile
from jinja2 import Environment, PackageLoader
from pipeline_tools import local_file_to_gcs
def main(ds):
    # Get the data necessary for the report.
    #choose year 2021, visualize the race/sex curve
    wk_all_df = pd.read_gbq("SELECT * FROM final.wk_all WHERE week_ending LIKE '%2021'")
    #choose year 2021, visualize the time curve
    daily_summary_df=pd.read_gbq("SELECT * FROM covid.daily_summary WHERE date_of_interest LIKE '%2021'")
    #real-time data table
    new_report_df=pd.read_gbq("SELECT * FROM final.new_report")
    #top test table
    top_test_df=pd.read_gbq("SELECT * FROM final.top_test")
    #vaccine curve
    vac_accumulated_by_day_df=pd.read_gbq("SELECT * FROM final.vac_accumulated_by_day WHERE date LIKE '%2021'")
    #visualize the hospitalization comparision barplot under vaccine or unvaccine
    breakthrough_df=pd.read_gbq("SELECT * FROM covid.breakthrough")
    #map of ratio of death/treated 
    #dh_28day=pd.read_gbq("SELECT * FROM final.wk_all ORDER BY date DESC LIMIT 1")
    #download the map data
    covid_map_df = pd.read_gbq('SELECT * FROM final.covid_map')
    covid_map_df.geometry = gpd.GeoSeries.from_wkt(covid_map_df.geometry)
    covid_map_gdf = gpd.GeoDataFrame(covid_map_df, geometry='geometry')
    # Render the data into the templates.
    env = Environment(loader=PackageLoader('generate_report1'))
    template = env.get_template('index_lab9.html')
    output = template.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        new_report=new_report_df.to_dict('records'),
        top_test=top_test_df.to_dict('records'),
        vac_accumulated_by_day=vac_accumulated_by_day_df.to_dict('list'),
        breakthrough=breakthrough_df.to_dict('list'),
        #death_treated=dh_28day.to_dict('list')
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
    print("Finished!")
if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today())

import geopandas as gpd
import pandas as pd
from pathlib import Path
from tempfile import NamedTemporaryFile
from jinja2 import Environment, FileSystemLoader
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
    #top hosp table
    top_hosp_df=pd.read_gbq("SELECT * FROM final.top_hosp")
    #top death table
    top_death_df=pd.read_gbq("SELECT * FROM final.top_death")
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

    # Load the templates.
    templates_folder = Path(__file__).parent / 'templates'
    template_env = Environment(loader=FileSystemLoader(templates_folder))
    IndexTemplate = template_env.get_template('index.html')
    casesTemplate = template_env.get_template('cases.html')
    deathsTemplate = template_env.get_template('deaths.html')
    hospitalTemplate = template_env.get_template('hospital.html')


    # Determine the folder to save the rendered report pages into; create it if
    # it doesn't already exist. E.g.: report_generator/_reports/2021-11-22/
    output_folder = Path(__file__).parent / '_reports' / ds
    output_folder.mkdir(parents=True, exist_ok=True)



    # Render the data into the templates.
    IndexOutput = IndexTemplate.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        new_report=new_report_df.to_dict('records'),
        top_test=top_test_df.to_dict('records'),
        vac_accumulated_by_day=vac_accumulated_by_day_df.to_dict('list'),
        breakthrough=breakthrough_df.to_dict('list'),
        #death_treated=dh_28day.to_dict('list')
    )

    # Write the report to the local folder, and upload to GCS.
    with open(output_folder / 'index.html', 'w') as local_file:
        local_file.write(IndexOutput)
        local_file_to_gcs(
            local_file_name=local_file.name,
            gcs_bucket_name='clementi_509_airflowcloud_bucket',
            gcs_blob_name=f'{ds}/index.html',
            content_type='text/html,'
        )
    print("Index.html report generated!")



    # Render the cases into the templates.
    casesOutput = casesTemplate.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        new_report=new_report_df.to_dict('list'),
        top_test=top_test_df.to_dict('records'),
        vac_accumulated_by_day=vac_accumulated_by_day_df.to_dict('list'),
        breakthrough=breakthrough_df.to_dict('list'),
        #death_treated=dh_28day.to_dict('list')
    )

    # Write the cases report to the local folder, and upload to GCS.
    with open(output_folder / 'cases.html', 'w') as local_file:
        local_file.write(casesOutput)
        local_file_to_gcs(
            local_file_name=local_file.name,
            gcs_bucket_name='clementi_509_airflowcloud_bucket',
            gcs_blob_name=f'{ds}/cases.html',
            content_type='text/html,'
        )
    print("cases.html report generated!")



    # Render the deaths into the templates.
    deathsOutput = deathsTemplate.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        new_report=new_report_df.to_dict('list'),
        top_death=top_death_df.to_dict('records'),
        vac_accumulated_by_day=vac_accumulated_by_day_df.to_dict('list'),
        breakthrough=breakthrough_df.to_dict('list'),
        #death_treated=dh_28day.to_dict('list')
    )

    # Write the deaths report to the local folder, and upload to GCS.
    with open(output_folder / 'deaths.html', 'w') as local_file:
        local_file.write(deathsOutput)
        local_file_to_gcs(
            local_file_name=local_file.name,
            gcs_bucket_name='clementi_509_airflowcloud_bucket',
            gcs_blob_name=f'{ds}/deaths.html',
            content_type='text/html,'
        )
    print("deaths.html report generated!")



    # Render the hospital into the templates.
    hospitalOutput = hospitalTemplate.render(
        wk_all=wk_all_df.to_dict('list'),
        daily_summary=daily_summary_df.to_dict('list'),
        covid_map=covid_map_gdf.to_json(),
        new_report=new_report_df.to_dict('list'),
        top_hosp=top_hosp_df.to_dict('records'),
        vac_accumulated_by_day=vac_accumulated_by_day_df.to_dict('list'),
        breakthrough=breakthrough_df.to_dict('list'),
        #death_treated=dh_28day.to_dict('list')
    )

    # Write the auxiliary report to the local folder, and upload to GCS.
    with open(output_folder / 'hospital.html', 'w') as local_file:
        local_file.write(hospitalOutput)
        local_file_to_gcs(
            local_file_name=local_file.name,
            gcs_bucket_name='clementi_509_airflowcloud_bucket',
            gcs_blob_name=f'{ds}/hospital.html',
            content_type='text/html,'
        )
    print("hospital.html report generated!")


    print("Finished!")

if __name__ == '__main__':
    import datetime as dt
    main(ds=dt.date.today().isoformat())

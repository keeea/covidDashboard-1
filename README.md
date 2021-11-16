# Visualization of COVID-19 in Philadelphia

**By**:
* Anran Zheng, anranz@design.upenn.edu
* Johnathan Clementi, clementi@design.upenn.edu
* Lan Xiao, lanxiao@design.upenn.edu

## Abstract
### Situation

COVID-19 has been spread worldwide since 2019, and there has been a new peek of the outbreak in the US at the beginning of 2021. So it is still significantly necessary for the government and institutions that face crowd gathering risk in Philadelphia to track the trend of reported cases, death, and hospitalization condition of COVID. In addition, as COVID vaccines are developed and used this year, the government and other stakeholders, such as universities, start to pay more attention to vaccine coverage, breakthrough infections, and hospitalization accessibility.

### Decision Metrics

First and foremost, this COVID dashboard will help to **track general infection trends** by time curve and 14-day changes of reported cases, death, hospitalization, and vaccination. Also, age, racial and sexual composition will be demonstrated to assist government and stakeholders in **identifying how to allocate related resources**. On top of that, hot pot maps by zip code will be helpful in **targeting breakout places and containing the spread of the epidemic promptly**. What's more important, the dashboard will combine data from different sources and engineer effect metrics and graphics, including ratio of positive test/vaccinated that will contribute to **simulate breakthrough infections**, ratio of treated/death that will contribute to **warn higher mortality due to poor hospitalization accessibility**, and a multiple line plot of hospitalization & vaccine that help to **explore whether neighborhoods are not active to take vaccine are more apt to not be hospitalized**.

## Data Sources
We choose four aspects of COVID-19 data, confirmed cases, hospitalization, death and vaccination mainly from [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-cases). Some data from [CDC](https://data.cdc.gov/browse) might also be considered. The data form that we will utilized in our project includes csv, geojson, shp and API.  We will also use the aggregated number by different groups of sex, race and age categories provided by all these datasets. Both real-time and historical data by ZIP is needed in our project. All the datasets are open-accessed to us. 

**Test and cases:** -- [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-cases), updated "daily" at 4 pm every day (according to city [metadata](https://metadata.phila.gov/#home/datasetdetails/5ea725f6890f920015c17af8/representationdetails/5ea73b68890f920015c190d3/)). We choose the historical test data, which starts from March 2020 to present, and real-time test outcome data by ZIP:

  name  | field  | format
  ------------- | ------------- | -------------
 COVID Tests by Date   | collection_date, test_result, count, etl_timestamp  | csv
COVID Tests by ZIP    | covid_status, zip_code, count, etl_timestamp  | GeoJSON

**Hospitalization:** -- [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-hospitalizations), updated "daily" at 4 pm every day (according to city [metadata](https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efb6f4a2f3c4c00199b0c84/)). Following the **Test and cases**, we choose the similar data type:  

  name  | field  | format
  ------------- | ------------- | -------------
COVID Hospitalizations by Date   | date, hospitalized, count, etl_timestamp  | csv
COVID Hospitalizations by ZIP    | hospitalized, zip_code, count, etl_timestamp | GeoJSON

**Death:** -- [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-deaths), updated "daily" at 4 pm every day (according to city [metadata](https://metadata.phila.gov/#home/datasetdetails/5efb5dc2bec0b10015172d9b/representationdetails/5efb6f4a2f3c4c00199b0c84/))

  name  | field  | format
  ------------- | ------------- | -------------
COVID Deaths by Date   | date, clinical_date_of_death, count, etl_timestamp  | csv
COVID Vaccinations by ZIP    | clinical_date_of_death, zip_code, count, etl_timestamp | GeoJSON

**Vaccine:** -- [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-vaccinations), updated "daily" at 4 pm every day (according to city [metadata](https://metadata.phila.gov/#home/datasetdetails/601abeb9f910a2001ce794e2/representationdetails/60b93022a59bf60021d2a63a/)). Unlike those above datasets, the cummulative of historical vaccination data can not be reached directly so real-time vaccination data and vaccination data by ZIP are chosen:

  name  | field  | format
  ------------- | ------------- | -------------
Total COVID Vaccinations   | date, clinical_date_of_death, count, etl_timestamp  | csv
COVID Deaths by ZIP    | partially_vaccinated,fully_vaccinated, zip_code, count, etl_timestamp | GeoJSON

**COVID Cumulative Historical Snapshots:** -- [OpenDataPhilly](https://www.opendataphilly.org/dataset/covid-cumulative-historical-data), updated "daily" at 4 pm every day. Here we pick three types of data:

  - the historical data of COVID-19 tested/death/hospitalized/vaccined by age/race/sex.
  - the historical data of COVID-19 tested/death/hospitalized/vaccined by ZIP.
  - the historical data of cummulative vaccination. 

All the data is csv.gz format. For tested/death/hospitalized data, the study period ranges from September 1st, 2020 to present. Since vaccination data is later open accessed, the study period of vaccination data ranges from March 21st, 2021 to now. We analyzed our data in three different time scale: real-time, the last 14 days and the cummulative since the beginning.

**Total population by ZIP in Philadelphia:** -- BigQuery public datasets,updated with the national census, here we choose 2018 5-years ACS.

**Philadelphia geometry:** -- [GeoServices](https://github.com/PhiladelphiaController/esri2gpd), updated as needed.


## Wireframes
![ConclusionWireframe drawio](https://user-images.githubusercontent.com/90301308/141871347-633dbcb8-497b-4296-ba3a-3cbb24032286.png)
![2ndEditionWireframe](https://user-images.githubusercontent.com/90301308/141871358-9990990e-aec4-426a-96a1-1d8278c869dc.png)




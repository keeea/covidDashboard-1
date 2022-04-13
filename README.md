# Visualization of COVID-19 in NYC

**By**:
* Anran Zheng, anranz@design.upenn.edu
* Johnathan Clementi, clementi@design.upenn.edu
* Lan Xiao, lanxiao@design.upenn.edu

## Dashboard Page
[page](https://storage.googleapis.com/coviddashboard_publicbucket/2021-12-15/index.html)

The data are no longer automatically updated due to the cloud platform fees.

## Abstract
### Situation

COVID-19 has been spread worldwide since 2019, and there has been a new peek of the outbreak in the US at the beginning of 2021. So it is still significantly necessary for the government and institutions that face crowd gathering risk in Philadelphia to track the trend of reported cases, death, and hospitalization condition of COVID. In addition, as COVID vaccines are developed and used this year, the government and other stakeholders, such as universities, start to pay more attention to vaccine coverage, breakthrough infections, and hospitalization accessibility.

### Decision Metrics

First and foremost, this COVID dashboard will help to **track general infection trends** by time curve and 14-day changes of reported cases, death, hospitalization, and vaccination. Also, age, racial and sexual composition will be demonstrated to assist government and stakeholders in **identifying how to allocate related resources**. On top of that, hot pot maps by zip code will be helpful in **targeting breakout places and containing the spread of the epidemic promptly**. What's more important, the dashboard will combine data from different sources and engineer effect metrics and graphics, including propotion of report cases who have been vaccinated that will contribute to **estimate breakthrough infections**, ratio of treated/death that will contribute to **warn higher mortality due to poor hospitalization accessibility**, and a multiple line plot of hospitalization & vaccine that help to **explore whether neighborhoods are not active to take vaccine are more apt to not be hospitalized**.

## Data Sources
We choose four aspects of COVID-19 data, **confirmed cases, hospitalization, death and vaccination** mainly from [NYC Open Data](https://data.cityofnewyork.us/browse?category=Health&q=covid) and [New York State Department of Health](https://health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Vaccination-Data/duk7-xrni). The data form that we will utilized in our project includes csv and geojson. We will also use the aggregated number by **different groups of race and age categories** provided by all these datasets except vaccination due to data unavailability. In terms of time, we consider **the real-time, latest 7 or 28 days, and historical daily** data. In terms of space, we choose MODZCTA (modified ZIP code tabulation area) level of NYC. All the datasets are open-accessed to us. 

**Daily historical case/death/hospitalization:** -- [NYC Open Data](https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3), updated every day from Feb 29th 2020 to present. The fields we may consider includes the date `DATE_OF_INTEREST`, daily new cases/death/hospitalization number `CASE/DEATH/HOSPITALIZED_COUNT` and the average of 7 days new cases/death/hospitalization number `CASE/DEATH/HOSPITALIZED_7DAY_AVG`.

**Weekly breakthrough:** -- [NYC Open Data](https://github.com/Anran0716/coronavirus-data/blob/master/trends/weekly-breakthrough.csv), updated every day. The fields we may consider includes date `Week_of_diagnosis`and the count or rate of cases/death/hospitalization under the vaccination or not `vax/unvax_case/hosp/death_count/rate`.

**Weekly cases/death/hospitalization rate by age or race:** -- [NYC Open Data](https://github.com/Anran0716/coronavirus-data/tree/master/trends), updated weekly. The fields we may consider includes date `week_ending`, the age category label (e.g. `age_0_4`...`age_75up`) and the race category label (e.g. `Asian_Pacific_Islander`...`	White`).

**Cases/death/hospitalization/vaccine by MODZCTA:** -- [NYC Open Data](https://github.com/Anran0716/coronavirus-data/tree/master/latest), updated daily for vaccination, weekly for cases and monthly for death and hospitalization. The fields we may consider includes date, ZIP code`modzcta`,`modzcta_name`, the count or rate of last 28 days hospitalization/death `hospitalization/death_rate/count_28day`,`daterange`, the positivity rate of past 7 days `percentpositivity_7day`, and the count that people were fully vaccinated `COUNT_FULLY_CUMULATIVE` etc.

**the historical vaccine data of NYC:** -- [New York State Department of Health](https://www.opendataphilly.org/dataset/covid-cumulative-historical-data), updated every day from Dec 14th 2020 to present. The fields we may consider includes date, region and the full vaccinated doses `Series Complete`.

**NYC base map by MODZCTA:** -- [NYC Open Data](https://github.com/Anran0716/coronavirus-data/tree/master/Geography-resources). The above data is csv format but this geographic file is geojson format.


## Wireframes
![ConclusionWireframe drawio (1)](https://user-images.githubusercontent.com/90301308/144319389-68c32989-d914-4009-890b-084bd070d046.png)




![2ndEditionWireframe](https://user-images.githubusercontent.com/90301308/141871358-9990990e-aec4-426a-96a1-1d8278c869dc.png)




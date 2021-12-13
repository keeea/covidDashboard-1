with test_7d as (
    select 
        modzcta_name,
        modzcta,
        percentpositivity_7day,
        people_positive,
        median_daily_test_rate
    from `musa509cloudcomputing.covid.test_7d`
),

hosp_death_28d as (
    select 
        modzcta,
        hospitalization_count_28day,
        hospitalization_rate_28day,
        death_count_28day,
        death_rate_28day,
        daterange
    from `musa509cloudcomputing.covid.hosp_death_28d`
),
case_death_1d as (
    select 
    MODIFIED_ZCTA as modzcta,
    COVID_DEATH_COUNT,
    COVID_DEATH_COUNT/COVID_CASE_COUNT as death_case_ratio
    from `musa509cloudcomputing.covid.test_death_1d`
)

select 
        a.modzcta_name,
        a.modzcta,
        a.percentpositivity_7day,
        a.people_positive,
        a.median_daily_test_rate,
        b.hospitalization_count_28day,
        b.hospitalization_rate_28day,
        b.death_count_28day,
        b.death_rate_28day,
        b.daterange,
        c.COVID_DEATH_COUNT,
        c.death_case_ratio
from test_7d as a
full join hosp_death_28d as b
on a.modzcta=b.modzcta
full join case_death_1d as c
on a.modzcta=c.modzcta
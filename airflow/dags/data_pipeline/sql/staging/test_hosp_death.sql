with test_7d as (
    select 
        modzcta_name,
        modzcta,
        percentpositivity_7day,
        median_daily_test_rate
    from `elated-guild-327520.covid.test_7d`
),

hosp_death_28d as (
    select 
        modzcta,
        hospitalization_count_28day,
        hospitalization_rate_28day,
        death_count_28day,
        death_rate_28day,
        daterange
    from `elated-guild-327520.covid.hosp_death_28d`
)

select 
        a.modzcta_name,
        a.modzcta,
        a.percentpositivity_7day,
        a.median_daily_test_rate,
        b.hospitalization_count_28day,
        b.hospitalization_rate_28day,
        b.death_count_28day,
        b.death_rate_28day,
        b.daterange
from test_7d as a
full join hosp_death_28d as b
on a.modzcta=b.modzcta
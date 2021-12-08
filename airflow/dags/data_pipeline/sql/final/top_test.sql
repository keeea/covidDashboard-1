with data_map as (
    select 
    a.modzcta_name,
    cast(a.modzcta as string) as modzcta,
    a.percentpositivity_7day,
    a.median_daily_test_rate,
    a.hospitalization_count_28day,
    a.hospitalization_rate_28day,
    a.death_count_28day,
    a.death_rate_28day,
    a.daterange,
    b.date,
    b.count_fully_cumulative,
    b.perc_fully
    from `elated-guild-327520.staging.test_hosp_death` a
    full join `elated-guild-327520.staging.vac_now_neigh` b
    on a.modzcta=b.modzcta
)

select 
row_number() OVER(order by percentpositivity_7day desc ) as Rank, 
modzcta_name as neighborhood_name,
concat(cast(percentpositivity_7day as string),"%") as percent_positivity_7day
from data_map
order by Rank
limit 5

with data_map as (
    select 
    a.modzcta_name,
    cast(a.modzcta as string) as modzcta,
    a.percentpositivity_7day,
    a.median_daily_test_rate,
    a.hospitalization_count_28day,
    ifnull(a.hospitalization_rate_28day,0) as hospitalization_rate_28day,
    a.death_count_28day,
    a.death_rate_28day,
    a.daterange,
    b.date,
    b.count_fully_cumulative,
    b.perc_fully
    from `musa509cloudcomputing.staging.test_hosp_death` a
    full join `musa509cloudcomputing.staging.vac_now_neigh` b
    on a.modzcta=b.modzcta
)

select 
row_number() OVER(order by hospitalization_rate_28day desc ) as Rank, 
modzcta_name as neighborhood_name,
concat(cast(hospitalization_rate_28day as string),"") as hospitalization_rate_28day
from data_map
order by Rank
limit 5
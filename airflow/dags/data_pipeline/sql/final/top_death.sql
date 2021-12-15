with death_map as (
    select 
    ifnull(COVID_DEATH_RATE,0) as COVID_DEATH_RATE_1d,
    NEIGHBORHOOD_NAME 
    from `musa509cloudcomputing.covid.test_death_1d`
)

select 
row_number() OVER(order by COVID_DEATH_RATE_1d desc ) as Rank, 
NEIGHBORHOOD_NAME as neighborhood_name,
concat(cast(COVID_DEATH_RATE_1d as string),"") as COVID_DEATH_RATE_1d
from death_map
order by Rank
limit 5
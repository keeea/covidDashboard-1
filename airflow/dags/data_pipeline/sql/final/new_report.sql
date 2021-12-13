with recent_7day_avg as (
    select 
        PARSE_DATE("%m/%d/%Y", date_of_interest) as date_of_interest,
        "date_is_different" as key,
        CASE_COUNT_7DAY_AVG,
        HOSP_COUNT_7DAY_AVG,
        DEATH_COUNT_7DAY_AVG
    from `musa509cloudcomputing.covid.daily_summary`
    where PARSE_DATE("%m/%d/%Y", date_of_interest) = DATE_SUB(current_date, INTERVAL 7 DAY)
),

past_14to21day_avg as (
    select 
        DATE_SUB(current_date, INTERVAL 7 DAY) as yesterday,
        "date_is_different" as key,
        PARSE_DATE("%m/%d/%Y", date_of_interest) as p_date_of_interest,
        CASE_COUNT_7DAY_AVG as p_CASE_COUNT_7DAY_AVG,
        HOSP_COUNT_7DAY_AVG as p_HOSP_COUNT_7DAY_AVG,
        DEATH_COUNT_7DAY_AVG as p_DEATH_COUNT_7DAY_AVG
    from `musa509cloudcomputing.covid.daily_summary`
    where PARSE_DATE("%m/%d/%Y", date_of_interest)= DATE_SUB(current_date, INTERVAL 21 DAY)
),

report_1 as (
    select 
        a.date_of_interest,
        "date_is_different" as key, 
        a.CASE_COUNT_7DAY_AVG,
        a.HOSP_COUNT_7DAY_AVG,
        a.DEATH_COUNT_7DAY_AVG,
        concat(cast(round((a.CASE_COUNT_7DAY_AVG-b.p_CASE_COUNT_7DAY_AVG)/b.p_CASE_COUNT_7DAY_AVG*100,2) as string),"%") as case_change,
        concat(cast(round((a.HOSP_COUNT_7DAY_AVG-b.p_HOSP_COUNT_7DAY_AVG)/b.p_HOSP_COUNT_7DAY_AVG*100,2) as string),"%") as hosp_change,
        concat(cast(round((a.DEATH_COUNT_7DAY_AVG-b.p_DEATH_COUNT_7DAY_AVG)/b.p_DEATH_COUNT_7DAY_AVG*100,2) as string),"%") as death_change,

    from recent_7day_avg as a
    full join past_14to21day_avg as b
    on a.key = b.key
)

select 
    "Case" as Type,
    a.CASE_COUNT_7DAY_AVG as Count_7Day_Avg,
    a.case_change as Change,
    b.case_count_total as Count_Total,
from report_1 a  
full join `musa509cloudcomputing.staging.report_total` b
on a.key=b.key
union all
select
    "Hospitalization" as Type,
    a.HOSP_COUNT_7DAY_AVG as Count_7Day_Avg,
    a.hosp_change as Change,
    b.hosp_count_total as Count_Total,
from report_1 a  
full join `musa509cloudcomputing.staging.report_total` b
on a.key=b.key
union all
select
    "Death" as Type,
    a.DEATH_COUNT_7DAY_AVG as Count_7Day_Avg,
    a.death_change as Change,
    b.death_count_total as Count_Total
from report_1 a  
full join `musa509cloudcomputing.staging.report_total` b
on a.key=b.key
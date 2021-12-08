select 
    DATE_SUB(current_date, INTERVAL 1 DAY) as yesterday,
    "date_is_different" as key,
    sum(CASE_COUNT) as case_count_total,
    sum(HOSPITALIZED_COUNT) as hosp_count_total,
    sum(DEATH_COUNT) as death_count_total
 from `elated-guild-327520.covid.daily_summary`
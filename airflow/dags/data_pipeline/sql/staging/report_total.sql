select 
    DATE_SUB(current_date, INTERVAL 7 DAY) as yesterday,
    sum(CASE_COUNT) as case_count_total,
    sum(HOSPITALIZED_COUNT) as hosp_count_total,
    sum(DEATH_COUNT) as death_count_total
 from `elated-guild-327520.covid.daily_summary`
select 
    `elated-guild-327520.covid.wk_hosp_age`.week_ending as week_ending,
    age_0_4,
    age_5_12,
    age_13_17,
    age_18_24,
    age_25_34,
    age_35_44,
    age_45_54,
    age_55_64,
    age_65_74,
    age_75up,
    Asian_Pacific_Islander,
    Black_African_American,
    Hispanic_Latino,
    White
from `elated-guild-327520.covid.wk_hosp_age` 
full join `elated-guild-327520.covid.wk_hosp_race`
on `elated-guild-327520.covid.wk_hosp_age`.week_ending = `elated-guild-327520.covid.wk_hosp_race`.week_ending
select 
    `musa509cloudcomputing.covid.wk_hosp_age`.week_ending as week_ending,
    IFNULL(age_0_4,0) age_0_4,
    IFNULL(age_5_12,0) age_5_12,
    IFNULL(age_13_17,0) age_13_17,
    IFNULL(age_18_24,0) age_18_24,
    IFNULL(age_25_34,0) age_25_34,
    IFNULL(age_35_44,0) age_35_44,
    IFNULL(age_45_54,0) age_45_54,
    IFNULL(age_55_64,0) age_55_64,
    IFNULL(age_65_74,0) age_65_74,
    IFNULL(age_75up,0) age_75up,
    IFNULL(Asian_Pacific_Islander,0) Asian_Pacific_Islander,
    IFNULL(Black_African_American,0) Black_African_American,
    IFNULL(Hispanic_Latino,0) Hispanic_Latino,
    IFNULL(White,0) White
from `musa509cloudcomputing.covid.wk_hosp_age` 
full join `musa509cloudcomputing.covid.wk_hosp_race`
on `musa509cloudcomputing.covid.wk_hosp_age`.week_ending = `musa509cloudcomputing.covid.wk_hosp_race`.week_ending
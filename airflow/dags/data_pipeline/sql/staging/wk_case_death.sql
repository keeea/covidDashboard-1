with wk_case as (
    select 
        `musa509-332421.covid.wk_case_age`.week_ending as week_ending,
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
    from `musa509-332421.covid.wk_case_age` 
    full join `musa509-332421.covid.wk_case_race` 
    on `musa509-332421.covid.wk_case_age`.week_ending = `musa509-332421.covid.wk_case_race` .week_ending
    ),

wk_death as (
    select 
        `musa509-332421.covid.wk_death_age`.week_ending as week_ending,
        age_0_17,
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
    from `musa509-332421.covid.wk_death_age`
    full join `musa509-332421.covid.wk_death_race`
    on `musa509-332421.covid.wk_death_age`.week_ending = `musa509-332421.covid.wk_death_race`.week_ending
)

select 
    a.week_ending week_ending,
    a.age_0_4 case_age_0_4,
    a.age_5_12 case_age_5_12,
    a.age_13_17 case_age_13_17,
    a.age_18_24 case_age_18_24,
    a.age_25_34 case_age_25_34,
    a.age_35_44 case_age_35_44,
    a.age_45_54 case_age_45_54,
    a.age_55_64 case_age_55_64,
    a.age_65_74 case_age_65_74,
    a.age_75up case_age_75up,
    a.Asian_Pacific_Islander case_Asian_Pacific_Islander,
    a.Black_African_American case_Black_African_American,
    a.Hispanic_Latino case_Hispanic_Latino,
    a.White case_White,
    b.age_0_17 death_age_0_17,
    b.age_18_24 death_age_18_24,
    b.age_25_34 death_age_25_34,
    b.age_35_44 death_age_35_44,
    b.age_45_54 death_age_45_54,
    b.age_55_64 death_age_55_64,
    b.age_65_74 death_age_65_74,
    b.age_75up death_age_75up,
    b.Asian_Pacific_Islander death_Asian_Pacific_Islander,
    b.Black_African_American death_,
    b.Hispanic_Latino death_Hispanic_Latino,
    b.White death_White 
from wk_case as a
full join wk_death as b
on a.week_ending=b.week_ending 
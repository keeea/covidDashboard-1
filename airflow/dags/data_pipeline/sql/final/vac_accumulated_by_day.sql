select 
Report_as_of as date,
sum(First_Dose) as First_Dose,
sum(Series_Complete) as Series_Complete
from `elated-guild-327520.covid.vac_ago`
where Region="New York City"
group by Report_as_of
order by Report_as_of asc 

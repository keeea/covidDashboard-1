select 
Report_as_of as date,
sum(First_Dose) as First_Dose,
sum(Series_Complete) as Series_Complete
from `musa509cloudcomputing.covid.vac_ago`
where Region="New York City"
group by Report_as_of
order by Report_as_of asc 

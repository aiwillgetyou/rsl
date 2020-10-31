-- recommendation favorite movie Arrival

-- step 1
/* create a column with lexemes text with tsvector type */
alter table movies
add column if not exists lexemesSummary tsvector;

/* convert summary column in lexemes text and add to previously created column */
update movies
set lexemesSummary = to_tsvector(summary);

-- step 2

/* query table based on values in the lexemes column */
select url from movies
where lexemesSumary @@ to_tsquery('arrival');

-- step 3

/* add another column called rankSummary */
alter table movies
add column if not exists rankSummary float4;


/* in the rank column, rank the movies based on the lexemes text with plainto_tsquery function in psql based on my favorite movie */
update movies
set rankSummary = ts_rank(lexemesSummary, plainto_tsquery(
(
select Summary from movies where url = 'arrival'
)
));


/* create a new table and export highly ranked movies computed from my favorite movies higher than 0.5 ranking */
create table if not exists  recommendationsSummaryArrival as 
select url, rankSummary from movies where rankSummary > 0.5 order by rankSummary desc limit 50;


/* copy the new table to a CSV file*/
\copy (select * from recommendationsSummaryArrival) to '/home/pi/rsl/topRecommendationsArrivalSummary.csv' with csv;

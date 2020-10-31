-- recommendation favorite movie Arrival

-- step 1

alter table movies
add column if not exists lexemesSummary tsvector;

update movies
set lexemesSummary = to_tsvector(summary);

-- step 2

select url from movies
where lexemesSumary @@ to_tsquery('arrival');

-- step 3

alter table movies
add column if not exists rankSummary float4;

update movies
set rankSummary = ts_rank(lexemesSummary, plainto_tsquery(
(
select Summary from movies where url = 'arrival'
)
));

create table if not exists  recommendationsSummaryArrival as 
select url, rankSummary from movies where rankSummary > 0.5 order by rankSummary desc limit 50;

\copy (select * from recommendationsSummaryArrival) to '/home/pi/rsl/topRecommendationsArrivalSummary.csv' with csv;

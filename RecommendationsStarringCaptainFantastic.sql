-- recommendation favorite movie Captain Fantastic

-- step 1

alter table movies
add column if not exists lexemesStarring tsvector;

update movies
set lexemesStarring = to_tsvector(Starring);

-- step 2

select url from movies
where lexemesStarring @@ to_tsquery('Mortenson');

-- step 3

alter table movies
add column if not exists rankStarring float4;

update movies
set rankStarring = ts_rank(lexemesStarring, plainto_tsquery(
(
select Starring from movies where url = 'captain-fantastic'
)
));

create table if not exists recommendationsStarringCaptainFantastic as 
select url, rankStarring from movies where rankStarring > 0.1 order by rankStarring desc limit 50;

\copy (select * from recommendationsStarringCaptainFantastic) to '/home/pi/rsl/topRecommendationsCaptainFantasticStarring.csv' with csv;

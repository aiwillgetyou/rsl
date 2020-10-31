-- recommendation favorite movie Captain Fantastic

-- step 1

/* create a column with lexemes text with tsvector type */
alter table movies
add column if not exists lexemesStarring tsvector;

/* convert summary column in lexemes text and add to previously created column */

update movies
set lexemesStarring = to_tsvector(Starring);

-- step 2

/* query table based on values in the lexemes column */
select url from movies
where lexemesStarring @@ to_tsquery('captain');

-- step 3

/* add another column called rankSummary */
alter table movies
add column if not exists rankStarring float4;

/* in the rank column, rank the movies based on the lexemes text with plainto_tsquery function in psql based on my favorite movie */
update movies
set rankStarring = ts_rank(lexemesStarring, plainto_tsquery(
(
select Starring from movies where url = 'captain-fantastic'
)
));

/* create a new table and export highly ranked movies computed from my favorite movies higher than 0.5 ranking */
create table if not exists recommendationsStarringCaptainFantastic as 
select url, rankStarring from movies where rankStarring > 0.1 order by rankStarring desc limit 50;

/* copy the new table to a CSV file*/
\copy (select * from recommendationsStarringCaptainFantastic) to '/home/pi/rsl/topRecommendationsCaptainFantasticStarring.csv' with csv;

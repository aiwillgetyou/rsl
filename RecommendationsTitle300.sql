-- recommendation favorite movie 300

-- step 1

/* create a column with lexemes text with tsvector type */
alter table movies
add column if not exists lexemesTitle tsvector;

/* convert summary column in lexemes text and add to previously created column */
update movies
set lexemesTitle = to_tsvector(Title);

-- step 2

/* query table based on values in the lexemes column */
select url from movies
where lexemesTitle @@ to_tsquery('300');

-- step 3

/* add another column called rankSummary */
alter table movies
add column if not exists rankTitle float4;

/* in the rank column, rank the movies based on the lexemes text with plainto_tsquery function in psql based on my favorite movie */
update movies
set rankTitle = ts_rank(lexemesTitle , plainto_tsquery(
(
select title from movies where url = '300'
)
));

/* create a new table and export highly ranked movies computed from my favorite movies higher than 0.5 ranking */
create table if not exists recommendationsTitle300 as 
select url, rankTitle from movies where rankTitle > 0.1 order by rankTitle desc limit 50;

/* copy the new table to a CSV file*/
\copy (select * from recommendationsTitle300) to '/home/pi/rsl/topRecommendations300Title.csv' with csv;

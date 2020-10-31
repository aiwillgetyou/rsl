-- recommendation favorite movie 300

-- step 1

alter table movies
add lexemesTitle tsvector;

update movies
set lexemesTitle = to_tsvector(Title);

-- step 2

select url from movies
where lexemesTitle@@ to_tsquery('300');

-- step 3

alter table movies
add rankTitle float4;

update movies
set rankTitle = ts_rank(lexemesTitle , plainto_tsquery(
(
select title from movies where url = '300'
)
));

create table recommendationsTitle300 as 
select url, rankTitle from movies where rankTitle > 0.1 order by rankTitle desc limit 50;

\copy (select * from recommendationsTitle300) to '/home/pi/rsl/topRecommendations300Title.csv' with csv;

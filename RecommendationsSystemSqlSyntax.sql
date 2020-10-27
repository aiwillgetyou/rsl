-- step 1

alter table movies
add lexemesDirector tsvector; -- < replace x with column name 

update movies
set lexemesDirector = to_tsvector(Director); -- replace the X with with column name

-- step 2

select url from movies
where lexemesDirector @@ to_tsquery('David'); -- replace x with column, replace y with search key

-- step 3

alter table movies
add rank2 float4;

update movies
set rank = ts_rank(lexemesDirector, plainto_tsquery( --replace x
(
select Summary from table where url Like 'fight' -- replace col with names and indicate search criteria at ?
)
));

create table recommendationsBasedonDirectorfield as --replace x 
select url, rank2 from table where rank2 > 0.1 order by rank2 desc limit 50; -- replace col1 and col2 replace other values as well.

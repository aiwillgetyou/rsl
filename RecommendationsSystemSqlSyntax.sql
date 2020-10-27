-- step 1

alter table movies
add lexemesX; -- < replace x with column name 

update movies
set lexemesX = to_tsvector(x); -- replace the X with with column name

-- step 2

select url from movies
where lexemesX @@ to_tsquery('y'); -- replace x with column, replace y with search key

-- step 3

alter table movies
add rank float4;

update movies
set rank = ts_rank(lexemesX, plainto_tsquery( --replace x
(
select col.name from table where col = '?' -- replace col with names and indicate search criteria at ?
)
));

create table recommendationsBasedonXfield as --replace x 
select col1, col2, from table where col > x order by x desc limit 50; -- replace col1 and col2 replace other values as well.

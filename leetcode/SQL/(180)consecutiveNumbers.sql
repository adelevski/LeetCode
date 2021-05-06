
/* This is a triple join to find distinct and at least
 triple-consecutive numbers from our table with Id's and Nums */


{"headers": {"Logs": ["Id", "Num"]}, "rows": {"Logs": [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]}}

select distinct a.Num as ConsecutiveNums from Logs a
join Logs b on a.Id = b.Id + 1 and a.Num = b.Num
join Logs c on a.Id = c.Id + 2 and a.Num = c.Num


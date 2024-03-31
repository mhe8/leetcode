"""
Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
"""

/* Write your T-SQL query statement below */
select w2.id
from weather w1
inner join weather w2
on datediff(day, w1.recordDate, w2.recordDate) = 1
where w2.temperature > w1.temperature
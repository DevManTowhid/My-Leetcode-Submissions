# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM PERSON P LEFT JOIN ADDRESS A USING (PERSONID)
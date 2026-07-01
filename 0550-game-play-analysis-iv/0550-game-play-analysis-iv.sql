SELECT 
    ROUND(COUNT(t2.player_id) / COUNT(t1.player_id), 2) AS fraction
FROM 
    (
        -- Get the first login date for every player
        SELECT player_id, MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
    ) AS t1
LEFT JOIN 
    Activity AS t2 
    ON t1.player_id = t2.player_id 
    AND t2.event_date = t1.first_login + INTERVAL 1 DAY;
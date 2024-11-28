-- Table: Players

-- +-------------+-------+
-- | Column Name | Type  |
-- +-------------+-------+
-- | player_id   | int   |
-- | group_id    | int   |
-- +-------------+-------+
-- player_id is the primary key of this table.
-- Each row of this table indicates the group of each player.
-- Table: Matches

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | match_id      | int     |
-- | first_player  | int     |
-- | second_player | int     | 
-- | first_score   | int     |
-- | second_score  | int     |
-- +---------------+---------+
-- match_id is the primary key of this table.
-- Each row is a record of a match, first_player and second_player contain the player_id of each match.
-- first_score and second_score contain the number of points of the first_player and second_player respectively.
-- You may assume that, in each match, players belongs to the same group.
 
-- The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, 
-- the lowest player_id wins.

-- Write an SQL query to find the winner in each group.

-- The query result format is in the following example:

-- Players table:
-- +-----------+------------+
-- | player_id | group_id   |
-- +-----------+------------+
-- | 15        | 1          |
-- | 25        | 1          |
-- | 30        | 1          |
-- | 45        | 1          |
-- | 10        | 2          |
-- | 35        | 2          |
-- | 50        | 2          |
-- | 20        | 3          |
-- | 40        | 3          |
-- +-----------+------------+

-- Matches table:
-- +------------+--------------+---------------+-------------+--------------+
-- | match_id   | first_player | second_player | first_score | second_score |
-- +------------+--------------+---------------+-------------+--------------+
-- | 1          | 15           | 45            | 3           | 0            |
-- | 2          | 30           | 25            | 1           | 2            |
-- | 3          | 30           | 15            | 2           | 0            |
-- | 4          | 40           | 20            | 5           | 2            |
-- | 5          | 35           | 50            | 1           | 1            |
-- +------------+--------------+---------------+-------------+--------------+

-- Result table:
-- +-----------+------------+
-- | group_id  | player_id  |
-- +-----------+------------+ 
-- | 1         | 15         |
-- | 2         | 35         |
-- | 3         | 40         |
-- +-----------+------------+

-- Solution
WITH t1 AS (
    SELECT 
        first_player, 
        SUM(first_score) AS total
    FROM (
        SELECT 
            first_player, 
            first_score
        FROM 
            matches
        UNION ALL
        SELECT 
            second_player, 
            second_score
        FROM 
            matches
    ) a
    GROUP BY 
        first_player
),

t2 AS (
    SELECT 
        *, 
        COALESCE(total, 0) AS score
    FROM 
        players p 
    LEFT JOIN 
        t1 ON p.player_id = t1.first_player
)

SELECT 
    group_id, 
    player_id
FROM (
    SELECT 
        *, 
        ROW_NUMBER() OVER (PARTITION BY group_id ORDER BY score DESC) AS rn
    FROM 
        t2
) b
WHERE 
    b.rn = 1;

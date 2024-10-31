-- Table: candidate

-- +-----+---------+
-- | id  | name    |
-- +-----+---------+
-- | 1   | A       |
-- | 2   | B       |
-- | 3   | C       |
-- | 4   | D       |
-- | 5   | E       |
-- +-----+---------+  

-- Table: vote

-- +-----+--------------+
-- | id  | candidate_id  |
-- +-----+--------------+
-- | 1   |     2        |
-- | 2   |     4        |
-- | 3   |     3        |
-- | 4   |     2        |
-- | 5   |     5        |
-- +-----+--------------+
-- id is the auto-increment primary key,
-- CandidateId is the id appeared in Candidate table.
-- Write a sql to find the name of the winning candidate. The above example will return the winner B.

-- +------+
-- | name |
-- +------+
-- | B    |
-- +------+
-- Notes:

-- Assume there is no tie. In other words there will be only one winning candidate

-- Solution
WITH t1 AS (
    SELECT 
        *, 
        RANK() OVER(ORDER BY b.votes DESC) AS rk
    FROM 
        candidate c
    JOIN (
        SELECT 
            candidate_id, 
            COUNT(*) AS votes
        FROM 
            vote
        GROUP BY 
            candidateid
    ) b 
    ON c.id = b.candidateid
)

SELECT 
    t1.name
FROM 
    t1
WHERE 
    t1.rk = 1;

-- At a social media company, there is a follow table with two columns: followee, follower.

-- write a sql query to get the amount of each follower’s follower if he/she has one.

-- +-------------+------------+
-- | followee    | follower   |
-- +-------------+------------+
-- |     A       |     B      |
-- |     B       |     C      |
-- |     B       |     D      |
-- |     D       |     E      |
-- +-------------+------------+
-- should output:
-- +-------------+------------+
-- | follower    | num        |
-- +-------------+------------+
-- |     B       |  2         |
-- |     D       |  1         |
-- +-------------+------------+
-- Explanation:
-- Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.
 

-- Note:
-- Followee would not follow himself/herself in all cases.
-- Please display the result in follower's alphabet order.

-- Solution
SELECT 
    followee AS follower, 
    COUNT(DISTINCT follower) AS num
FROM 
    follow
WHERE 
    followee = ANY (
        SELECT 
            follower 
        FROM 
            follow
    )
GROUP BY 
    followee
ORDER BY 
    followee;

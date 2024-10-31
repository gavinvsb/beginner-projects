-- Table: Trips

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | id          | int      |
-- | client_id   | int      |
-- | driver_id   | int      |
-- | status      | enum     |
-- | date        | date     |
-- +-------------+----------+
-- client_id is the primary key (column with unique values) for this table.
-- The table holds all taxi trips. Each trip has a unique id, while client_id and driver_id are foreign keys to the users_id at the Users table.
-- Status is an ENUM (category) type of ('completed', 'cancelled_by_driver', 'cancelled_by_client').
 
-- Table: Users

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | users_id    | int      |
-- | banned      | enum     |
-- | role        | enum     |
-- +-------------+----------+
-- users_id is the primary key (column with unique values) for this table.
-- The table holds all users. Each user has a unique users_id, and role is an ENUM type of ('client', 'driver').
-- banned is an ENUM (category) type of ('Yes', 'No').
 
-- The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

-- Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day. Round Cancellation Rate to two decimal points.
-- Return the result table in any order.

-- Solution
SELECT 
    T.date,
    ROUND(
        SUM(
            CASE 
                WHEN T.status IN ('cancelled_by_driver', 'cancelled_by_client') 
                THEN 1 
                ELSE 0 
            END 
        ) / COUNT(*) * 100, 2 
    ) AS cancellation_rate 
FROM 
    Trips T 
JOIN 
    Users UC 
    ON T.client_id = UC.users_id 
    AND UC.banned = 'No' 
    AND UC.role = 'client' 
JOIN 
    Users UD 
    ON T.driver_id = UD.users_id 
    AND UD.banned = 'No' 
    AND UD.role = 'driver' 
GROUP BY 
    T.date;

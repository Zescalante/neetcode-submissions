SELECT DISTINCT
    I1.account_id
    -- I1.ip_address,
    -- I2.ip_address,
    -- I1.login,
    -- I1.logout,
    -- I2.login,
    -- I2.logout
FROM log_info I1
CROSS JOIN log_info I2 
WHERE 
    I1.account_id = I2.account_id AND 
    I1.ip_address <> I2.ip_address AND 
    (
        (I1.login BETWEEN I2.login AND I2.logout) OR
        (I2.login BETWEEN I1.login AND I1.logout)
    )
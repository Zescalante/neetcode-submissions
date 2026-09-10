CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    total_price DECIMAL(10, 2) NOT NULL
);

INSERT INTO users (user_id, name) VALUES
(1, 'John'),
(2, 'Jane');

INSERT INTO orders (order_id, user_id, total_price) VALUES
(1, 1, 100.00),
(2, 2, 200.00);
-- Do not modify above this line. --



SELECT 
    U.user_id,
    U.name,
    O.order_id,
    O.total_price
FROM users U
CROSS JOIN orders O
WHERE U.user_id = O.user_id;



DROP TABLE IF EXISTS users;
-- Create the table without the foreign key first.
CREATE TABLE users (
id SERIAL PRIMARY KEY,
username text,
email text
);

DROP TABLE IF EXISTS posts;
-- Then the table with the foreign key second.
CREATE TABLE posts (
id SERIAL PRIMARY KEY,
title text,
content text,
views int,
-- The foreign key name is always {other_table_singular}_id
user_id int,
constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


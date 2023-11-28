DROP TABLE IF EXISTS users CASCADE;
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

-- -- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('TestUser1', 'test1.email@test.com');
INSERT INTO users (username, email) VALUES ('TestUser2', 'test2.email@test.com');
INSERT INTO users (username, email) VALUES ('TestUser3', 'test3.email@test.com');
INSERT INTO users (username, email) VALUES ('TestUser4', 'test4.email@test.com');


INSERT INTO posts (user_id, title, content, views) VALUES (1, 'Lorem ipsum', 'Lorem ipsum dolor sit amet', 0);
INSERT INTO posts (user_id, title, content, views) VALUES (2, 'Consectetur', 'Consectetur adipiscing elit', 0);
INSERT INTO posts (user_id, title, content, views) VALUES (3, 'Sed do', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua', 0);
INSERT INTO posts (user_id, title, content, views) VALUES (4, 'Ut enim', 'Ut enim ad minim veniam', 0);


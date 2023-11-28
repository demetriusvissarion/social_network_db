-- -- The job of this file is to reset all of our important database tables.
-- -- And add any data that is needed for the tests to run.
-- -- This is so that our tests, and application, are always operating from a fresh
-- -- database state, and that tests don't interfere with each other.

-- -- First, we must delete (drop) all our tables
-- DROP TABLE IF EXISTS social_networks;
-- DROP SEQUENCE IF EXISTS social_networks_id_seq;
-- DROP TABLE IF EXISTS albums;
-- DROP SEQUENCE IF EXISTS albums_id_seq;

-- -- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS social_networks_id_seq;
-- CREATE TABLE social_networks (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     genre VARCHAR(255)
-- );

-- CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
-- CREATE TABLE albums (
--     id SERIAL PRIMARY KEY,
--     title VARCHAR(255),
--     release_year INTEGER,
--     social_network_id INTEGER
-- );

-- -- Finally, we add any records that are needed for the tests to run
-- INSERT INTO social_networks (name, genre) VALUES ('Pixies', 'Rock');
-- INSERT INTO social_networks (name, genre) VALUES ('ABBA', 'Pop');
-- INSERT INTO social_networks (name, genre) VALUES ('Taylor Swift', 'Pop');
-- INSERT INTO social_networks (name, genre) VALUES ('Nina Simone', 'Jazz');

-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Doolittle', 1989, 1);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Surfer Rosa', 1988, 1);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Waterloo', 1974, 2);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Super Trouper', 1980, 2);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Bossanova', 1990, 1);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Lover', 2019, 3);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Folklore', 2020, 3);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('I Put a Spell on You', 1965, 4);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Baltimore', 1978, 4);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Here Comes the Sun', 1971, 4);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Fodder on My Wings', 1982, 4);
-- INSERT INTO albums (title, release_year, social_network_id) VALUES ('Ring Ring', 1973, 2);



## Exercise

Your assignment is to test-drive a social network program. You should:

1. Set up a new project called `social_network` from the
   [starter](https://github.com/makersacademy/databases-in-python-project-starter).

2. Use the [Two Tables Design Recipe](../resources/two_table_design_recipe_template.md)
   to design and create a table for the following user stories:

   ```
   As a social network user,
   So I can have my information registered,
   I'd like to have a user account with my email address.

   As a social network user,
   So I can have my information registered,
   I'd like to have a user account with my username.

   As a social network user,
   So I can write on my timeline,
   I'd like to create posts associated with my user account.

   As a social network user,
   So I can write on my timeline,
   I'd like each of my posts to have a title and a content.

   As a social network user,
   So I can know who reads my posts,
   I'd like each of my posts to have a number of views.
   ```

3. Create a `seeds/social_network.sql`.

4. Test-drive the application to meet the user stories above.
    => make sure tables are linked correctly and working together to display results
    => apply all changes to app.py to see if app works
        => create users, access posts by user



# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
```

```
Nouns:

users: username, email
posts: user_id, title, content, views
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| users                 | username, email                |
| posts                 | user_id, title, content, views |

1. Name of the first table (always plural): `users` 

    Column names: `username`, `email`

2. Name of the second table (always plural): `posts` 

    Column names: `user_id`, `title`, `content`, `views`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
id: SERIAL
username: text
email: text

Table: posts
id: SERIAL
user_id: int
title: text
content: text
views: int
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one user have many posts? (Yes)
2. Can one post have many users? (No)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

Replace the relevant bits in this example with your own:

```
# EXAMPLE

1. Can one user have many posts? YES
2. Can one post have many users? NO

-> Therefore,
-> A user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.
```

*If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).*

## 5. Write the SQL

```sql
-- EXAMPLE
-- file: social_network.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username text,
  email text
);

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

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 social_network < seeds/social_network.sql
```
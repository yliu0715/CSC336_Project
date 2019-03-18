-- To start the mysql shell:
-- $ mysql -u USERNAME -p
--
-- To automatically use a database:
-- $ mysql -u USERNAME -p DATABASE
--
-- You will then be prompted for your password.

-- Here we are initializing our database and relations.
-- We will populate them with an external script.

USE DB1;

-- CREATE DATABASE Example;

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Skills;
DROP TABLE IF EXISTS Profile;
DROP TABLE IF EXISTS Recruitment;
DROP TABLE IF EXISTS Accomplishments;

CREATE TABLE User(
    userID VARCHAR(128),
    password VARCHAR(128),
    firstname VARCHAR(128),
    lastname VARCHAR(128),
    enail VARCHAR(128),
    phone INTEGER
);

CREATE TABLE Skills(
    name VARCHAR(128),
    type VARCHAR(128)
);

CREATE TABLE Profile(
    userID VARCHAR(128),
    avatar VARCHAR(128),
    skills VARCHAR(128),
    accomplishments VARCHAR(128),
    location VARCHAR(128)
);

CREATE TABLE Recruitment(
    host VARCHAR(128),
    members VARCHAR(128),
    description VARCHAR(128),
    requirements VARCHAR(128)
);

CREATE TABLE Accomplishments(
    userID VARCHAR(128),
    accomplishmentName VARCHAR(128),
    descriptions VARCHAR(128),
    verification VARCHAR(128)
);
create table City(
city_name varchar(20) primary key
);


-------------------------
-- Create Cocktails table
-------------------------

CREATE TABLE  Cocktail 
(
cocktail_name varchar(50) NOT NULL PRIMARY KEY
);

-------------------------
-- Create Human table
-------------------------

CREATE TABLE human
(
human_name varchar(50) PRIMARY KEY
);

-------------------------
-- Create Bar table
-------------------------

CREATE TABLE Bar
(
bar_name varchar(50) PRIMARY KEY
, city_name varchar(50) references City(city_name)
);

-------------------------
-- Create humanBar table
-------------------------

create table humanBar(
human_name varchar(50) references human(human_name),
bar_name varchar(50) references Bar(bar_name),
primary key(human_name)
);

-------------------------
-- Create humancocktail table
-------------------------

create table HumanCocktail(
cocktail_name varchar(50) references Cocktail(cocktail_name),
human_name varchar(50) references human(human_name),
primary key(cocktail_name)
);




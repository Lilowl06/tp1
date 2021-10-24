create database if not exists app;
use app;

create table if not exists recueilCitations(
    id int auto_increment primary key,
    citation varchar(500),
    auteur varchar(255)
);
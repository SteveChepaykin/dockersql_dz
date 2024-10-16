create database if not exists mydb;
use mydb;

create table if not exists users (
    name varchar(255),
    age int
);
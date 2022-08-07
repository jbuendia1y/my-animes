DROP DATABASE IF EXISTS `my_animes`;
CREATE DATABASE my_animes;

USE my_animes;

DROP TABLE IF EXISTS `users`;
CREATE TABLE users(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    password TEXT NOT NULL
);

DROP TABLE IF EXISTS `animes`;
CREATE TABLE animes(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    slug VARCHAR(100) NOT NULL,
    image TEXT NOT NULL,
    title VARCHAR(100) NOT NULL,
    synopsis TEXT NOT NULL,
    total_chapters INT NOT NULL,
    sequel TEXT NULL,
    prequel TEXT NULL
);

DROP TABLE IF EXISTS `chapters`;
CREATE TABLE chapters(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    image TEXT NOT NULL,
    title VARCHAR(100) NOT NULL,
    video_path TEXT NOT NULL,
    anime_id INT,
    KEY anime_id_idx (anime_id)
)

DROP TABLE IF EXISTS `user_anime`;
CREATE TABLE user_anime(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    anime_id INT,
    user_id INT,
    KEY anime_id_idx (anime_id),
    KEY user_id_idx (user_id)
);
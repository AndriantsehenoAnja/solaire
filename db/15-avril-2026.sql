-- DROP DATABASE solaire;
-- GO
CREATE DATABASE solaire;
GO
USE solaire;
GO
-- Création des tables 
CREATE TABLE Materielle(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    debutH time not null,
    finH time not null,
    consomation DECIMAL(10,2) NOT NULL
);
GO

CREATE TABLE PeriodeJ(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    debutH time not null,
    finH time not null
);
GO

CREATE TABLE Panneaux(
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    consomation DECIMAL(10,2) NOT NULL,
    coef INT NOT NULL,
    prix DECIMAL(10,2) NOT NULL
);

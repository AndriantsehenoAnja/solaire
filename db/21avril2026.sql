use solaire;
CREATE TABLE jours(
    id INT PRIMARY KEY,
    prixU DECIMAL(10,2) NOT NULL
);
INSERT INTO jours(id,prixU) VALUES
(1,200),
(2,300);
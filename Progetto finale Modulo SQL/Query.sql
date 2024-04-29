-- Creazione Tabella "Product"
CREATE TABLE Product (
	ProductID INT PRIMARY KEY NOT NULL,
	ProductName VARCHAR (250),
	ProductCategory VARCHAR (250),
 	ProductPrice DECIMAL (6,2)
	);

-- Popolamento Tabella "Product"
INSERT INTO Product (ProductID, ProductName, ProductCategory, ProductPrice) VALUES
('1', 'Bambola Sirenetta', 'Tematici', 39.50),
('2', 'Lego Star Wars', 'Costruzioni', 149.99),
('3', 'Macchina telecomandata', 'Elettronici', 187.23),
('4', 'Puzzle 3D', 'Educativi', 149.99),
('5', 'Lego Harry Potter', 'Costruzioni', 179.99),
('6', 'Pallone da calcio', 'Sportivi', 76.54),
('7', 'Cucina giocattolo', 'Creativi', 349.99),
('8', 'Allegro chirurgo', 'Giochi da Tavolo', 68.99),
('9', 'Treno telecomandato', 'Elettronici', 108.87),
('10', 'Cluedo', 'Giochi da Tavolo', 45.99),
('11', 'Kit Pongo', 'Creativi', 26.99),
('12', 'Robot Emilio', 'Elettronici', 386.99),
('13', 'Monopoly', 'Giochi da Tavolo', 45.99),
('14', 'Bicicletta Mountain Bike', 'Sportivi', 399.99),
('15', 'Risiko', 'Giochi da Tavolo', 49.45),
('16', 'Assassin\'s Creed: Valhalla', 'Videogiochi', 70.99),
('17', 'Bambola Biancaneve', 'Tematici', 65.99),
('18', 'Playstation 5', 'Videogiochi', 579.99),
('19', 'Piccolo chimico', 'Educativi', 53.76),
('20', 'FIFA 23', 'Videogiochi', 78.99),
(21, 'Fallout', 'Videogiochi', 52.35); 

-- Creazione Tabella "Region"
CREATE TABLE Region (
	RegionID INT PRIMARY KEY NOT NULL,
        RegionName VARCHAR (100),
	Country VARCHAR (100)
 	);

-- Popolamento Tabella "Region"
INSERT INTO Region (RegionID, RegionName, Country) VALUES
(1, 'Europe', 'Germany'),
(2, 'North America', 'USA'),
(3, 'Europe', 'France'),
(4, 'North America', 'Canada'),
(5, 'Europe', 'Italy'),
(6, 'North America', 'Mexico'),
(7, 'South America', 'Brazil'),
(8, 'Europe', 'Spain'),
(9, 'South America', 'Argentina'),
(10, 'Asia', 'Japan'),
(11, 'South America', 'Colombia'),
(12, 'Asia', 'China'),
(13, 'Europe', 'United Kingdom'),
(14, 'Asia', 'South Korea'),
(15, 'Oceania', 'Australia'),
(16, 'Africa', 'South Africa'),
(17, 'Oceania', 'New Zealand'),
(18, 'Africa', 'Nigeria'),
(19, 'Oceania', 'Fiji'),
(20, 'Africa', 'Egypt');

-- Creazione Tabella "Sales"
CREATE TABLE Sales (
	SalesID INT PRIMARY KEY NOT NULL,
	SalesDate DATE,
	SalesQuantity INT,
	SalesPrice DECIMAL (6,2),
	ProductID_FK INT,
	FOREIGN KEY (ProductID_FK) REFERENCES Product (ProductID),
	RegionID_FK INT,
	FOREIGN KEY (RegionID_FK) REFERENCES Region (RegionID)
 	);

-- Popolamento Tabella "Sales"
INSERT INTO Sales (SalesID, SalesDate, SalesQuantity, SalesPrice, ProductID_FK, RegionID_FK) VALUES
(1, '2022-01-03', 10, 395.00, 1, 5),
(2, '2022-01-05', 5, 749.95, 2, 2),
(3, '2022-01-08', 3, 562.47, 3, 6),
(4, '2023-02-10', 8, 1199.92, 4, 7),
(5, '2023-02-12', 2, 359.98, 5, 10),
(6, '2023-03-15', 7, 535.78, 6, 3),
(7, '2023-03-18', 4, 139.96, 7, 15),
(8, '2023-04-20', 6, 413.94, 8, 1),
(9, '2023-04-23', 9, 980.83, 9, 16),
(10, '2023-05-25', 1, 45.99, 10, 11),
(11, '2023-06-28', 5, 134.95, 11, 4),
(12, '2023-07-01', 3, 1160.97, 12, 8),
(13, '2023-08-03', 10, 459.90, 13, 14),
(14, '2023-08-06', 2, 799.98, 14, 19),
(15, '2023-09-08', 8, 395.92, 15, 9),
(16, '2023-09-11', 4, 283.96, 16, 20),
(17, '2023-10-14', 7, 461.93, 17, 12),
(18, '2023-10-16', 6, 347.94, 18, 3),
(19, '2023-11-19', 9, 2429.91, 19, 5),
(20, '2023-11-21', 1, 349.99, 20, 17),
(21, '2024-01-24', 5, 157.45, 1, 18),
(22, '2024-02-26', 3, 563.67, 2, 16),
(23, '2024-03-29', 8, 179.92, 3, 12),
(24, '2024-04-01', 2, 215.98, 4, 9),
(25, '2024-05-03', 7, 1679.93, 5, 2),
(26, '2024-06-06', 4, 307.96, 6, 20),
(27, '2024-07-09', 6, 236.94, 7, 1),
(28, '2024-08-11', 9, 689.91, 8, 7),
(29, '2024-09-14', 1, 70.99, 9, 18),
(30, '2024-10-17', 5, 224.95, 10, 3);

-- Esporre l’elenco dei soli prodotti venduti e per ognuno di questi il fatturato totale per anno
SELECT
   P.ProductName AS Prodotto,
   P.ProductID,
   YEAR (S.SalesDate) AS Anno,
   SUM(S.SalesPrice) AS FatturatoTot,
   SUM(S.SalesQuantity) AS QuantitaTot
FROM
   Sales AS S
INNER JOIN
   Product AS P ON S.ProductID_FK = P.ProductID
GROUP BY
   P.ProductName, 
   ProductID, 
   YEAR (S.SalesDate)
ORDER BY
   P.ProductName, 
   YEAR (S.SalesDate);

-- Esporre il fatturato totale per stato per anno. Ordina il risultato per data e per fatturato decrescente
SELECT
   Country AS Stato,
   YEAR (S.SalesDate) AS Anno,
   SUM(S.SalesPrice) AS FatturatoTot
FROM
   Sales AS S
INNER JOIN 
   Region AS R ON S.RegionID_FK = R.RegionID
GROUP BY
   R.Country,
YEAR (S.SalesDate)
ORDER BY
   Country DESC, 
   FatturatoTot DESC, 
   YEAR (S.SalesDate) DESC;

-- Rispondere alla seguente domanda: qual è la categoria di articoli maggiormente richiesta dal mercato?
SELECT
   P.ProductCategory AS Categoria,
   SUM(S.SalesQuantity) AS TotQuantitaVenduta
FROM
   Product AS P
INNER JOIN
   Sales AS S ON P.ProductID = S.ProductID_FK
GROUP BY
   P.ProductCategory
ORDER BY
  TotQuantitaVenduta  DESC
LIMIT 1;

-- Rispondere alla seguente domanda: quali sono, se ci sono, i prodotti invenduti? Proponi due approcci risolutivi differenti
-- APPROCCIO N°1
SELECT ProductID, ProductName, ProductCategory
FROM Product
WHERE ProductID NOT IN (SELECT DISTINCT ProductID_FK FROM Sales);
-- APPROCCIO N°2
SELECT P.ProductID, P.ProductName, P.ProductCategory
FROM Product AS P
LEFT JOIN Sales AS S ON P.ProductID = S.ProductID_FK
WHERE S.ProductID_FK IS NULL;

-- Esporre l’elenco dei prodotti con la rispettiva ultima data di vendita (la data di vendita più recente).
SELECT 
    P.ProductID, 
    P.ProductName, 
    P.ProductCategory, 
    MAX(S.SalesDate) AS UltimaDataVendita
FROM 
    Product AS P
LEFT JOIN 
    Sales AS S ON P.ProductID = S.ProductID_FK
GROUP BY 
    P.ProductID, P.ProductName, P.ProductCategory;





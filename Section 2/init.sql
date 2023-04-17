CREATE TABLE items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(50) NOT NULL,
    manufacturer_name VARCHAR(100) NOT NULL,
    item_cost FLOAT NOT NULL,
    item_weight FLOAT NOT NULL
);

INSERT INTO items VALUES (0, 'Toothpaste', 'smiles', 10.24, 10000.1);
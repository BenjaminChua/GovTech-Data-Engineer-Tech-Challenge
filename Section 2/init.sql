CREATE TABLE items (
  item_id INT PRIMARY KEY,
  item_name VARCHAR(50) NOT NULL,
  manufacturer_name VARCHAR(100) NOT NULL,
  item_cost NUMERIC NOT NULL,
  item_weight NUMERIC NOT NULL
);

INSERT INTO items
VALUES 
  (0, 'Toothpaste', 'smiles', 3.24, 0.0533),
  (1, 'Toothbrush', 'smiles', 2.51, 0.011),
  (2, 'Mouth Wash', 'frowns', 11.51, 0.234511),
  (3, 'Dental Floss', 'frowns', 4.23, 0.061),
  (4, 'Moisturiser', 'cleans', 20.1, 0.52);

CREATE TABLE members (
  membership_id VARCHAR(50) PRIMARY KEY,
  member_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  date_of_birth VARCHAR(8) NOT NULL,
  mobile_no VARCHAR(8) NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  above_18 BOOLEAN NOT NULL
);

INSERT INTO members
VALUES
  ('Smith_c7677', 'Patty Smith',	'Patty_Smith@ross.com',	19750827,	59428759,	'Patty',	'Smith',	TRUE),
  ('Wang_04168', 'Sean Wang DDS',	'Sean_Wang@gibson-calderon.com',	19600311,	25595367,	'Sean',	'Wang',	TRUE),
  ('Estrada_0bf5b', 'Richard Estrada',	'Richard_Estrada@malone.com',	19921015,	22821527,	'Richard',	'Estrada',	TRUE),
  ('Cline_825fb', 'Jackson Cline',	'Jackson_Cline@hudson.net',	19710121,	48056519,	'Jackson',	'Cline',	TRUE),
  ('Williams_3e726', 'Allen Williams',	'Allen_Williams@sanchez.net',	19971109,	77991519,	'Allen',	'Williams',	TRUE);

CREATE TABLE transactions (
  transaction_id INT PRIMARY KEY,
  membership_id VARCHAR(50) REFERENCES members(membership_id),
  total_price NUMERIC NOT NULL,  
  total_weight NUMERIC NOT NULL
);

INSERT INTO transactions
VALUES
  (0, 'Smith_c7677', 8.26, 0.0753),
  (1, 'Wang_04168', 108.96, 2.722),
  (2, 'Smith_c7677', 34.53, 0.703533),
  (3, 'Wang_04168', 7.53, 0.033),
  (4, 'Estrada_0bf5b', 3.24, 0.0533),
  (5, 'Smith_c7677', 20.1, 0.52),
  (6, 'Cline_825fb', 112.01, 2.834511),
  (7, 'Williams_3e726', 21.22, 0.2885),
  (8, 'Williams_3e726', 41.52, 0.8552),
  (9, 'Smith_c7677', 2.51, 0.011);

CREATE TABLE transaction_items (
  id INT PRIMARY KEY,
  transaction_id INT REFERENCES transactions(transaction_id),
  item_id INT REFERENCES items(item_id),  
  quantity INT NOT NULL
);

INSERT INTO transaction_items
VALUES
  (0, 0, 0, 1),
  (1, 0, 1, 2),
  (2, 1, 3, 1),
  (3, 1, 4, 5),
  (4, 1, 3, 1),
  (5, 2, 2, 2),
  (6, 2, 2, 1),
  (7, 3, 1, 3),
  (8, 4, 0, 1),
  (9, 5, 4, 1),
  (10, 6, 4, 5),
  (11, 6, 2, 1),
  (12, 7, 1, 2),
  (13, 7, 0, 1),
  (14, 7, 0, 3),
  (15, 7, 0, 1),
  (16, 8, 4, 1),
  (17, 8, 3, 2),
  (18, 8, 0, 4),
  (19, 9, 1, 1);
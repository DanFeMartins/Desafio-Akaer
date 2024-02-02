-- Create TABLE products(
--     id INTEGER NOT NULL primary key,
--     name VARCHAR(255),
--     amount integer,
--     price float,
--     id_categories integer,
--     FOREIGN Key (id_categories) REFERENCES categories(id)
-- );


-- Create TAble categories(
--     id INTEGER NOT NULL PRIMARY key,
--     name VARCHAR(255)
-- );

-- insert into products(name, amount,price, id_categories)
-- VALUES
--     ('Two-doors wardrobe', 100, 800, 1),
--     ('Dining table', 1000, 560, 3),
--     ('Towel holder', 10000, 25.50, 4),
--     ('Computer desk', 350, 320.50, 2),
--     ('chair', 3000, 210.64, 4),
--     ('single bed', 750, 460,1);


-- insert into categories(name)
-- VALUES
--     ('wood'),
--     ('luxury'),
--     ('vintage'),
--     ('modern'),
--     ('super luxury');

SELECT
    p.name AS product_name, p.amount, c.name AS category_name
FROM 
    categories c
JOIN
    products p
ON
    p.id_categories = c.id;


-- select * from categories
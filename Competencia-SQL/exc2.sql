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
--     ('Blue Chair', 30, 300.00, 9),
--     ('Red Chair', 200, 2150.00, 2),
--     ('Disney Wardrobe', 400, 829.50, 4),
--     ('Blue Toaster', 20, 9.90, 3),
--     ('Solar Panel', 30, 3000.25, 4);

-- insert into categories(id, name)
-- VALUES
--     (1,'Superior'),
--     (2,'Super Luxury'),
--     (3,'Modern'),
--     (4,'Nerd'),
--     (5,'Infantile'),
--     (6,'Robust'),
--     (9,'Wood');


-- select * from categories;

SELECT 
    p.name, c.name
FROM
    products p
JOIN
    categories c
ON
    c.id = p.id_categories
WHERE
    p.amount > 100 and c.id NOT IN (4, 5);









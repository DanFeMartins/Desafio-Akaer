-- CREATE TABLE customers (
--     id INTEGER NOT NULL PRIMARY KEY,
--     name VARCHAR(255),
--     street VARCHAR(255),
--     city VARCHAR(255),
--     state CHAR(2),
--     credit_limit INTEGER
-- );

-- drop table customers;

-- INSERT INTO customers (name, street, city, state, credit_limit)
-- VALUES 
--     ('Nicolas Diogo Cardoso', 'Acesso Um', 'Cidade do Cliente', 'RS', 475),
--     ('Cecília Olivia Rodrigues', 'Rua Sizuka Usuy', 'Cianorte', 'PR', 3170),
--     ('Augusto fernando Carlos Eduardo CArdoso', 'Rua Baldomiro Koerich', 'Palhoça', 'SC', 1067),
--     ('Nicolas Diogo Cardoso', 'Acesso Um', 'Cidade do Cliente', 'RS', 475),
--     ('Sabrina Heloisa Gabriela Barros', 'Rua Engenehiro TIto Marques Fernandes', 'Porto Alegre', 'RS', 4312),
--     ('Joaquim Diego Lorenzo Araújo', 'Rua Vitoriano', 'Novo Hamburgo', 'RS', 2314);

-- SELECT * FROM customers;

-- CREATE TABLE orders (
--     id INTEGER NOT NULL PRIMARY KEY,
--     orders_date DATE,
--     id_customers INTEGER,
--     FOREIGN Key (id_customers) REFERENCES customers(id)

-- );

-- INSERT into orders(id, orders_date, id_customers)
-- VALUES
--     (1,'2016-05-13', 3),
--     (2,'2016-01-12', 2),
--     (3,'2016-04-18', 5),
--     (4,'2016-00-07', 4),
--     (5,'2016-02-13', 6),
--     (6,'2016-08-05', 3);



-- SELECT * FROM orders;

-- SELECT * From customers;

select 
    c.name, o.id
FROM
    customers c
JOIN
    orders o 
ON
    c.id = o.id_customers
AND
    o.orders_date >= '2016-01-01' 
AND
    o.orders_date < '2016-06-31'


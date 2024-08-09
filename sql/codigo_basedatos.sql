-- Crear base de datos
CREATE DATABASE IF NOT EXISTS inventario;

-- escoger la base de datos donde se crearan las tablas
USE inventario;

CREATE TABLE IF NOT EXISTS catergorias(idCategoria int PRIMARY KEY AUTO_INCREMENT,
                                      nombreCategoria varchar(100) UNIQUE NOT NULL);
CREATE TABLE IF NOT EXISTS productos(idProductos varchar(5) PRIMARY KEY,
                                     nombreProducto varchar(1000) UNIQUE NOT NULL,
                                     idCategoria int,
                                     
                                     CONSTRAINT fk01 FOREIGN KEY (idCategoria) REFERENCES catergorias(idCategoria) ON UPDATE CASCADE ON DELETE RESTRICT);

-- Usar la base de datos
USE tursmo_db1;

-- Crear tabla guia_turistica
CREATE TABLE guia_turistica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

-- Crear tabla guia
CREATE TABLE guia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    guia_turistica_id INT NOT NULL,
    FOREIGN KEY (guia_turistica_id) REFERENCES guia_turistica(id)
);

-- Crear tabla lugar
CREATE TABLE lugar (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    guia_turistica_id INT NOT NULL,
    FOREIGN KEY (guia_turistica_id) REFERENCES guia_turistica(id)
);

-- Crear tabla actividad
CREATE TABLE actividad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    lugar_id INT NOT NULL,
    FOREIGN KEY (lugar_id) REFERENCES lugar(id)
);


-- Crea una nueva base de datos para tu proyecto
CREATE DATABASE prueba_desarrollo2;

-- Utiliza la base de datos recién creada
USE prueba_desarrollo2;

-- Crea una tabla para almacenar los datos de los alumnos
CREATE TABLE alumnos (
    codigo_alumno INT AUTO_INCREMENT PRIMARY KEY,
    apellido_paterno VARCHAR(50),
    apellido_materno VARCHAR(50),
    nombres VARCHAR(100),
    carrera_profesional VARCHAR(100),
    domicilio VARCHAR(200),
    fecha_nacimiento DATE
);
SELECT * FROM alumnos;
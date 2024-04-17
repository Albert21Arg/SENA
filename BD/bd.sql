CREATE DATABASE IF NOT EXISTS escuela_rita;

-- escoger la base de datos donde se crearan las tablas
USE escuela_rita;
-- Padres
CREATE TABLE IF NOT EXISTS padres (
    idPadre INT PRIMARY KEY AUTO_INCREMENT,
    cedula INT(60) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL
);
-- Madres
CREATE TABLE IF NOT EXISTS Madres(
    idMadre INT PRIMARY KEY AUTO_INCREMENT,
    cedula INT(10) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL
);
-- Acudientes
CREATE TABLE IF NOT EXISTS  Acudientes(
    idAcudientes INT PRIMARY KEY AUTO_INCREMENT,
    cedula INT(10) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL
);
-- Matriculas
CREATE TABLE IF NOT EXISTS matriculas (idMatricula INT PRIMARY KEY AUTO_INCREMENT,
	  									fechaMatricula DATE
);
-- Grupos
CREATE TABLE IF NOT EXISTS Grupos(idGrupo INT PRIMARY KEY AUTO_INCREMENT,
                                  descripcion VARCHAR(50) NOT NULL                                    
                );
-- Maestros
CREATE TABLE IF NOT EXISTS Maestros (idMaestro INT PRIMARY KEY AUTO_INCREMENT,
                                    cedula INT(10) UNIQUE NOT NULL,
                                    nombre VARCHAR(20) NOT NULL,
                                    apellido VARCHAR(20) NOT NULL,
                                    fechaNacimiento DATE NOT NULL,
                                    telefono INT(11) NOT NULL,
                                    profesion VARCHAR(50) NOT NULL
);
-- MaestrosGrupos
CREATE TABLE IF NOT EXISTS MaestrosGrupos(idMaestros INT,
                                          idGrupos INT,
                                          CONSTRAINT fk0 FOREIGN KEY (idMaestro) REFERENCES Maestros(idMaestro) ON UPDATE CASCADE ON DELETE RESTRICT,
                                          CONSTRAINT fk0 FOREIGN KEY (idGrupo) REFERENCES Grupos(idGrupo) ON UPDATE CASCADE ON DELETE RESTRICT
);
                
-- Estudiantes
CREATE TABLE IF NOT EXISTS Estudiantes (idEstudiante INT PRIMARY KEY AUTO_INCREMENT,
                                        identificacion INT UNIQUE NOT NULL,
                                        primerNombre VARCHAR(20) NOT NULL,
                                        segundoNombre VARCHAR(20),
                                        primerApellido VARCHAR(20) NOT NULL,
                                        segundoApellido VARCHAR(20),
                                        fechaNacimiento DATE NOT NULL,
                                        telefono BIGINT(11),
                                        tipoSangre VARCHAR(3) NOT NULL,
                                        fechaMatricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Habilidades
CREATE TABLE IF NOT EXISTS habilidades (idHabilidad INT PRIMARY KEY AUTO_INCREMENT,
    									descripcion VARCHAR(100) NOT NULL
);
-- EstudiantesHabilidades
CREATE TABLE IF NOT EXISTS EstudiantesHabilidades(EstudiantesHabilidades INT PRIMARY KEY AUTO_INCREMENT,
                                               idEstudiante INT ,
                                               idHabilidad	INT ,
                                               CONSTRAINT fk0 FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante) ON UPDATE CASCADE ON DELETE RESTRICT,
                                               CONSTRAINT fk0 FOREIGN KEY (idHabilidad) REFERENCES Habilidad(idHabilidad) ON UPDATE CASCADE ON DELETE RESTRICT
                                              );
-- Alergias
CREATE TABLE IF NOT EXISTS Alergias(idAlergia INT PRIMARY KEY AUTO_INCREMENT,
                                    descripcion VARCHAR (100)UNIQUE
);
-- EstudiantesAlergias
CREATE TABLE IF NOT EXISTS EstudiantesAlergias(idEstudiantesAlergias INT PRIMARY KEY AUTO_INCREMENT,
                                               idEstudiante INT ,
                                               idAlergia	INT ,
                                               CONSTRAINT fk0 FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante) ON UPDATE CASCADE ON DELETE RESTRICT,
                                               CONSTRAINT fk0 FOREIGN KEY (idAlergia) REFERENCES Alergias(idAlergia) ON UPDATE CASCADE ON DELETE RESTRICT
                                              );

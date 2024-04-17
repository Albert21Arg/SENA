CREATE DATABASE IF NOT EXISTS escuela_rita;

-- escoger la base de datos donde se crearan las tablas
USE escuela_rita;
-- Padres
CREATE TABLE IF NOT EXISTS padres (idPadre INT PRIMARY KEY AUTO_INCREMENT,
                                   cedula INT(60) UNIQUE NOT NULL,
                                   nombre VARCHAR(20) NOT NULL,
                                   apellido VARCHAR(20) NOT NULL,
                                   fechaNacimiento DATE NOT NULL,
                                   telefono INT(11) NOT NULL
                                  );
-- Madres
CREATE TABLE IF NOT EXISTS Madres(idMadre INT PRIMARY KEY AUTO_INCREMENT,
	                             cedula INT(10) UNIQUE NOT NULL,
	                             nombre VARCHAR(20) NOT NULL,
	                             apellido VARCHAR(20) NOT NULL,
	                             fechaNacimiento DATE NOT NULL,
		                         telefono INT(11) NOT NULL
                                 );
-- Acudientes
CREATE TABLE IF NOT EXISTS  Acudientes(idAcudiente INT PRIMARY KEY AUTO_INCREMENT,
                                        cedula INT(10) UNIQUE NOT NULL,
                                        nombre VARCHAR(20) NOT NULL,
                                        apellido VARCHAR(20) NOT NULL,
                                        fechaNacimiento DATE NOT NULL,
                                        telefono INT(11) NOT NULL
                                      );
-- Matriculas
CREATE TABLE IF NOT EXISTS matriculas (idMatricula INT PRIMARY KEY AUTO_INCREMENT,
	  									fechaMatricula TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
CREATE TABLE IF NOT EXISTS MaestrosGrupos(idMaestrosGrupos INT,
                                          idMaestro INT,
                                          idGrupo INT,
                                          CONSTRAINT fk01 FOREIGN KEY (idMaestro) REFERENCES Maestros(idMaestro) ON UPDATE CASCADE ON DELETE RESTRICT,
                                          CONSTRAINT fk02 FOREIGN KEY (idGrupo) REFERENCES Grupos(idGrupo) ON UPDATE CASCADE ON DELETE RESTRICT
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
                                        idPadre INT,
                                        idMadre INT,
                                        idAcudiente INT,
                                        idGrupo INT,
                                        idMatricula INT,
                                        CONSTRAINT fk03 FOREIGN KEY (idPadre) REFERENCES Padres(idPadre) ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk04 FOREIGN KEY (idMadre) REFERENCES Madres(idMadre) ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk05 FOREIGN KEY (idAcudiente) REFERENCES Acudientes(idAcudiente) ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk06 FOREIGN KEY (idGrupo) REFERENCES Grupos(idGrupo) ON UPDATE CASCADE ON DELETE RESTRICT,
                                        CONSTRAINT fk07 FOREIGN KEY (idMatricula) REFERENCES Matriculas(idMatricula) ON UPDATE CASCADE ON DELETE RESTRICT
                                       );
-- Habilidades
CREATE TABLE IF NOT EXISTS habilidades (idHabilidad INT PRIMARY KEY AUTO_INCREMENT,
    									descripcion VARCHAR(100) NOT NULL);
-- EstudiantesHabilidades
CREATE TABLE IF NOT EXISTS EstudiantesHabilidades(EstudiantesHabilidades INT PRIMARY KEY AUTO_INCREMENT,
                                               idEstudiante INT ,
                                               idHabilidad	INT ,
                                               CONSTRAINT fk08 FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante) ON UPDATE CASCADE ON DELETE RESTRICT,
                                               CONSTRAINT fk09 FOREIGN KEY (idHabilidad) REFERENCES Habilidades(idHabilidad) ON UPDATE CASCADE ON DELETE RESTRICT
                                              );
-- Alergias
CREATE TABLE IF NOT EXISTS Alergias(idAlergia INT PRIMARY KEY AUTO_INCREMENT,
                                    descripcion VARCHAR (100)UNIQUE
                                   );
-- EstudiantesAlergias
CREATE TABLE IF NOT EXISTS EstudiantesAlergias(idEstudiantesAlergias INT PRIMARY KEY AUTO_INCREMENT,
                                               idEstudiante INT ,
                                               idAlergia	INT ,
                                               CONSTRAINT fk10 FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante) ON UPDATE CASCADE ON DELETE RESTRICT,
                                               CONSTRAINT fk11 FOREIGN KEY (idAlergia) REFERENCES Alergias(idAlergia) ON UPDATE CASCADE ON DELETE RESTRICT
                                              );
-- EstudiantesMaestros 
CREATE TABLE IF NOT EXISTS EstudiantesMaestros (idEstudiantesMaestros INT PRIMARY KEY AUTO_INCREMENT,
                                               idEstudiante INT ,
                                               idMaestro	INT ,
                                               CONSTRAINT fk12 FOREIGN KEY (idEstudiante) REFERENCES Estudiantes(idEstudiante) ON UPDATE CASCADE ON DELETE RESTRICT,
                                               CONSTRAINT fk13 FOREIGN KEY (idMaestro) REFERENCES Maestros(idMaestro) ON UPDATE CASCADE ON DELETE RESTRICT
                                               );

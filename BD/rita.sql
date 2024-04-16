CREATE DATABASE IF NOT EXISTS escuela_rita;

-- escoger la base de datos donde se crearan las tablas
USE escuela_rita;

-- Creación de la tabla 'estudiantes'
CREATE TABLE estudiantes (
    idEstudiante INT PRIMARY KEY,
    identificacion INT UNIQUE NOT NULL,
    primerNombre VARCHAR(20) NOT NULL,
    segundoNombre VARCHAR(20),
    primerApellido VARCHAR(20) NOT NULL,
    segundoApellido VARCHAR(20),
    fechaNacimiento DATE NOT NULL,
    telefono INT(11),
    tipoSangre VARCHAR(3) NOT NULL,
    fechaMatricula DATE NOT NULL
);
-- Creación de la tabla 'grupos'
CREATE TABLE grupos (
    idGrupo INT PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL,
    idEstudiante INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

-- Creación de la tabla 'padres'
CREATE TABLE padres (
    idPadre INT PRIMARY KEY,
    cedula INT(60) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL,
    idEstudiante INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

-- Creación de la tabla 'madres'
CREATE TABLE madres (
    idMadre INT PRIMARY KEY,
    cedula INT(10) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL,
    idEstudiante INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

-- Creación de la tabla 'acudientes'
CREATE TABLE acudientes (
    idAcudientes INT PRIMARY KEY,
    cedula INT(10) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL,
    idEstudiante INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

-- Creación de la tabla 'habilidades'
CREATE TABLE habilidades (
    idHabilidad INT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

-- Creación de la tabla 'alergias'
CREATE TABLE alergias (
    idAlergias INT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

-- Creación de la tabla 'maestros'
CREATE TABLE maestros (
    idMaestro INT PRIMARY KEY,
    cedula INT(10) UNIQUE NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fechaNacimiento DATE NOT NULL,
    telefono INT(11) NOT NULL,
    profesion VARCHAR(50) NOT NULL
);

-- Creación de la tabla 'matriculas'
CREATE TABLE matriculas (
    idMatricula INT PRIMARY KEY,
    fechaMatricula DATE,
    idEstudiante INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

-- Creación de la tabla 'alergiasEstudiantes'
CREATE TABLE alergiasEstudiantes (
    idAlergiaEstudiante INT PRIMARY KEY,
    idEstudiante INT,
    idAlergia INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante),
    FOREIGN KEY (idAlergia) REFERENCES alergias(idAlergias)
);

-- Creación de la tabla 'habilidadesEstudiantes'
CREATE TABLE habilidadesEstudiantes (
    idHabilidadEstudiante INT PRIMARY KEY,
    idEstudiante INT,
    idHabilidad INT,
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante),
    FOREIGN KEY (idHabilidad) REFERENCES habilidades(idHabilidad)
);

-- Creación de la tabla 'maestrosGrupos'
CREATE TABLE maestrosGrupos (
    idMaestroGrupo INT PRIMARY KEY,
    idMaestro INT,
    idGrupo INT,
    FOREIGN KEY (idMaestro) REFERENCES maestros(idMaestro),
    FOREIGN KEY (idGrupo) REFERENCES grupos(idGrupo)
);

-- Creación de la tabla 'maestroestudiante'
CREATE TABLE maestroestudiante (
    idMaestroEstudiante INT PRIMARY KEY,
    idMaestro INT,
    idEstudiante INT,
    FOREIGN KEY (idMaestro) REFERENCES maestros(idMaestro),
    FOREIGN KEY (idEstudiante) REFERENCES estudiantes(idEstudiante)
);

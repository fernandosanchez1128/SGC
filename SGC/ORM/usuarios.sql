--USUARIOS
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('001', 'Andres', 'Perez', 'a@.com', '123', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('002', 'Andres', 'Roa', 'b@.com', '124', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('003', 'Miguel', 'Murillo', 'c@.com', '125', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('004', 'Pecoso', 'Castro', 'd@.com', '126', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('005', 'Heli', 'Palacios', 'e@.com', '127', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('006', 'Harold', 'Preciado', 'f@.com', '128', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('007', 'Coco', 'Perea', 'g@.com', '129', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('008', 'Camello', 'Serna', 'h@.com', '130', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('009', 'Wilson', 'Carpintero', 'i@.com', '131', 'coordinador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('010', 'Carmelo', 'Valencia', 'j@.com', '132', 'digitador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('011', 'Pelicano', 'Banguero', 'k@.com', '133', 'digitador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('012', 'Fantasma', 'Ballesteros', 'l@.com', '134', 'digitador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('013', 'Galvan', 'Rey', 'm@.com', '135', 'digitador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('014', 'Chicho', 'Serna', 'n@.com', '136', 'digitador');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('015', 'Edixon', 'Perea', 'o@.com', '137', 'leaderteacher');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('016', 'Pitufo', 'DeAvila', 'p@.com', '138', 'leaderteacher');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('017', 'Jaime', 'Castrillon', 'q@.com', '139', 'masterteacher');
insert into usuario (cedula, nombres, apellidos, correo_electronico, contrasena, type) values ('018', 'Tressor', 'Moreno', 'r@.com', '140', 'masterteacher');


--LT
insert into leaderteacher (cedula , dpto_secretaria) values ('001', 'Valle del Cauca');
insert into leaderteacher (cedula , dpto_secretaria) values ('002', 'Cauca');
insert into leaderteacher (cedula , dpto_secretaria) values ('003', 'Amazonas');
insert into leaderteacher (cedula , dpto_secretaria) values ('004', 'Narino');
insert into leaderteacher (cedula , dpto_secretaria) values ('005', 'Tolima');
insert into leaderteacher (cedula , dpto_secretaria) values ('006', 'Huila');
insert into leaderteacher (cedula , dpto_secretaria) values ('007', 'Caqueta');
insert into leaderteacher (cedula , dpto_secretaria) values ('008', 'Putumayo');
insert into leaderteacher (cedula , dpto_secretaria) values ('009', 'Amazonas');
insert into leaderteacher (cedula , dpto_secretaria) values ('010', 'Valle del Cauca');
insert into leaderteacher (cedula , dpto_secretaria) values ('011', 'Cauca');
insert into leaderteacher (cedula , dpto_secretaria) values ('012', 'Amazonas');
insert into leaderteacher (cedula , dpto_secretaria) values ('013', 'Narino');
insert into leaderteacher (cedula , dpto_secretaria) values ('014', 'Tolima');
insert into leaderteacher (cedula , dpto_secretaria) values ('015', 'Huila');
insert into leaderteacher (cedula , dpto_secretaria) values ('016', 'Caqueta');
insert into leaderteacher (cedula , dpto_secretaria) values ('017', 'Putumayo');
insert into leaderteacher (cedula , dpto_secretaria) values ('018', 'Amazonas');

--CURSOS
insert into curso (id, nombre) values (001, 'curso1');
insert into curso (id, nombre) values (002, 'curso2');
insert into curso (id, nombre) values (003, 'curso3');
insert into curso (id, nombre) values (004, 'curso4');
insert into curso (id, nombre) values (005, 'curso5');
insert into curso (id, nombre) values (006, 'curso6');
insert into curso (id, nombre) values (007, 'curso7');
insert into curso (id, nombre) values (008, 'curso8');
insert into curso (id, nombre) values (009, 'curso9');
insert into curso (id, nombre) values (010, 'curso10');
insert into curso (id, nombre) values (011, 'curso11');
insert into curso (id, nombre) values (012, 'curso12');
insert into curso (id, nombre) values (013, 'curso13');
insert into curso (id, nombre) values (014, 'curso14');
insert into curso (id, nombre) values (015, 'curso15');
insert into curso (id, nombre) values (016, 'curso16');
insert into curso (id, nombre) values (017, 'curso17');
insert into curso (id, nombre) values (018, 'curso18');
insert into curso (id, nombre) values (019, 'curso19');
insert into curso (id, nombre) values (020, 'curso20');

--COHORTES(curso,cohorte,ano,semestre, ini, fin)
insert into cohorte values (001, 001, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (001, 002, 2015, 1, '2015-02-01', '2015-03-15');
insert into cohorte values (001, 003, 2015, 1, '2015-01-01', '2015-02-15');

insert into cohorte values (002, 004, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (002, 005, 2015, 1, '2015-03-01', '2015-04-15');
insert into cohorte values (002, 006, 2015, 1, '2015-05-01', '2015-06-15');

insert into cohorte values (003, 007, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (003, 008, 2015, 1, '2015-03-01', '2015-04-15');

insert into cohorte values (004, 009, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (004, 010, 2015, 1, '2015-04-01', '2015-05-15');
insert into cohorte values (004, 011, 2015, 1, '2015-02-01', '2015-03-15');

insert into cohorte values (005, 012, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (005, 013, 2015, 1, '2015-01-01', '2015-02-15');

insert into cohorte values (006, 014, 2015, 1, '2015-01-01', '2015-02-15');

insert into cohorte values (007, 015, 2015, 1, '2015-03-01', '2015-04-15');

insert into cohorte values (008, 016, 2015, 1, '2015-01-01', '2015-02-15');

insert into cohorte values (009, 017, 2015, 1, '2015-01-01', '2015-02-15');

insert into cohorte values (010, 018, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (010, 019, 2015, 1, '2015-02-01', '2015-03-15');
insert into cohorte values (010, 020, 2015, 1, '2015-03-01', '2015-04-15');
insert into cohorte values (010, 021, 2015, 1, '2015-04-01', '2015-05-15');

insert into cohorte values (011, 022, 2015, 1, '2015-01-01', '2015-02-15');
insert into cohorte values (011, 023, 2015, 1, '2015-02-01', '2015-03-15');

insert into cohorte values (012, 024, 2015, 1, '2015-01-01', '2015-02-15');

--Matricula
insert into matricula values ('001', 001, 001, 3.8);
insert into matricula values ('002', 001, 002, 4.5);
insert into matricula values ('003', 001, 001, 2.0);
insert into matricula values ('004', 001, 001, 3.3);
insert into matricula values ('005', 001, 001, 3.2);
insert into matricula values ('006', 001, 001, 4.2);

insert into matricula values ('007', 002, 004, 4.3);
insert into matricula values ('008', 002, 004, 4.5);
insert into matricula values ('009', 002, 004, 4.7);
insert into matricula values ('010', 002, 005, 2.3);

insert into matricula values ('011', 003, 007, 3.9);
insert into matricula values ('012', 003, 007, 4.8);

insert into matricula values ('013', 004, 009, 5.0);
insert into matricula values ('014', 004, 009, 3.1);
insert into matricula values ('015', 004, 009, 2.5);
insert into matricula values ('016', 004, 009, 1.8);

insert into matricula values ('017', 005, 012, 3.3);
insert into matricula values ('018', 005, 012, 4.9);

--Actividades
insert into actividades values(001, 1, 'act1', 0.3);
insert into actividades values(001, 2, 'act2', 0.3);
insert into actividades values(001, 3, 'act3', 0.3);
insert into actividades values(001, 4, 'act4', 0.1);

--Notas
insert into notas values('001', 1, 001, 001, 4.5, 'true');
insert into notas values('001', 2, 001, 001, 3.0, 'true');
insert into notas values('001', 3, 001, 001, 3.5, 'true');
insert into notas values('001', 4, 001, 001, 5.0, 'true');

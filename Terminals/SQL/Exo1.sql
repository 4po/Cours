
/*Exercice sur : http://sqlfiddle.com*/

/* Création de Table sql */

create table HOTEL(NOMS_HOTEL VARCHAR(15), ADRESS VARCHAR(50),primary keY(NOMS_HOTEL));   
create table CHAMBRE(NUMERO_CH INTEGER,PRIX INTEGER, NOMS_HOTEL VARCHAR(15),primary keY(NUMERO_CH,NOMS_HOTEL), foreign key (NOMS_HOTEL) references HOTEL(NOMS_HOTEL) on delete cascade on update cascade);
create table CLIENT(NUMERO_CLI INTEGER, NOMS_CLI VARCHAR(15),PRENOMS_CLI VARCHAR(15),primary keY(NUMERO_CLI));
create table RESERVATION(NUMERO_RES INTEGER,DATE_RSA VARCHAR(50),NUMERO_CLI INTEGER,NUMERO_CH INTEGER, primary keY(NUMERO_RES), foreign key (NUMERO_CLI) references CLIENT(NUMERO_CLI) on delete cascade on update cascade,foreign key (NUMERO_CH) references CHAMBRE(NUMERO_CH) on delete cascade on update cascade);

/* Ajout de valeur dans une table */

insert into HOTEL(NOMS_HOTEL, ADRESS) values ("Love-Hotel", "1337 Ghetto du cybercrime, Neo-Tokyo"); 
insert into CLIENT(NUMERO_CLI, NOMS_CLI, PRENOMS_CLI) values (1875, "Makise", "Kurise"),(7845, "Rentaro", "Okabe"),(1337,"0x307845","0xE");
insert into CHAMBRE(NUMERO_CH,PRIX,NOMS_HOTEL) values (1,40,"Love-Hotel"),(2,24,"Love-Hotel"),(3,35,"Love-Hotel");
insert into RESERVATION(NUMERO_RES,DATE_RSA,NUMERO_CLI,NUMERO_CH) values (45876,"2011-5-18",1875,1),(98463,"2011-6-17",7845,2),(21547,"2011-8-19",1337,3);

/* Exemple de requete :                                                                                                 
SELECT * FROM HOTEL
Output : Love Hotel   1337 Ghetto du cybercrime, Neo-Tokyo
--> Affiche toute la table HOTEL.
SELECT * FROM CLIENT ORDER BY 1
Output : 
1337 	0x307845 	0xE
1875 	Makise 	        Kurise
7845 	Rentaro 	Okabe
---> Affiche toute la table CLIENT trié dans l'ordre croissant de l'attribut NUMERO_CLI.
SELECT NUMERO_RES, NUMERO_CH,DATE_RSA  FROM RESERVATION ORDER BY 1
Output :
21547 	3 	2011-8-19
45876 	1 	2011-5-18
98463 	2 	2011-6-17
---> Affiche les attributs NUMERO_RES, NUMERO_CH,DATE_RSA de la table RESERVATION trié par ordre croissant de l'attribut NUMERO_RES.
                                                                                                 
*/                                                                                               
/* Le 21/09/2020 à 9:55 par 0xE */

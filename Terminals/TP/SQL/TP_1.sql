/*


TP 1 : Base en SQL (28/09/20) par 0xE


mysql> show tables;
+--------------------+
| Tables_in_capteurs |
+--------------------+
| CLASSE             |
| MESURESG1          |
| MESURESG2          |
| MESURESG3          |
| MESURESG4          |
| MESURESG5          |
| MESURESG6          |
| MESURESG7          |
| SALLE              |
+--------------------+

--> Affiche les tables de la base de donnés capteur

mysql> describe MESURESG4;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | mediumint(9) | NO   | PRI | NULL    | auto_increment |
| temp       | varchar(5)   | YES  |     | NULL    |                |
| id_capteur | varchar(2)   | YES  |     | NULL    |                |
| id_carte   | varchar(10)  | YES  |     | NULL    |                |
| date       | varchar(10)  | YES  |     | NULL    |                |
| nom_classe | varchar(10)  | YES  |     | NULL    |                |
| nom_salle  | varchar(10)  | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+

--> Affiche les valeurs de la table MESURESG4

*/

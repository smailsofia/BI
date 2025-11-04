CREATE DataWHereCommande;
CREATE TABLE DClient
(id_seq_client VARCHAR(10) NOT NULL,id_client_prod INT NOT NULL,source_prod CHAR(20) ,company_name CHAR(20), city CHAR(20),country CHAR(20))
GO
CREATE TABLE DTemps
(id_temps DATETIME NOT NULL,annee DATETIME NOT NULL,mois_annee DATETIME)
GO
CREATE TABLE DEmployee
(id_seq_employee VARCHAR(10) NOT NULL,id_employee_prod INT NOT NULL,source_prod CHAR(20) ,nOM CHAR(20), prenom CHAR(20),territory CHAR(20),territoryDescri CHAR(20),region char(20))
GO
CREATE TABLE TFCommandes
(id_seq_fait VARCHAR(10) NOT NULL,id_seq_employee VARCHAR(10) NOT NULL,id_temps DATETIME NOT NULL ,id_seq_client VARCHAR(10) NOT NULL, nbr_commandes_livrees VARCHAR(10) ,nbr_commandes_non_livrees VARCHAR(10))
GO

ALTER TABLE DClient
ADD CONSTRAINT pk_DClient PRIMARY KEY (id_seq_client);
GO

ALTER TABLE DEmployee
ADD CONSTRAINT pk_DEmployee PRIMARY KEY (id_seq_employee);
GO

ALTER TABLE DTemps
ADD CONSTRAINT pk_DTemps PRIMARY KEY (id_temps);
GO

ALTER TABLE TFCommandes
ADD 
CONSTRAINT fk_TFCommandes_DClient FOREIGN KEY (id_seq_client) REFERENCES DClient(id_seq_client),
CONSTRAINT fk_TFCommandes_DEmployee FOREIGN KEY (id_seq_employee) REFERENCES DEmployee(id_seq_employee),
CONSTRAINT fk_TFCommandes_DTemps FOREIGN KEY (id_temps) REFERENCES DTemps(id_temps),
CONSTRAINT pk_TFCommandes PRIMARY KEY (id_seq_fait, id_seq_employee, id_temps, id_seq_client);
GO

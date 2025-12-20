
DROP DATABASE IF EXISTS DataWHereCommande;
GO

CREATE DATABASE DataWHereCommande;
GO

USE DataWHereCommande;
GO

CREATE TABLE DCustomer ( 
    IdSeqCustomer INT IDENTITY(1,1) NOT NULL,
    CustomerID VARCHAR(20),
    SourceProd VARCHAR(20),
    CompanyName VARCHAR(40),
    City VARCHAR(20),
    Country VARCHAR(20)
);
GO

CREATE TABLE DEmployee (
    IdSeqEmployee INT IDENTITY(1,1) NOT NULL,
    EmployeeID VARCHAR(20),
    SourceProd VARCHAR(20),
    LastName VARCHAR(20),
    FirstName VARCHAR(20),
    Territory VARCHAR(20),
    TerritoryDescr VARCHAR(20),
    Region VARCHAR(10)
);
GO

CREATE TABLE DTime (
    IdTime INT NOT NULL,
    YearD DATETIME,
    MonthYear DATETIME
);
GO

CREATE TABLE TFOrder (
    IdSeqOrder INT IDENTITY(1,1) NOT NULL,
    IdSeqCustomer INT NOT NULL,
    IdSeqEmployee INT NOT NULL,
    IdTime INT NOT NULL,
    NbShippedOrders VARCHAR(20),
    NbNonShippedOrders VARCHAR(20)
);
GO

ALTER TABLE DCustomer
ADD CONSTRAINT PK_Customer PRIMARY KEY(IdSeqCustomer);
GO

ALTER TABLE DEmployee
ADD CONSTRAINT PK_Employee PRIMARY KEY(IdSeqEmployee);
GO

ALTER TABLE DTime
ADD CONSTRAINT PK_Time PRIMARY KEY(IdTime);
GO

ALTER TABLE TFOrder
ADD 
    CONSTRAINT FK1_Order FOREIGN KEY(IdSeqCustomer) REFERENCES DCustomer(IdSeqCustomer),
    CONSTRAINT FK2_Order FOREIGN KEY(IdSeqEmployee) REFERENCES DEmployee(IdSeqEmployee),
    CONSTRAINT FK3_Order FOREIGN KEY(IdTime) REFERENCES DTime(IdTime),
    CONSTRAINT PK_Order  PRIMARY KEY(IdSeqOrder, IdSeqCustomer, IdSeqEmployee, IdTime);
GO
﻿

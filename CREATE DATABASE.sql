CREATE DATABASE DB2  
GO  
CREATE TABLE tblDemo  
(  
   Id int primary key,  
   Name char(20)  
)  
GO  


DROP DATABASE DB2

SELECT @@version

SELECT SERVERPROPERTY('productversion')
     , SERVERPROPERTY('productlevel')
     , SERVERPROPERTY('edition')
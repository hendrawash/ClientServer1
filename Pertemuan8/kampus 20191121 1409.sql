
USE kampus;

--
-- Drop table `mahasiswa`
--
DROP TABLE IF EXISTS mahasiswa;

--
-- Set default database
--
USE kampus;

--
-- Create table `mahasiswa`
--
CREATE TABLE mahasiswa (
  Id int(11) NOT NULL AUTO_INCREMENT,
  NIM varchar(5) NOT NULL,
  Nama varchar(255) DEFAULT NULL,
  Alamat text DEFAULT NULL,
  PRIMARY KEY (Id)
)
ENGINE = INNODB;

-- 
-- Dumping data for table mahasiswa
--
INSERT INTO mahasiswa VALUES
(1, '001', 'Hendrawan', 'Brebes');

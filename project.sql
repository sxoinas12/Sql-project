CREATE TABLE `ΕΝΟΙΚΙΑΖΕΙ` (
	`ΤΙΜΗ` FLOAT(4) ,
	`ΩΡΑ ΑΡΧΗΣ` VARCHAR(50) ,
	`ΩΡΑ ΛΗΞΗΣ` VARCHAR(50) ,
	`ΗΜΕΡΟΜΗΝΙΑ` VARCHAR(50) ,
	`ΚΩΔΙΚΟΣ` INT(10) REFERENCES `ΠΕΛΑΤΗΣ`(`ΚΩΔΙΚΟΣ`),
	`ID` INT(10)   REFERENCES `ΓΗΠΕΔΟ`(`ID`) ,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ`,`ID`) 

	
);

CREATE TABLE `ΓΗΠΕΔΟ` (
	`ΦΩΤΙΣΜΟΣ` VARCHAR(100) ,
	`ΚΛΙΜΑΤΙΣΜΟΣ` VARCHAR(50) ,
	`ID` INT(10) ,
	`ΜΠΑΛΕΣ` INT(5)  ,
	`ΡΟΥΧΑ` VARCHAR(255)  ,
	`ΠΑΠΟΥΤΣΙΑ` FLOAT ,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `ΠΕΛΑΤΗΣ` (
	`ΚΩΔΙΚΟΣ` INT(10) NOT NULL,
	`ΟΝΟΜΑ` VARCHAR(50)  ,
	`ΕΠΩΝΥΜΟ` VARCHAR(50)  ,
	`ΤΗΛΕΦΩΝΟ` VARCHAR(15)  ,
	PRIMARY KEY (`ΚΩΔΙΚΟΣ`)
);

CREATE TABLE `ΜΠΑΣΚΕΤ` (
	`ΔΑΠΕΔΟ` VARCHAR(50) ,
	`ID` INT(10)   REFERENCES `ΓΗΠΕΔΟ`(`ID`) ,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `ΠΟΔΟΣΦΑΙΡΟ` (
	`ΔΙΑΣΤΑΣΕΙΣ` VARCHAR(10) ,
	`ΕΙΔΟΣ ΤΑΠΗΤΑ` VARCHAR(25) ,
	`ID` INT(10)   REFERENCES `ΓΗΠΕΔΟ`(`ID`) ,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `ΒΟΛΕΥ` (
	`ID` INT(10)   REFERENCES `ΓΗΠΕΔΟ`(`ID`) ,
	PRIMARY KEY (`ID`)
);


LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\water_potability.csv"
IGNORE INTO TABLE sensores
FIELDS TERMINATED BY ';'
IGNORE 1 ROWS
(ph, dureza, solido, sulfato, condutividade , turbidez, potabilidade);

SELECT * FROM aps_qualidade_agua.sensores;
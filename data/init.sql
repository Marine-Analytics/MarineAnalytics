BEGIN TRANSACTION;
    CREATE TABLE IF NOT EXISTS vessels(id INT, name TEXT);
    CREATE TABLE IF NOT EXISTS sensors(vessel_id INT, id INT, name TEXT, normal_min INT, normal_max INT);
    CREATE TABLE IF NOT EXISTS sensors_history(vessel_id INT, sensor_id INT, value REAL, date DATETIME);
COMMIT;

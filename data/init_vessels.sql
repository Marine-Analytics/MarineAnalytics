-- Создать два судна --
BEGIN TRANSACTION;
    INSERT INTO vessels VALUES(1,'Тестовый стенд');
    INSERT INTO vessels VALUES(2,'Водник');
COMMIT;

-- Конфигурация тестового стенда
BEGIN TRANSACTION;
    INSERT INTO sensors VALUES(1,1,'Концентрация кислорода, %',10,30);
    INSERT INTO sensors VALUES(1,2,'Вибрация мотора, дБ',10,30);
    INSERT INTO sensors VALUES(1,3,'Температура, °C',10,50);
COMMIT;

-- Конфигурация водника
BEGIN TRANSACTION;
    INSERT INTO sensors VALUES(2,1,'Скорость судна, узлы',null,null);
    INSERT INTO sensors VALUES(2,2,'Скорость вращения вала',null,10000);
    INSERT INTO sensors VALUES(2,3,'Вибрация мотора',null,50);
    INSERT INTO sensors VALUES(2,4,'Объем топлива левого бака',null,null);
    INSERT INTO sensors VALUES(2,5,'Объем топлива правого бака',null,null);
COMMIT;

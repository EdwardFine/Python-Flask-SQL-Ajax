USE workbench_setup;
INSERT INTO names (name,created_at,updated_at) VALUES("Edward",NOW(),NOW());
INSERT INTO names (name,created_at,updated_at) 
VALUES("Donkey Kong",NOW(),NOW()),("Diddy Kong",NOW(),NOW()),("Tinky Kong",NOW(),NOW()),("Lanky Kong",NOW(),NOW()),("Chunky Kong",NOW(),NOW());
DELETE FROM names where id >1 and id<5 and name="Edward";
DELETE FROM names where id>9;
SELECT * FROM names;
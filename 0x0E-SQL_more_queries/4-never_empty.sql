-- A script that creates a table in the current database
CREATE TABLE IF NOT EXISTS id_not_null(
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256)
);

-- A script that creates a table in the current database
CREATE TABLE IF NOT EXISTS unique_id(
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256),
    UNIQUE(`id`)
);

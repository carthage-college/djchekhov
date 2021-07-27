SELECT
    id,
    firstname as first_name,
    lastname as last_name,
    username,
    TRIM(program) as program
FROM
    provisioning_vw
WHERE
    program LIKE "GRAD%"

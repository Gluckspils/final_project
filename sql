# Запрос №1
SELECT login,
       COUNT(*)
FROM "Couriers"
INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "inDelivery" = TRUE
GROUP BY "Couriers".login ;


# Запрос №2
SELECT track, 
       CASE
           WHEN finished = true THEN 2
           WHEN cancelled = true THEN -1
           WHEN "inDelivery" = true THEN 1
           ELSE 0
       END AS status
FROM "Orders" ;

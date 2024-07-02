SELECT D1.ID, COALESCE((
                        SELECT COUNT(*)
                        FROM ECOLI_DATA D2
                        WHERE D2.PARENT_ID = D1.ID
                        ), 0) AS CHILD_COUNT
FROM ECOLI_DATA D1
ORDER BY D1.ID;
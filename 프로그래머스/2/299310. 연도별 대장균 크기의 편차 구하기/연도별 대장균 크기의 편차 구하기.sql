SELECT YEAR(D1.DIFFERENTIATION_DATE) AS YEAR, (D2.MS - D1.SIZE_OF_COLONY) AS YEAR_DEV, D1.ID
FROM ECOLI_DATA D1
    JOIN (SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS MS
          FROM ECOLI_DATA
          GROUP BY YEAR(DIFFERENTIATION_DATE)) D2 ON YEAR(D1.DIFFERENTIATION_DATE) = D2.YEAR
ORDER BY YEAR, YEAR_DEV
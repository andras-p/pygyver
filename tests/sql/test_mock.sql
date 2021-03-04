`test.test_table` AS (
	SELECT CAST('TRUE' AS BOOLEAN) AS column_boolean, CAST('2021-01-01' AS DATE) AS column_date, CAST('2020-10-09T00:00:00' AS DATETIME) AS column_datetime, CAST('5.5' AS FLOAT64) AS column_float, CAST('1.0' AS FLOAT64) AS column_float64, CAST('55' AS INT64) AS column_int64, CAST('1' AS INT64) AS column_integer, CAST('5.5' AS NUMERIC) AS column_numeric, CAST('testing' AS STRING) AS column_string, CAST(NULL AS TIME) AS column_time, CAST('2019-09-27 15:59:46.052 UTC' AS TIMESTAMP) AS column_timestamp
	UNION ALL
	SELECT CAST('TRUE' AS BOOLEAN), CAST('2021-01-02' AS DATE), CAST('2020-10-09T00:00:01' AS DATETIME), CAST('1.0' AS FLOAT64), CAST(NULL AS FLOAT64), CAST('1' AS INT64), CAST(NULL AS INT64), CAST('1.5' AS NUMERIC), CAST('table' AS STRING), CAST(NULL AS TIME), CAST('2019-09-27 15:59:46.052 UTC' AS TIMESTAMP)
	UNION ALL
	SELECT CAST('FALSE' AS BOOLEAN), CAST(NULL AS DATE), CAST('2020-10-09T00:00:02' AS DATETIME), CAST(NULL AS FLOAT64), CAST('5.5' AS FLOAT64), CAST('10' AS INT64), CAST('55' AS INT64), CAST(NULL AS NUMERIC), CAST('1' AS STRING), CAST('23:59:59.99999' AS TIME), CAST('2019-09-27 15:59:46.052 UTC' AS TIMESTAMP)
)
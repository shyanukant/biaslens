# Now you can run queries using the client
QUERY = '''
SELECT
  DATE,
  SourceCommonName,
  DocumentIdentifier,
  V2Themes,
  V2Tone,
  Extras,
  V2Locations
FROM
  `gdelt-bq.gdeltv2.gkg`
WHERE
  LOWER(V2Themes) LIKE '%climate%'
  AND DATE >= CAST(FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY)) AS INT64)
LIMIT 100
'''
# Graylog Maintenance

## Delete by Query

```
curl -X POST "localhost:9200/myindex/_delete_by_query" -H 'Content-Type: application/json' -d'
{
  "query": { 
    "match": {
      "message": "some message"
    }
  }
}
'
```

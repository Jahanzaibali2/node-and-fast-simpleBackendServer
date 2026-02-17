# Balance Inquiry Server

Backend server on **port 8000** that accepts parameters and is reachable by agents.

## Run

```bash
npm start
```

Or: `node server.js`

## Endpoints

- **GET** `http://localhost:8000?param1=value1&param2=value2`  
  Query parameters are echoed in the JSON response.

- **POST** `http://localhost:8000`  
  Accepts parameters in the query string and/or JSON body.  
  Example body: `{"key": "value"}`

CORS is enabled so requests from other origins (e.g. browser or agent) are allowed.

## Example (agent or curl)

```bash
# GET with parameters
curl "http://localhost:8000?action=balance&id=123"

# POST with JSON body
curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d "{\"action\":\"inquiry\",\"account\":\"ACC001\"}"
```

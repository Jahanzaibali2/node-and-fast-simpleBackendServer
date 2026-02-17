const http = require("http");

const PORT = 8000;

const server = http.createServer((req, res) => {
  // CORS headers so agents/clients from other origins can reach it
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    res.end();
    return;
  }

  const url = new URL(req.url || "/", `http://localhost:${PORT}`);
  const params = Object.fromEntries(url.searchParams);

  if (req.method === "GET") {
    res.setHeader("Content-Type", "application/json");
    res.writeHead(200);
    res.end(
      JSON.stringify({
        ok: true,
        method: "GET",
        params,
        message: "Server received your parameters",
      })
    );
    return;
  }

  if (req.method === "POST") {
    let body = "";
    req.on("data", (chunk) => (body += chunk));
    req.on("end", () => {
      let payload = {};
      try {
        if (body) payload = JSON.parse(body);
      } catch (_) {
        payload = { raw: body };
      }
      res.setHeader("Content-Type", "application/json");
      res.writeHead(200);
      res.end(
        JSON.stringify({
          ok: true,
          method: "POST",
          queryParams: Object.fromEntries(url.searchParams),
          body: payload,
          message: "Server received your parameters",
        })
      );
    });
    return;
  }

  res.writeHead(405);
  res.end("Method Not Allowed");
});

server.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log("GET  - pass params in query: http://localhost:8000?key=value");
  console.log("POST - pass params in query or JSON body");
});

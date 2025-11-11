package main

import (
    "net/http"
    "log"
    "encoding/json"
    "github.com/go-redis/redis/v8"
    "context"
)

var rdb *redis.Client
var ctx = context.Background()

func main() {
    rdb = redis.NewClient(&redis.Options{Addr: "redis:6379"})
    http.HandleFunc("/ingest", ingestHandler)
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func ingestHandler(w http.ResponseWriter, r *http.Request) {
    var logEntry map[string]interface{}
    _ = json.NewDecoder(r.Body).Decode(&logEntry)
    entry, _ := json.Marshal(logEntry)
    rdb.LPush(ctx, "logs", entry)
    w.Write([]byte("ok"))
}

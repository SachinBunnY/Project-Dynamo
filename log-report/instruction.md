Analyze the Apache-style access log located at `/app/access.log`.
Generate a JSON report and save it as `/app/report.json`.

The report must have these fields:

- `total_requests`: the total number of log entries in the access log.
- `unique_ips`: the number of unique client IP addresses that made requests.
- `top_path`: the request path that appears most frequently in the log.

The output must be perfect and valid JSON.

import re

log_data = """2026-09-26 08:00:12 INFO  Connected to database at 10.0.0.5:5432
2026-09-26 08:01:33 WARN  Connection pool usage at 85 percent
2026-09-26 08:02:47 INFO  User 'admin' logged in from 192.168.1.10
2026-09-26 08:05:19 ERROR Failed to parse request body: invalid JSON
2026-09-26 08:05:20 INFO  Retrying request id=4423 in 500ms
2026-09-26 08:07:55 DEBUG Cache hit ratio: 0.92
2026-09-26 08:10:00 INFO  Scheduled job 'cleanup' started
2026-09-26 08:10:41 WARN  Disk usage on /var/log reached 90 percent
2026-09-26 08:12:03 ERROR Timeout while calling payment-service after 5000ms
2026-09-26 08:12:04 INFO  Fallback provider activated
2026-09-26 08:15:37 DEBUG GC pause: 42ms
2026-09-26 08:18:22 INFO  User 'maria' uploaded file report.pdf
2026-09-26 08:20:11 WARN  Deprecated API endpoint /v1/old called
2026-09-26 08:22:50 ERROR Unhandled exception in worker-3: NullPointerException
2026-09-26 08:22:51 INFO  Worker-3 restarted by supervisor
2026-09-26 08:25:14 DEBUG Heartbeat sent to cluster node 10.0.0.7
2026-09-26 08:30:00 INFO  Daily backup completed in 128 seconds
2026-09-26 08:31:45 ERROR Backup verification failed: checksum mismatch"""

pattern_warn_error = r'^\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+(ERROR|WARN(?:ING)?)\s+(.*)$'

print("1. Строки с уровнем ERROR или WARN")
for time, level, message in re.findall(pattern_warn_error, log_data, re.MULTILINE):
    print(f"{time} {level} {message}")

pattern_general = r'^\d{4}-\d{2}-\d{2}\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)$'
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

print("\n2. Строки, где упоминаются IP-адреса")
for time, level, message in re.findall(pattern_general, log_data, re.MULTILINE):
    if re.search(ip_pattern, message):
        print(f"{time} {level} {message}")
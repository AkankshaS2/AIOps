from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "server-metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="server-metrics-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for message in consumer:
    metrics = message.value

    # Example expected message:
    # {"server_id": "server02", "cpu_usage": 85, "memory_usage": 60}

    server_id = metrics.get("server_id", "unknown")
    cpu_usage = metrics.get("cpu_usage")

    if cpu_usage is not None and cpu_usage > 80:
        print(f'alert:High cpu usage detected on {server_id}: {cpu_usage}%')
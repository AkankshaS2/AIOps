pip install uv
uv venv
source .venv/bin/activate


`wget https://downloads.apache.org/kafka/4.1.0/kafka_2.13-4.1.0.tgz` 

`wget https://downloads.apache.org/kafka/4.1.0/kafka_2.13-4.1.0.tgz` 

`KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"`

`bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties`

`bin/kafka-server-start.sh config/server.properties`

`bin/kafka-topics.sh --create --topic server-metrics localhost:9092`

`bin/kafka-console-producer.sh --topic server-metrics --bootstrap:localhost:9092`

`bin/kafka-console-consumer.sh --topic server-metrics --bootstrap:localhost:9092 --from-beginning`
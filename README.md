# Tarea 3 - Procesamiento de Datos con Apache Spark

**Estudiante:** Isacc Fidel Mestra Ochoa
**Curso:** Big Data
**Universidad:** UNAD

## Descripción
Este repositorio contiene la solución al componente práctico de la Tarea 3. Se realizó un análisis de siniestralidad vial en Bogotá D.C. utilizando Apache Spark para el procesamiento en Batch, y Apache Kafka junto con Spark Streaming para el procesamiento en tiempo real.

## Requisitos
- Apache Spark 3.5.8
- Apache Kafka 3.9.2
- Python 3
- Librerías: `pyspark`, `kafka-python`

## Ejecución

### 1. Procesamiento Batch (Análisis de Siniestros)
Asegúrate de tener el archivo `siniestros.csv` en la misma carpeta del script y ejecuta:
```bash
spark-submit tarea3.py


### 2. Procesamiento en Tiempo Real (Kafka + Spark Streaming)
Terminal 1 (ZooKeeper):

bash
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties
Terminal 2 (Kafka):

bash
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties
Terminal 3 (Productor):

bash
python3 kafka_producer.py
Terminal 4 (Consumidor Spark):

bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8 spark_streaming_consumer.py

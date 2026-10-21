from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, hour, dayofweek

# 1. Iniciar la sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisBatchSiniestros") \
    .getOrCreate()

# Reducir los logs para que la consola no se llene
spark.sparkContext.setLogLevel("ERROR")

print("--- Cargando datos ---")
# 2. Cargar el CSV (separador ';' y header=True)
df = spark.read.csv("siniestros.csv", header=True, inferSchema=True, sep=";")

# Mostrar las columnas para confirmar la lectura
print("Columnas del dataset:")
df.printSchema()

# 3. Limpieza y Transformación
# Convertir FECHA a tipo Date y extraer Hora y Día de la semana
df_limpio = df.withColumn("Fecha_Date", to_date(col("FECHA"), "dd/MM/yyyy")) \
              .withColumn("Hora", hour(col("HORA"))) \
              .withColumn("Dia_Semana", dayofweek(col("Fecha_Date")))

# 4. Análisis Exploratorio (EDA) - Resultados en consola
print("--- Top 5 Horas con más siniestros ---")
df_limpio.groupBy("Hora").count().orderBy("count", ascending=False).show(5)

print("--- Siniestros por Día de la Semana (1=Domingo, 7=Sábado) ---")
df_limpio.groupBy("Dia_Semana").count().orderBy("Dia_Semana").show()

print("--- Top 5 Localidades con más siniestros ---")
df_limpio.groupBy("CODIGO_LOCALIDAD").count().orderBy("count", ascending=False).show(5)

# Detener Spark
spark.stop()

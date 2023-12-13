# DATA ENGINEERING INTERVIEW QUESTIONS

### 1. What is difference between dataframe,dataset and RDD

RDDs or Resilient Distributed Datasets is the fundamental data structure of the Spark. It is the collection of objects which is capable of storing the data partitioned across the multiple nodes of the cluster and also allows them to do processing in parallel.

It is fault-tolerant if you perform multiple transformations on the RDD and then due to any reason any node fails. The RDD, in that case, is capable of recovering automatically.

Dataframes can read and write the data into various formats like CSV, JSON, AVRO, HDFS, and HIVE tables. It is already optimized to process large datasets for most of the pre-processing tasks so that we do not need to write complex functions on our own.

Spark Datasets is an extension of Dataframes API with the benefits of both RDDs and the Datasets. It is fast as well as provides a type-safe interface. Type safety means that the compiler will validate the data types of all the columns in the dataset while compilation only and will throw an error if there is any mismatch in the data types.
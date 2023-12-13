# DATA ENGINEERING INTERVIEW QUESTIONS

### 1. What is difference between dataframe,dataset and RDD

RDDs or Resilient Distributed Datasets is the fundamental data structure of the Spark. It is the collection of objects which is capable of storing the data partitioned across the multiple nodes of the cluster and also allows them to do processing in parallel.

It is fault-tolerant if you perform multiple transformations on the RDD and then due to any reason any node fails. The RDD, in that case, is capable of recovering automatically.

Dataframes can read and write the data into various formats like CSV, JSON, AVRO, HDFS, and HIVE tables. It is already optimized to process large datasets for most of the pre-processing tasks so that we do not need to write complex functions on our own.

Spark Datasets is an extension of Dataframes API with the benefits of both RDDs and the Datasets. It is fast as well as provides a type-safe interface. Type safety means that the compiler will validate the data types of all the columns in the dataset while compilation only and will throw an error if there is any mismatch in the data types.

### 2. What is Cloud First, Cloud Journey and Migration ?

* Definition: "Cloud First" is a strategic principle or policy that organizations adopt to prioritize the use of cloud computing services over traditional on-premises solutions when considering new IT projects or technology investments.
* Objective: The goal is to leverage the benefits of cloud computing, such as scalability, flexibility, cost-efficiency, and rapid innovation. By adopting a "Cloud First" approach, organizations aim to take full advantage of the capabilities offered by cloud service providers.

* Definition: The "Cloud Journey" refers to the entire process of adopting and integrating cloud computing services into an organization's IT infrastructure and operations.
* Stages: The journey typically involves multiple stages, including assessment and planning, migration, integration, optimization, and ongoing management. Each stage addresses different aspects of the transition to ensure a smooth and effective move to the cloud.

* Definition: Cloud migration is the process of moving applications, data, and IT resources from on-premises environments or legacy systems to cloud-based infrastructure.
* Types of Migration:
    * Rehosting (Lift and Shift): Moving applications to the cloud with minimal changes.
    * Refactoring (Replatforming): Adapting or optimizing applications for better performance and scalability in the cloud.
    * Rearchitecting (Rebuilding): Redesigning applications to fully leverage cloud-native features.
    * Rebuilding (Full Rehost): Creating applications from scratch using cloud-native services.
* Challenges: Migration involves various challenges, such as data transfer, application compatibility, security, and training. Proper planning and execution are crucial for a successful migration.

### 3. What is Lift & Shift ?
"Lift and Shift" refers to a cloud migration strategy where existing applications or workloads are moved from their current on-premises or traditional hosting environment to the cloud without significant modifications. The goal is to quickly transition the application to the cloud infrastructure without redesigning or rearchitecting its components.

### 4.  What is three tier architecture ?
Three-tier architecture is a software design pattern that divides an application into three interconnected components or layers: the presentation layer (user interface), the application layer (business logic), and the data layer (database). This modular structure enhances scalability, maintainability, and flexibility in software development.
### 5. What is AMI ?
An Amazon Machine Image (AMI) is a pre-configured virtual machine image used to create instances (virtual servers) in Amazon Elastic Compute Cloud (EC2). It contains the necessary information to launch instances, including the operating system, application server, and any additional software.

### 6. What is SDN & CDN ?
**SDN(Software-Defined Networking)** is a network architecture approach that separates the control plane (decision-making) from the data plane (traffic handling) in networking devices. It enables centralized management and programmability, making networks more agile and adaptable to changing requirements.

**CDN(Content Delivery Network)** is a distributed network of servers strategically placed to deliver web content (such as images, videos, and web pages) to users based on their geographic location. This improves website performance, reduces latency, and enhances the user experience by optimizing content delivery.
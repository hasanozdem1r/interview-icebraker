# DevOps Interview Questions

### 1. What is DevOps
DevOps is a set of practices that aim to enhance collaboration and communication between development and operations teams to improve the speed and quality of software delivery. 

It emphasizes automation, continuous integration, continuous delivery/deployment (CI/CD), and infrastructure as code (IaC) to ensure software is delivered rapidly and reliably. DevOps also involves monitoring and measuring software performance to detect and resolve issues quickly.

### 2. How is DevOps different from agile methodology?

Agile methodology is a project management approach that emphasizes flexibility and collaboration among cross-functional teams to deliver software in small increments. 

DevOps is a cultural shift that emphasizes collaboration between development and operations teams to automate and streamline software delivery, with a focus on continuous integration, testing, delivery, and deployment.

### 3. Which are some of the most popular DevOps tools?
There are many tools available for implementing DevOps practices, and the choice of tooling will depend on the specific needs and preferences of the organization. Here are some of the most popular DevOps tools:

* Git - A distributed version control system that enables developers to collaborate on code changes and track changes over time.
* Jenkins - An open-source automation server that supports continuous integration and continuous delivery.
* Docker - A containerization platform that enables developers to package applications and dependencies into portable containers that can be deployed anywhere.
* Kubernetes - An open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.
* Ansible - An open-source automation tool that allows system administrators to automate the deployment and configuration of software applications.
* Terraform - An open-source infrastructure as code tool that allows developers to provision and manage infrastructure resources on cloud platforms.
* Prometheus - An open-source monitoring system that collects metrics from applications and infrastructure and provides insights into system performance.
* ELK Stack - A set of open-source tools that includes Elasticsearch, Logstash, and Kibana, used for log management and analysis.
* Nagios - An open-source monitoring tool that helps to detect and resolve issues with infrastructure and applications.

These are just a few examples of the many tools available in the DevOps ecosystem, and there are many more depending on specific needs and use cases.

### 4. What are the different phases in DevOps?

DevOps involves the integration of development and operations processes across the software development lifecycle. Here are the different phases in DevOps:

* Plan: This phase involves the planning and coordination of activities across teams, defining goals, and prioritizing tasks.
* Develop: In this phase, the development team writes, tests, and reviews code changes using tools like version control, continuous integration, and automated testing.
* Build: This phase involves packaging and building the application code into a deployable artifact, such as a Docker image or an executable file.
* Test: In this phase, automated tests are run to ensure the code changes meet quality standards, and manual testing is done to validate the software's functionality.
* Deploy: In this phase, the application code is deployed to the production environment, either manually or using automated deployment tools.
* Operate: In this phase, the operations team monitors the application's performance and availability, troubleshoots issues, and maintains the infrastructure.
* Monitor: In this phase, the performance of the application and infrastructure is continuously monitored to detect and resolve issues quickly and to provide insights into system performance.

These phases are not necessarily sequential, and many of them may occur simultaneously or iteratively depending on the organization's needs and practices. DevOps practices aim to automate and streamline each phase of the software development lifecycle to achieve faster and more reliable software delivery.

### 5. What is the difference between continuous delivery and continuous deployment?

|                                    Continuous Delivery                                    |                                     Continuous Deployment                                     |
|:-----------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------:|
|                    Ensures code can be safely deployed on to production                   |      Every change that passes the automated tests is deployed to production automatically     |
|              Ensures business applications and services function as expected              |           Makes software development and the release process faster and more robust           |
| Delivers every change to a production-like environment through rigorous automated testing | There is no explicit approval from a developer and requires a developed culture of monitoring |

### 6. What is the use of SSH ?
SSH (Secure Shell) is a cryptographic network protocol that provides a secure and encrypted way to access and manage remote machines over an insecure network.

The main use of SSH is to establish a secure connection between two networked devices, such as a client and a server, and to provide secure access to the shell of the remote machine. This allows system administrators to remotely manage servers and other networked devices, such as routers and switches, securely.

In addition to providing secure shell access, SSH can also be used for secure file transfer (SFTP) and remote command execution. SSH can also be used for tunneling other network protocols, such as HTTP, FTP, and SMTP, over an encrypted connection.

### 7. What is configuration management ?

Configuration management (CM) is a crucial practice in software development and IT operations, which involves the systematic handling of changes to maintain the integrity of systems over time. CM encompasses a range of policies, techniques, procedures, and tools that are used to evaluate change proposals, manage changes, and track their progress while maintaining proper documentation.

By implementing CM, organizations can ensure that changes are made in a controlled and standardized manner, reducing the risk of errors and system failures. It also facilitates collaboration between team members and enables faster, more efficient delivery of software and services.

CM practices include version control, testing, deployment automation, monitoring, and documentation. These practices help organizations maintain a comprehensive view of their IT infrastructure and make informed decisions about changes that will impact the system.

### 8. How many locations does Git have ?

```markdown
+-----------------------+       +------------------+
|    Remote Repository  |       |    Local Repository  |
| (e.g., GitHub, GitLab)|       |------------------|
+-----------------------+       | .git directory   | 
               |                 +------------------+
               |<-------------->  |  Objects (commits, blobs, etc.) |
               |                 |  Refs (branches, tags)        |     
               V                 +------------------+
+-----------------------+           
|     Working Directory |           
|  (Your project files) |           
+-----------------------+           
            ^            
            |            
          stage/changes 
            |            
+-----------------------+          
|      Staging Area     |          
|    (Index)            |          
+-----------------------+          
```
**Remote Repository**: A central repository, often hosted on platforms like GitHub, GitLab, or Bitbucket.
Stores the history of your project and acts as a shared point of collaboration.

**Local Repository**: A copy of the entire repository stored on your computer within a hidden .git directory.
Contains all the commits, branches, tags, and configuration information.

**Working Directory**: The directory where your actual project files reside.
You modify files, create new files, and delete files within this directory.

**Staging Area (Index)**: An intermediate area where you prepare a snapshot of changes before committing them to your local repository.
Lets you selectively add and organize the changes you want to include in your next commit.

### 9. What is difference between git merge vs git rebase ?
When we merge changes from one Git branch to another, we can use ‘git merge’ or ‘git rebase’.

* Merge preserves history, whereas rebase rewrites it.Git merge is non-destructive. Neither the main nor the feature branch is changed.
* Git rebase moves the feature branch histories to the head of the main branch. Rebasing is useful for streamlining a complex history. The benefit of rebase is that it has a linear commit history.
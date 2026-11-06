
# Intelligent Cloud Monitoring Dashboard (ICMD)

### AWS-Based Infrastructure Monitoring and Alerting System

ICMD is a cloud monitoring application built using Python, Django and AWS services to monitor EC2 infrastructure, collect system metrics, visualize resource utilization and generate automated alerts when predefined thresholds are exceeded.

The project uses an event-driven, serverless architecture to automate metric collection and monitoring without requiring a continuously running monitoring process.

---

## Project Overview

Managing cloud infrastructure requires continuous visibility into resource utilization and system health.

ICMD addresses this by integrating AWS monitoring services with a Django-based dashboard. It periodically collects EC2 monitoring metrics, stores historical data and provides a centralized interface for monitoring infrastructure performance.

### Key Features

- **EC2 Monitoring:** Monitor cloud infrastructure metrics using Amazon CloudWatch.
- **Automated Metric Collection:** Collect monitoring data through AWS Lambda.
- **Scheduled Execution:** Use Amazon EventBridge to trigger monitoring workflows.
- **Data Storage:** Store collected monitoring metrics in Amazon DynamoDB.
- **Threshold-Based Alerts:** Identify resource utilization exceeding configured thresholds.
- **Email Notifications:** Send infrastructure alerts through Amazon SNS.
- **Monitoring Dashboard:** Visualize infrastructure metrics through a Django web application.
- **AWS Integration:** Connect Python applications with AWS services using Boto3.

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Backend | Django |
| Cloud Platform | AWS |
| Infrastructure | Amazon EC2 |
| Monitoring | Amazon CloudWatch |
| Serverless Computing | AWS Lambda |
| Scheduling | Amazon EventBridge |
| Database | Amazon DynamoDB |
| Notifications | Amazon SNS |
| AWS SDK | Boto3 |
| Local Database | SQLite |
| Frontend | HTML, CSS, JavaScript |

---

## System Architecture

The application follows an event-driven monitoring architecture.

```text
       Amazon EventBridge
               |
               | Scheduled Trigger
               v
          AWS Lambda
               |
               | Retrieve EC2 Metrics
               v
       Amazon CloudWatch
               |
               | Metric Data
               v
          AWS Lambda
               |
        +------+------+
        |             |
        v             v
    DynamoDB      Threshold
    Storage       Evaluation
                      |
                      | Threshold Exceeded
                      v
                  Amazon SNS
                      |
                      v
                Email Alert


       Django Monitoring Dashboard
                      |
                      v
                  DynamoDB
                      |
                      v
             Metric Visualization
```

---

## Monitoring Workflow

The monitoring process follows these steps:

1. **Scheduled Trigger:** Amazon EventBridge triggers the monitoring workflow at the configured interval.

2. **Metric Collection:** AWS Lambda executes Python logic to retrieve EC2 infrastructure metrics from Amazon CloudWatch.

3. **Data Processing:** The collected metrics are processed and evaluated against predefined monitoring thresholds.

4. **Data Storage:** Monitoring records are stored in Amazon DynamoDB for subsequent retrieval.

5. **Alert Generation:** When a monitored metric exceeds its configured threshold, the application triggers an alert through Amazon SNS.

6. **Dashboard Visualization:** The Django dashboard retrieves stored monitoring data and displays infrastructure metrics for monitoring and analysis.

---

## AWS Services Used

### 1. Amazon EC2
Provides the cloud computing infrastructure being monitored.

### 2. Amazon CloudWatch
Collects and provides infrastructure monitoring metrics such as CPU utilization.

### 3. AWS Lambda
Executes serverless Python functions for automated metric collection and processing.

### 4. Amazon EventBridge
Schedules monitoring executions at configured intervals without maintaining a continuously running process.

### 5. Amazon DynamoDB
Stores collected monitoring data for dashboard retrieval and analysis.

### 6. Amazon SNS
Delivers email notifications when configured monitoring thresholds are exceeded.

### 7. AWS IAM
Manages permissions and secure access between AWS services.

---

## Project Structure

```text
ICMD-PROJECT/
│
├── dashboard/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── icmd_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── templates/
│   └── dashboard/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## Installation and Setup

### Prerequisites

- Python 3.10+
- pip
- AWS account
- AWS CLI (for AWS configuration)

### 1. Clone the Repository

```bash
git clone https://github.com/Saimohith4/ICMD-PROJECT-.git

cd ICMD-PROJECT-
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure AWS Credentials

Configure your AWS credentials using:

```bash
aws configure
```

Provide the appropriate AWS access key, secret key and region.

Ensure the IAM role or user has only the permissions required for the monitoring workflow, including access to the relevant CloudWatch metrics, DynamoDB table and SNS topic.

### 5. Configure Environment Variables

Configure the AWS resource identifiers and application settings required by your deployment.

Do not commit AWS credentials, secret keys or sensitive configuration values to GitHub.

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Django Development Server

```bash
python manage.py runserver
```

Open the application:

```text
http://127.0.0.1:8000/
```

---

## Engineering Highlights

- Designed an event-driven monitoring workflow using AWS managed services.
- Automated infrastructure metric collection using serverless computing.
- Integrated Python applications with AWS services using Boto3.
- Implemented scheduled monitoring using EventBridge and Lambda.
- Connected metric storage, threshold evaluation and notification workflows.
- Developed a centralized Django dashboard for infrastructure monitoring.

---

## Cost Optimization

The architecture uses scheduled serverless execution rather than maintaining an always-running monitoring process.

This approach helps reduce unnecessary compute consumption.

EC2 resources and scheduled monitoring triggers can be stopped or disabled when monitoring is not required, helping avoid unnecessary AWS charges.

Actual costs depend on resource usage, AWS region and service pricing.

---

## Learning Outcomes

Through this project, I gained practical experience in:

- AWS cloud infrastructure and service integration.
- Serverless application development.
- Event-driven architecture.
- Infrastructure monitoring and alerting.
- Python automation using Boto3.
- Django application development.
- Cloud resource management and cost optimization.

---

## Author

**Sai Mohith Sriramoju**

- GitHub: https://github.com/Saimohith4
- LinkedIn: https://linkedin.com/in/sriramojohith-72577a248

---

## License

This project is intended for educational and demonstration purposes.

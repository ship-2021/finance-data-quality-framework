 Finance Data Quality & Reconciliation Testing Framework
Overview

# Finance Data Quality & Reconciliation Testing Framework

## Overview

A Python-based automated testing framework designed to validate financial data quality, source-to-target reconciliation, business rules, and data integrity across financial data pipelines.

This project demonstrates how Software Engineers in Test can use Python, PyTest, SQL, Snowflake, and CI/CD practices to automate data validation and identify data-processing defects.

### Key Focus Areas

- Data quality and integrity validation
- Source-to-target reconciliation
- Financial business rule testing
- API and event-driven data validation
- ETL audit and batch monitoring
- Automated test execution and reporting
- Snowflake data warehouse integration

## Business Problem

Financial data pipelines must maintain accuracy, completeness, and consistency across source systems, transformation layers, and reporting tables.

Data-processing defects can result in missing records, duplicate trades, incorrect financial totals, and unreliable reports.

This framework demonstrates automated validation techniques that help identify such defects early and improve confidence in financial data processing.

## Features

### 1. Data Quality Testing

- Mandatory-field and NULL validation
- Duplicate-record detection
- Data type and value validation
- Positive quantity and price checks
- Supported currency validation

### 2. Source-to-Target Reconciliation

- Source and target record-count comparison
- Financial total and trade-value validation
- Missing-record identification
- Record-level comparison using business keys
- Investigation of data mismatches

### 3. Financial Business Rule Testing

- Trade field validation
- Quantity and price constraints
- Currency validation
- Invalid and boundary-value test cases

### 4. API Testing

- HTTP status-code validation
- Response structure and mandatory-field checks
- Invalid trade payload testing
- API error-response testing
- Automated API tests using Python and PyTest

### 5. Event-Driven Data Validation

- Required event-field validation
- Duplicate event detection
- Idempotency test scenarios
- Event-to-curated-record reconciliation

### 6. ETL Audit and Batch Validation

- Batch-level processing checks
- Expected versus actual record counts
- Failure investigation and reconciliation
- Validation of audit information

### 7. Test Automation and Reporting

- Modular PyTest test suites
- Automated test execution
- HTML test reports using `pytest-html`
- GitHub Actions workflow support for CI/CD

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Test Automation | PyTest, pytest-html |
| Data Validation | SQL, Pandas |
| Data Warehouse | Snowflake |
| API Testing | Requests, Responses |
| Data Engineering Concepts | ETL, reconciliation, data quality, batch auditing |
| CI/CD | GitHub Actions |

## Project Structure

```text
finance-data-quality-framework/
├── .github/
│   └── workflows/
├── dashboards/
├── data/
├── reports/
├── sql/
├── tests/
├── validation/
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or a compatible version
- Git
- A configured Snowflake account for Snowflake integration tests
- Dependencies listed in `requirements.txt`

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Test Suite

```bash
pytest
```

### Generate an HTML Test Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the test execution results.

## Snowflake Integration

The framework can connect to Snowflake using the Snowflake Python Connector to execute SQL queries and validate financial data stored in warehouse tables.

### Example Database Structure

| Schema | Purpose |
|---|---|
| `RAW` | Raw or ingested financial data |
| `CURATED` | Cleaned and transformed data |
| `AUDIT` | ETL batch and processing audit information |

Example tables used in the project:

- `FINANCE_QA.RAW.RAW_TRADES`
- `FINANCE_QA.CURATED.CURATED_TRADES`
- `FINANCE_QA.AUDIT.ETL_BATCH_AUDIT`

### Configure the Connection

Install the required packages if they are not already included in `requirements.txt`:

```bash
pip install snowflake-connector-python python-dotenv
```

Configure your connection settings in a local `.env` file:

```dotenv
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=your_warehouse
SNOWFLAKE_DATABASE=FINANCE_QA
SNOWFLAKE_SCHEMA=RAW
SNOWFLAKE_ROLE=your_role
```

Replace these placeholders with your own Snowflake configuration.

### Example Python Connection

```python
import os

import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

conn = snowflake.connector.connect(
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    user=os.environ["SNOWFLAKE_USER"],
    password=os.environ["SNOWFLAKE_PASSWORD"],
    warehouse=os.environ["SNOWFLAKE_WAREHOUSE"],
    database=os.environ["SNOWFLAKE_DATABASE"],
    schema=os.environ["SNOWFLAKE_SCHEMA"],
    role=os.getenv("SNOWFLAKE_ROLE"),
)

try:
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()"
        )
        print(cursor.fetchone())
finally:
    conn.close()
```

### Snowflake Validation Scenarios

The framework can validate:

- Source-to-target record counts
- NULL values in mandatory fields
- Duplicate trade identifiers
- Financial totals and trade-value reconciliation
- Batch-level audit information
- Data consistency across pipeline layers

**Security:** Never commit `.env` files, passwords, or other secrets to GitHub. Add `.env` to `.gitignore`. For CI/CD, use GitHub Actions Secrets or an approved secrets manager.

## Example Data Quality Checks

### Detect Duplicate Trade IDs

```sql
SELECT TRADE_ID, COUNT(*) AS duplicate_count
FROM FINANCE_QA.CURATED.CURATED_TRADES
GROUP BY TRADE_ID
HAVING COUNT(*) > 1;
```

This query identifies trade IDs appearing more than once. The uniqueness rule must match the business requirements; some systems may require a composite key, such as trade ID and batch ID.

### Compare Source and Target Counts

```sql
SELECT
    (SELECT COUNT(*)
     FROM FINANCE_QA.RAW.RAW_TRADES) AS source_count,
    (SELECT COUNT(*)
     FROM FINANCE_QA.CURATED.CURATED_TRADES) AS target_count;
```

A count mismatch requires investigation. Matching counts alone do not guarantee that the underlying records or financial values are correct.

### Validate Mandatory Fields

```sql
SELECT COUNT(*) AS invalid_records
FROM FINANCE_QA.CURATED.CURATED_TRADES
WHERE TRADE_ID IS NULL;
```

The test should fail when mandatory-field violations are found, according to the defined data-quality rules.

## Test Execution Results

The framework uses PyTest to execute automated validation tests.

### Console Results

The console output provides a summary of the test execution, including passed, failed, or skipped tests.
The console output provides a quick summary of the executed test suite, including passed and failed tests.
<img width="2686" height="1120" alt="image" src="https://github.com/user-attachments/assets/81ba498c-e4f2-46ab-a62d-bc6b48319bec" />

### HTML Test Report

The HTML report provides a more detailed view of test execution results.

An HTML report is generated for a more detailed view of test execution results.
<img width="2850" height="1452" alt="image" src="https://github.com/user-attachments/assets/716a9bb6-74e0-4c3e-9496-be820ed3e4a1" />

Generate the report with:

```bash
pytest --html=reports/report.html --self-contained-html
```

The generated report is available at `reports/report.html`.

Add screenshots of your latest actual test execution to the repository, for example:

```text
reports/
└── screenshots/
    ├── console-results.png
    └── html-report.png
```

Once these images are committed, display them here:

```markdown
### Console Test Results

![PyTest Console Results](reports/screenshots/console-results.png)

### HTML Test Report

![PyTest HTML Report](reports/screenshots/html-report.png)
```

Ensure screenshots show the actual latest results and contain no credentials or sensitive information.

## CI/CD Integration

The project includes GitHub Actions workflow support for automated test execution on configured repository events, such as pushes or pull requests.

Automated execution helps identify regressions early and provides repeatable test results.

If Snowflake integration tests are executed through GitHub Actions, configure the required connection credentials securely using repository or environment secrets.

## Testing Approach

The framework follows a risk-based data testing approach:

1. Validate source data and required fields.
2. Verify transformations and business rules.
3. Reconcile source and target record counts.
4. Compare financial totals and individual records.
5. Validate API responses and event-processing behavior.
6. Review test results and investigate failures.
7. Re-run relevant tests after fixes.

## Expected Outcome

The framework demonstrates practical testing techniques for financial data platforms, with an emphasis on data accuracy, reconciliation, automated validation, and repeatable quality checks.

## Future Enhancements

- Expand integration tests against live data pipelines.
- Add schema-drift detection.
- Improve batch-level audit and recovery testing.
- Extend event-processing tests for retries and duplicate delivery.
- Add richer CI test reporting and coverage tracking.
- Expand performance testing for larger datasets.







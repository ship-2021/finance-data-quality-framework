 Finance Data Quality & Reconciliation Testing Framework
Overview




# Finance Data Quality & Reconciliation Testing Framework

## Overview

A Python-based automated testing framework designed to validate financial data quality, source-to-target reconciliation, business rules, and data integrity across financial data pipelines.

The project demonstrates how Software Engineers in Test can automate data validation using Python, PyTest, SQL, and CI/CD practices.

**Key focus areas:**
- Data quality and integrity validation
- Source-to-target reconciliation
- Financial business rule testing
- API and event validation
- ETL audit and batch monitoring
- Automated test execution and reporting

## Business Problem

Financial data pipelines must maintain accuracy, completeness, and consistency across source systems, transformation layers, and reporting tables.

Data processing defects can result in missing records, duplicate trades, incorrect financial totals, and unreliable reports.

This framework demonstrates automated checks that help identify such defects early and improve confidence in financial data processing.

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
- Idempotency testing scenarios
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
- GitHub Actions CI/CD workflow support

## Technology Stack

- **Language:** Python
- **Testing:** PyTest, pytest-html
- **Data Validation:** SQL, Pandas
- **Data Warehouse:** Snowflake
- **Data Engineering Concepts:** ETL, reconciliation, data quality, batch auditing
- **API Testing:** Requests, Responses
- **CI/CD:** GitHub Actions

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

- Python 3.11 or a compatible supported Python version
- Git
- Required dependencies listed in `requirements.txt`

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

Open `reports/report.html` in a browser to review the test results.

## Example Data Quality Checks

### Detect Duplicate Trade IDs

```sql
SELECT TRADE_ID, COUNT(*) AS duplicate_count
FROM CURATED_TRADES
GROUP BY TRADE_ID
HAVING COUNT(*) > 1;
```

The uniqueness rule should match the actual business key. Some systems may require a composite key, such as trade ID and batch ID.

### Compare Source and Target Counts

```sql
SELECT
    (SELECT COUNT(*) FROM SOURCE_TRADES) AS source_count,
    (SELECT COUNT(*) FROM TARGET_TRADES) AS target_count;
```

A count mismatch triggers further investigation. Matching counts alone do not guarantee that the underlying records are correct.

### Validate Mandatory Fields

```sql
SELECT COUNT(*) AS invalid_records
FROM CURATED_TRADES
WHERE TRADE_ID IS NULL;
```

The test should fail when mandatory-field violations are found, according to the defined data-quality rules.

## CI/CD Integration

The project includes GitHub Actions workflow support for automated test execution on configured repository events, such as pushes or pull requests.

Automated execution helps identify regressions early and provides repeatable test results.

## Testing Approach

The framework follows a risk-based data testing approach:

1. Validate source data and required fields.
2. Verify transformation and business rules.
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

**Test Execution Results

The framework uses PyTest to execute automated data-quality, reconciliation, business-rule, API, and event-validation tests.

Console Results

The console output provides a quick summary of the executed test suite, including passed and failed tests.
<img width="2686" height="1120" alt="image" src="https://github.com/user-attachments/assets/81ba498c-e4f2-46ab-a62d-bc6b48319bec" />


HTML Test Report

An HTML report is generated for a more detailed view of test execution results.
<img width="2850" height="1452" alt="image" src="https://github.com/user-attachments/assets/716a9bb6-74e0-4c3e-9496-be820ed3e4a1" />


Generate the report:

pytest --html=reports/report.html --self-contained-html

Report location: reports/report.html

Test counts and screenshots should reflect the latest actual test execution.

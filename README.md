# Healthcare Data Governance and Cleaning

## Project Overview

This project demonstrates basic healthcare data governance and data quality management practices using a de-identified synthetic patient dataset. The objective was to classify data fields, validate data quality, apply reproducible cleaning rules, and document the results while maintaining patient privacy.

## Objectives

- Create a privacy-aware data dictionary.
- Verify that the dataset is de-identified.
- Validate data types, ranges, missing values, and duplicate patient identifiers.
- Apply data cleaning rules without modifying or inventing clinical information.
- Document findings in a transparent and reproducible manner.

## Dataset

**File:** `healthcare_patients_sample.csv`

The dataset contains synthetic patient records used for educational and training purposes. No direct patient identifiers are included.

## Why the Dataset is De-identified

The dataset is considered de-identified because it does not contain:

- Patient names
- Addresses
- Phone numbers
- Email addresses
- Dates of birth
- Government-issued identification numbers

Instead, each record uses a synthetic patient identifier (`PatientID`) that cannot be linked to a real individual.

## Data Dictionary

The data dictionary is provided in:

`Data_Dictionary.xlsx`

Fields included:

- PatientID
- Age
- Gender
- Diagnosis
- PrimaryMedication
- DosageMg
- TreatmentDurationDays
- Readmitted
- BloodPressure
- CholesterolLevel

## Validation Checks Performed

The following data quality checks were conducted:

### 1. Data Type Validation
Verified that each column contains the expected data type.

### 2. Missing Value Detection
Checked all fields for null or blank values.

### 3. Duplicate Record Detection
Verified that all PatientID values are unique.

### 4. Range Validation
Validated acceptable ranges for:
- Age
- DosageMg
- TreatmentDurationDays
- CholesterolLevel

### 5. Format Validation
Checked blood pressure values for the expected format:

`Systolic/Diastolic`

## Cleaning Rules Applied

The following cleaning rules were defined:

1. Preserve original records.
2. Remove exact duplicate records if detected.
3. Standardize categorical fields where necessary.
4. Flag missing or invalid values.
5. Do not estimate, modify, or invent clinical values.

## Quality Exception Log

Quality issues identified during validation are documented in:

`Quality_Exception_Log.xlsx`

If no issues are found, the log records that no corrective actions were required.

## Deliverables

- healthcare_patients_sample.csv
- Data_Dictionary.xlsx
- Validation_Report.docx
- Quality_Exception_Log.xlsx
- Cleaning_Summary.docx
- README.md

## Conclusion

The dataset successfully demonstrates healthcare data governance and data quality assessment practices. Validation checks were performed using reproducible rules, privacy considerations were documented, and data integrity was maintained throughout the cleaning process.
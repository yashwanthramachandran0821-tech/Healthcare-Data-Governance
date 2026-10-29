import pandas as pd
import re

# Load dataset
df = pd.read_csv("healthcare_patients_sample.csv")

print("=" * 50)
print("HEALTHCARE DATA VALIDATION REPORT")
print("=" * 50)

# ---------------------------
# Missing Values Check
# ---------------------------
print("\n1. Missing Values Check")
missing = df.isnull().sum()

if missing.sum() == 0:
    print("PASS: No missing values found.")
else:
    print("FAIL: Missing values detected.")
    print(missing[missing > 0])

# ---------------------------
# Duplicate PatientID Check
# ---------------------------
print("\n2. Duplicate PatientID Check")

duplicates = df[df.duplicated(subset=["PatientID"])]

if duplicates.empty:
    print("PASS: No duplicate Patient IDs found.")
else:
    print("FAIL: Duplicate Patient IDs detected.")
    print(duplicates[["PatientID"]])

# ---------------------------
# Age Validation
# ---------------------------
print("\n3. Age Range Validation (0-120)")

invalid_age = df[(df["Age"] < 0) | (df["Age"] > 120)]

if invalid_age.empty:
    print("PASS: All ages are within valid range.")
else:
    print("FAIL: Invalid ages detected.")
    print(invalid_age[["PatientID", "Age"]])

# ---------------------------
# Dosage Validation
# ---------------------------
print("\n4. Dosage Validation (>0 mg)")

invalid_dosage = df[df["DosageMg"] <= 0]

if invalid_dosage.empty:
    print("PASS: All dosage values are valid.")
else:
    print("FAIL: Invalid dosage values detected.")
    print(invalid_dosage[["PatientID", "DosageMg"]])

# ---------------------------
# Treatment Duration Validation
# ---------------------------
print("\n5. Treatment Duration Validation (>0 days)")

invalid_duration = df[df["TreatmentDurationDays"] <= 0]

if invalid_duration.empty:
    print("PASS: All treatment durations are valid.")
else:
    print("FAIL: Invalid treatment durations detected.")
    print(invalid_duration[["PatientID", "TreatmentDurationDays"]])

# ---------------------------
# Cholesterol Validation
# ---------------------------
print("\n6. Cholesterol Validation (>0)")

invalid_cholesterol = df[df["CholesterolLevel"] <= 0]

if invalid_cholesterol.empty:
    print("PASS: All cholesterol values are valid.")
else:
    print("FAIL: Invalid cholesterol values detected.")
    print(invalid_cholesterol[["PatientID", "CholesterolLevel"]])

# ---------------------------
# Blood Pressure Format Validation
# ---------------------------
print("\n7. Blood Pressure Format Validation")

bp_pattern = r"^\d{2,3}/\d{2,3}$"

invalid_bp = df[
    ~df["BloodPressure"].astype(str).str.match(bp_pattern, na=False)
]

if invalid_bp.empty:
    print("PASS: Blood pressure format is valid.")
else:
    print("FAIL: Invalid blood pressure format detected.")
    print(invalid_bp[["PatientID", "BloodPressure"]])

# ---------------------------
# Data Types Check
# ---------------------------
print("\n8. Data Type Summary")
print(df.dtypes)

print("\n" + "=" * 50)
print("VALIDATION COMPLETED")
print("=" * 50)
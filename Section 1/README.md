# Section 1: Data Pipelines

## Instructions to use
1. Env set up using requirements.txt
2. Add 2 datasets in csv format into inputs folder
3. Run main.py

## Assumptions
- Inputs are csv files
- Data is pulled from these files instead of pushed from upstream
- For a vague date like 05/08/2006, we assume dayfirst format (i.e. 05 is the day and 08 is the month)
- Process input files in batches at hourly interval. Each batch is 1 csv file
- Output are csv files in a file folder named outputs

## Validation Checks (in order, only on those still valid)
- Mobile Number == 8 digits
- Email with 3 parts: [alphanumerical]@[emailprovider].[com/net]
- Name is required
- Age > 18 y/o as of 1 Jan 2022

## Data Format
- Name split into first_name and last_name
  - Trim leading and trailing whitespaces
  - Check for salutations
  - Remove if missing name
- Birthday into YYYYMMDD format
- Create bool field above_18 based on Birthday (also required for validation)
- Membership IDs with user last name + SHA256 hash of birthday

## Output
- Save processed output files (both successful & unsucessful) in output folder at hourly intervals
import pandas as pd
import re
import numpy as np
import hashlib

'''
input: name of dataset (assumed to be in inputs folder and in csv format)
output: successful and unsuccessful applicants (in respective output folders)
'''
def main(dataset):
  # read dataset
  ori_df = pd.read_csv(f'inputs/{dataset}')
  df = ori_df.copy()

  print(df.shape)

  # format mobile_no: check for only digits, length == 8
  df['mobile_no'] = df['mobile_no'].apply(lambda x: ''.join(re.findall(r'\d+', x)))
  df['still_successful'] = df['mobile_no'].apply(lambda x: True if len(x) == 8 else False)

  # keep unsuccessful into a list of indexes
  unsuccessful_idx = df[~df['still_successful']].index

  # df retains still successful apps
  df = df[df['still_successful']].drop(columns='still_successful')

  # format email: check for [alphanumerical]@[emailprovider].[com/net]
  df[['first_email_part', 'second_email_part']] = df['email'].str.split('@', expand = True)
  df[['emailprovider', 'com/net']] = df['second_email_part'].str.split('.', expand = True)
  df['still_successful'] = df['com/net'].isin(['com', 'net'])

  working_cols = ['first_email_part', 'second_email_part', 'emailprovider', 'com/net', 'still_successful']

  # keep unsuccessful into a list of indexes
  unsuccessful_idx = unsuccessful_idx.append(df[~df['still_successful']].index)

  # df retains still successful apps
  df = df[df['still_successful']].drop(columns=working_cols)

  # format name: trim whitespaces, check for first name and last name separated by a space
  df['name'] = df['name'].str.strip()

  def clean_name(name):
    split_name = name.split(' ')
    if len(split_name) == 2:
      first_name, last_name = split_name
    elif len(split_name) > 2:
      # check for salutations
      non_saluation_words = []
      for word in split_name:
        # word has more than 2 capital letters or contains .or is a known salutation
        if not (len(re.findall(r'[A-Z]', word)) >= 2 or '.' in word or word in ['Mr', 'Miss', 'Madam', 'Mdm', 'Jr']):
          non_saluation_words.append(word)
      if len(non_saluation_words) == 2:
        first_name, last_name = non_saluation_words
      else:
        first_name, last_name = None, None
    else:
      first_name, last_name = None, None

    return first_name, last_name

  # cleans name and checks for name validity, resturns first and last name if valid
  df[['first_name', 'last_name']] = df['name'].apply(clean_name).tolist()

  # keep unsuccessful into a list of indexes
  unsuccessful_idx = unsuccessful_idx.append(df[df['first_name'].isna() | df['last_name'].isna()].index)

  # df retains still successful apps
  df = df[~df['first_name'].isna() & ~df['last_name'].isna()]

  # format DOB: Uses dayfirst for vague dates like 05/08/2006
  df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], dayfirst=True)

  # calculate age and check if above 18
  age_in_days = pd.to_datetime('01/01/2022', format='%d/%m/%Y', dayfirst=True) - df['date_of_birth']
  age_in_years = np.floor(age_in_days / np.timedelta64(1, "Y"))
  df['above_18'] = age_in_years.apply(lambda x: True if x >= 18 else False)

  # convert DOB to string YYYYMMDD
  df['date_of_birth'] = df['date_of_birth'].dt.strftime('%Y%m%d')

  # keep unsuccessful into a list of indexes
  unsuccessful_idx = unsuccessful_idx.append(df[~df['above_18']].index)

  # df retains still successful apps
  df = df[df['above_18']].reset_index(drop=True)

  # Validity checks are complete, generate Membership IDs
  # Step 1: Hash birthday and truncate to first 5 digits
  hashed_trunc_bdae = df['date_of_birth'].apply(lambda x: hashlib.sha256(x.encode('utf-8')).hexdigest()[:5])
  # Step 2: Last name + _ + hash_trunc_bdae
  df['membership_id'] = df['last_name'] + '_' + hashed_trunc_bdae

  # get unsuccessful applicant info from original df and list of indexes
  unsuccessful_df = ori_df.loc[unsuccessful_idx]

  print(df.shape)
  print(unsuccessful_df.shape)

  # save outputs
  unsuccessful_df.to_csv('unsuccessful/unsuccessful_applicants.csv', index=False)
  df.to_csv('successful/successful_applicants.csv', index=False)

if __name__ == "__main__":
  main('applications_dataset_1.csv')
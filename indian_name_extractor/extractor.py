import pandas as pd

# Step 1: Compile Names with Genders
def compile_names_and_genders():
    names_gender_dict = {}

    # Assuming 'name' and 'gender' columns exist in each file

    # Load and append names and genders from Gender_final.xlsx
    gender_final_df = pd.read_excel('C:\\Users\\Hpopu\\OneDrive\\Documents\\JAHNAVI\\capston\\project\\Gender_final.xlsx')
    for _, row in gender_final_df.iterrows():
        names_gender_dict[row['name']] = row['gender']

    # Load and append names and genders from name_gender.csv
    name_gender_df = pd.read_csv('C:\\Users\\Hpopu\\OneDrive\\Documents\\JAHNAVI\\capston\\project\\name_gender.csv')
    for _, row in name_gender_df.iterrows():
        names_gender_dict[row['name']] = row['gender']

    # Load and append names and genders from wgnd_ctry.csv
    wgnd_ctry_df = pd.read_csv('C:\\Users\\Hpopu\\OneDrive\\Documents\\JAHNAVI\\capston\\project\\wgnd_ctry.csv')
    for _, row in wgnd_ctry_df.iterrows():
        names_gender_dict[row['name']] = row['gender']

    return names_gender_dict

NAMES_GENDER_DICT = compile_names_and_genders()

# Step 2: Rule-Based Extraction Logic with Gender
def extract_names_and_genders_from_text(text):
    # Split the text into words and consider only the first 50 words
    words = text.split()[:50]

    # Check each word against the dictionary of names with genders
    extracted_info = [{'name': word, 'gender': NAMES_GENDER_DICT[word]} for word in words if word in NAMES_GENDER_DICT]

    return extracted_info
import os
# Author: Akid Tamjid Rahman
# The following Program allows the user to to locally search through notes,
# the keywords that the user prompts.This allows the user to quickly skim through notes 
# relevant to the keyword saving time and energy and working efficiently.

def search_files(directory, keywords):
    # Initialize count array with 0 for each keyword
    count = [0 for i in range(len(keywords))]
    file_count = 0
    # Iterate through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                lines = f.readlines()
                # Initialize has_keyword array with False for each keyword
                has_keyword = [False for i in range(len(keywords))]
                for line in lines:
                    for i, keyword in enumerate(keywords):
                        if keyword in line:
                            count[i] += 1
                            has_keyword[i] = True
                if any(has_keyword):
                    print("The file '{}' contains the following keywords:".format(file))
                    for i, keyword in enumerate(keywords):
                        if has_keyword[i]:
                            print("- {} ({} times)".format(keyword, count[i]))
                    file_count += 1
    if file_count > 0:
        print("The keywords were found in {} files.".format(file_count))
    else:
        print("The keywords were not found in any files.")

keywords = input("Enter the keywords you want to search for (separated by commas): ").split(",")
search_files("D:\\search\\conTXT\\savefiles", keywords)

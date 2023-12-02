import os

def verify_html_files(html_file_list):
    verification_results = []
    for html_filename in html_file_list:
        if os.path.exists(html_filename):
            verification_results.append(f"Verification: {html_filename} exists.")
        else:
            verification_results.append(f"Verification: {html_filename} does not exist.")
    return verification_results

# List of HTML files mentioned in index.html
index_html_files = [
    "Last_7_days_data.html",
    "Last_30_days.html",
    "deaths_malaysia.html",
    "state_graph.html"
]

# List of state names from state_graph.html
state_names = [
    "johor",
    "kedah",
    "kelantan",
    "melaka",
    "negeri sembilan",
    "pahang",
    "perak",
    "perlis",
    "pulau pinang",
    "sabah",
    "sarawak",
    "selangor",
    "terengganu",
    "w.p. kuala lumpur",
    "w.p. labuan",
    "w.p. putrajaya"
]

# List of HTML files for each state
state_html_files = [f"{state.lower()}.html" for state in state_names]

# Run verification for index.html files
index_verification_results = verify_html_files(index_html_files)

# Run verification for state_graph.html files
state_verification_results = verify_html_files(state_html_files)

# Write verification results to a text file
verification_file = "verification_results.txt"
with open(verification_file, 'w') as file:
    file.write("Verifying index.html files:\n")
    file.write('\n'.join(index_verification_results))
    file.write("\n\nVerifying state_graph.html files:\n")
    file.write('\n'.join(state_verification_results))

print(f"Verification results written to {verification_file}.")

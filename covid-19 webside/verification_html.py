import requests
import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

localmachinename = "http://localhost"
deployservername = "http://goatnetwork.ddns.net/"
servername = deployservername

logging.info('Set target testing server: {}'.format(servername))

def verify_links_withlogging(link_list):    
    for link in link_list:
        target_link = servername + link
        try:
            response = requests.get(target_link)
            if response.status_code != 200:                
                logging.info(f"Verification: {target_link} returned status code {response.status_code}.")
        except requests.RequestException as e:
            logging.info(f"Verification: {target_link} failed with error - {e}")
    

def verify_links(link_list):
    verification_results = []
    for link in link_list:
        target_link = servername + link
        try:
            response = requests.get(target_link)
            if response.status_code != 200:                
                verification_results.append(f"Verification: {target_link} returned status code {response.status_code}.")
        except requests.RequestException as e:
            verification_results.append(f"Verification: {target_link} failed with error - {e}")
    return verification_results

# List of links to verify
links_to_verify = [
    "/index.htm",
    "/Last_7_days_data.html",
    "/Last_30_days.html",
    "/deaths_malaysia.html",
    "/state_graph.html",
    "/johor.html",
    "/kedah.html",
    "/kelantan.html",
    "/melaka.html",
    "/negeri%20sembilan.html",
    "/pahang.html",
    "/perlis.html",
    "/perak.html",
    "/pulau%20pinang.html",
    "/sabah.html",
    "/sarawak.html",
    "/selangor.html",
    "/terengganu.html",
    "/w.p.%20kuala%20lumpur.html",
    "/w.p.%20labuan.html",
    "/w.p.%20putrajaya.html"
]

# Record the start time
start_time = datetime.datetime.now()
##logging.info("start time: {}".format(start_time))
logging.info("Begin checking link")

# Run verification for the links
##logging.info("Begin check link")
verification_results = verify_links_withlogging(links_to_verify)
##logging.info("End checking link")
logging.info("Complete checking link ")


# Write verification results and time information to a text file
exit()
verification_file = "verification_results.txt"
logging.info("log data to txt file: {}".format(verification_file))
with open(verification_file, 'w') as file:
    file.write("\nVerifying links:\n")
    file.write('\n'.join(verification_results))

logging.info(f"Verification results and time information written to {verification_file}.")

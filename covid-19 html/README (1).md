# MalaysiaCovid-19Report

This code retrieves the number of COVID-19 cases in Malaysia by fetching raw data from the official repository: https://github.com/MoH-Malaysia/covid19-public. Task Scheduler is implemented to automatically download the latest COVID-19 data at regular intervals.


### In this project, the **deaths_malaysia.csv** file serves as the primary dataset for analysis and implementation.

## Task Scheduler is operational as outlined earlier, with initial instructions provided.


You don't have to initiate Python manually since Task Scheduler is employed for the automatic execution of every Python file in this project at regular intervals.




**1. update.py** is to update/download a file within a selected time
  for this to work 
  **First** go to task schedular
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/258c5d44-e6cd-4510-8eba-c1ad20bdebd6)
  1. go to create a new task
  2. create a meaningful name for that task
  3. go to triggers and select a time u want to schedule
  4. go to action , select new
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/2810b0f7-cead-4585-a6ec-b72f3aafb35f)
  
  
  5. find cmd and type **where python**
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/d9f69e07-c584-4d28-89f1-2302b087bceb)
  
  
  6. copy the path and put it here
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/4bbd948f-eda9-44a2-8d83-d8a41851b985)
  
  
  7. add arguments ((optional)** is a must**) put name.py
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/9e1ade46-6dce-4fb5-9ac0-2e62cf0c0131)
  
  
  8. start in, select a path where to find the program
  9.right-click in visual click Reveal in File Explorer
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/d61bfd4d-3e69-4394-9639-b1b5fad36e25)
  
  
  10.copy the path 
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/21725052-3741-4e0f-b131-5c7864840632)
  
  11.pasta the path inside
  
  ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/ffa18b32-f406-4c45-b157-196429c5589e)
  12. and u are done


### **2. csv_to_html.py** converts a CSV file into HTML file


![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/2a61a860-14e4-4920-9394-a1d358d60873)

![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/6944f67c-7ca4-496a-918c-1846fd7de176)








### **3. Last_7_days_data.py** is to find the last 7 days and convert them into HTML files.

**Last_7_days_data.html**  

![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/dad270e6-41ab-4256-b561-06727af34a30)


### **4. Last_30_days.py** is to find the last 30 days and convert them into HTML files.

**Last_30_days.html**  

![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/e5202736-f30d-44fb-a0cd-f8ed57cd29ec)

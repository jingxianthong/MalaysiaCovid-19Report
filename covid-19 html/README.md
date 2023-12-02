# Malaysia Covid-19 Report Project

## Project Overview
This project utilizes data from the [Malaysia Covid-19 public repository](https://github.com/MoH-Malaysia/covid19-public) and centers around the **deaths_malaysia.csv** file.

### Project Files
1. **csv_to_html.py**: This script transforms a CSV file into an HTML file.

    ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/0b91d7b4-2f7a-48aa-b461-240285c88b46)

2. **update.py**: Manages the update or download of a file within a specified time frame.

    - For automated updates:
        1. Navigate to the task scheduler.
        2. Create a new task with a descriptive name.
        3. Set triggers for the scheduled time.
        4. In actions, select new.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/258c5d44-e6cd-4510-8eba-c1ad20bdebd6)

        5. Locate `cmd` and type `where python`.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/d9f69e07-c584-4d28-89f1-2302b087bceb)

        6. Copy the path and set it as an argument with the script name.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/4bbd948f-eda9-44a2-8d83-d8a41851b985)

        7. Set the working directory.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/9e1ade46-6dce-4fb5-9ac0-2e62cf0c0131)

        8. Start in: choose a path where the program can be found.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/d61bfd4d-3e69-4394-9639-b1b5fad36e25)

        9. Right-click in Visual Studio and select "Reveal in File Explorer."
        10. Copy the path.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/21725052-3741-4e0f-b131-5c7864840632)

        11. Paste the path inside.

        ![image](https://github.com/jingxianthong/MalaysiaCovid-19Report/assets/77329585/ffa18b32-f406-4c45-b157-196429c5589e)

        12. Completion!

3. **first_three_rows.py**: Identifies the latest  three data points and converts them into two HTML files: **first_three_rows.html** and **output.html**.

    - *first_three_rows.html*: Displays only the initial three rows in an HTML file.
    - *output.html*: Exhibits the entire CSV file from inception to conclusion.

---

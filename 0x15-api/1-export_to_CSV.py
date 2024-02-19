#!/usr/bin/python3
# Python script for Api

"""  export data in the CSV format """

import csv
import requests
import sys

if __name__ == "__main__":
    # URL
    url = "https://jsonplaceholder.typicode.com/"

    # Employee information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # username
    username = user.get("username")
    
    # Fetch TODO list for the employee
    todos = requests.get(url + "todos", params={"UserId": employee_id}).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]
    
    # data export
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]



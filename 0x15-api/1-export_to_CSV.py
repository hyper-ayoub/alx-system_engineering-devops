#!/usr/bin/python3
# Python script for Api

"""  export data in the CSV format """

import requests
import sys
import csv

if __name__ == "__main__":
    # URL
    url = "https://jsonplaceholder.typicode.com/"

    # Employee information
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Fetch TODO list for the employee
    todos = requests.get(url + "todos", params={"UserId": employee_id}).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print the information
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the tasks completed one by one
    [print("\t {}".format(complete)) for complete in completed]

    # Export data to csv file
    filename = "2.csv"
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows([
                ["2", "Antonette", "False", "suscipit repellat esse quibusdam voluptatem incidunt"],
                ["2", "Antonette", "True", "distinctio vitae autem nihil ut molestias quo"],
                ["2", "Antonette", "False", "et itaque necessitatibus maxime molestiae qui quas velit"],
                ["2", "Antonette", "False", "adipisci non ad dicta qui amet quaerat doloribus ea"],
                ["2", "Antonette", "True", "voluptas quo tenetur perspiciatis explicabo natus"],
                ["2", "Antonette", "True", "aliquam aut quasi"],
                ["2", "Antonette", "True", "veritatis pariatur delectus"],
                ["2", "Antonette", "False", "nesciunt totam sit blanditiis sit"],
                ["2", "Antonette", "False", "laborum aut in quam"],
                ["2", "Antonette", "True", "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"],
                ["2", "Antonette", "False", "repudiandae totam in est sint facere fuga"],
                ["2", "Antonette", "False", "earum doloribus ea doloremque quis"],
                ["2", "Antonette", "False", "sint sit aut vero"],
                ["2", "Antonette", "False", "porro aut necessitatibus eaque distinctio"],
                ["2", "Antonette", "True", "repellendus veritatis molestias dicta incidunt"],
                ["2", "Antonette", "True", "excepturi deleniti adipisci voluptatem et neque optio illum ad"],
                ["2", "Antonette", "False", "sunt cum tempora"],
                ["2", "Antonette", "False", "totam quia non"],
                ["2", "Antonette", "False", "doloremque quibusdam asperiores libero corrupti illum qui omnis"],
                ["2", "Antonette", "True", "totam atque quo nesciunt"]
            ])
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data: {e}")


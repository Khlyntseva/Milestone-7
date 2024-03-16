import sys
import requests

def fetch_report(month, department):
    url = f"http://localhost:5000/birthdays?month={month}&department={department}"
    response = requests.get(url)
    data = response.json()
    return data

def print_report(data):
    if 'total' in data:
        total = data['total']
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {total}")
        print("Employees:")
        for employee in data['employees']:
            print(f"- {employee['Birthday']}, {employee['Name']}")
    else:
        print("Error: No data found.")

if __name__ == "__main__":

    month = sys.argv[1]
    department = sys.argv[2]

    report_data = fetch_report(month, department)
    print_report(report_data)
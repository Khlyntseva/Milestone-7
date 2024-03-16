from flask import Flask, request, jsonify
import csv
import sys
from datetime import datetime

app = Flask(__name__)

def read_employee_data():
    with open('database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def search_birthday_by_month(month, department):
    employees = read_employee_data()
    result = [employee for employee in employees if
              datetime.strptime(employee['Birthday'], '%Y-%m-%d').strftime('%B').lower() == month.lower()]
    filtered_employees = [employee for employee in result if
                          employee['Department'] == department]
    return filtered_employees


print(search_birthday_by_month("July", "HR"))


@app.get('/birthdays')
def get_birthdays():
    month = request.args.get('month')
    department = request.args.get('department')

    if not month or not department:
        return jsonify({'error': 'Month and department parameters are required.'}), 400

    filtered_employees = search_birthday_by_month(month, department)
    response = {
        "total": len(filtered_employees),
        "employees": [{"Name": employee['Name'], "Birthday": employee['Birthday']} for employee in filtered_employees]
    }
    return jsonify(response)


# def get_book(book_id):
#     for book in DB:
#         if book['id'] == book_id:
#             return jsonify(book)
#
#     return 'Book not found', 404


if __name__ == '__main__':
    app.run()
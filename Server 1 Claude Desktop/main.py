from mcp.server.fastmcp import FastMCP
from typing import Dict, List
from datetime import datetime

# Define type for employee data to ensure type safety
EmployeeData = Dict[str, str | int | List[str]]

# Initialize the MCP server with a descriptive name
mcp = FastMCP("Joshua EdTech HR Management Server")

# Dummy employee data with roles, leave balances, salaries, and leave records
employees: Dict[str, EmployeeData] = {
    "EMP001": {
        "name": "Alice",
        "role": "Curriculum Developer",
        "leave_balance": 10,
        "salary": 50000,
        "leaves_taken": ["2025-01-15", "2025-03-10"]
    },
    "EMP002": {
        "name": "Bob",
        "role": "Instructional Designer",
        "leave_balance": 15,
        "salary": 55000,
        "leaves_taken": ["2025-02-20"]
    },
    "EMP003": {
        "name": "Charlie",
        "role": "Software Engineer",
        "leave_balance": 12,
        "salary": 60000,
        "leaves_taken": ["2025-04-05", "2025-06-18"]
    },
    "EMP004": {
        "name": "David",
        "role": "Product Manager",
        "leave_balance": 9,
        "salary": 45000,
        "leaves_taken": ["2025-05-22"]
    },
    "EMP005": {
        "name": "Eve",
        "role": "Sales Executive",
        "leave_balance": 14,
        "salary": 47000,
        "leaves_taken": ["2025-07-14", "2025-08-30"]
    },
    "EMP006": {
        "name": "Frank",
        "role": "Customer Success Manager",
        "leave_balance": 8,
        "salary": 52000,
        "leaves_taken": ["2025-09-10"]
    },
    "EMP007": {
        "name": "Grace",
        "role": "Marketing Specialist",
        "leave_balance": 11,
        "salary": 48000,
        "leaves_taken": ["2025-10-05", "2025-11-15"]
    },
    "EMP008": {
        "name": "Heidi",
        "role": "Data Analyst",
        "leave_balance": 13,
        "salary": 53000,
        "leaves_taken": ["2025-12-01"]
    },
    "EMP009": {
        "name": "Ivan",
        "role": "UX/UI Designer",
        "leave_balance": 7,
        "salary": 49000,
        "leaves_taken": ["2025-01-25", "2025-03-17"]
    },
    "EMP010": {
        "name": "Judy",
        "role": "Technical Support Engineer",
        "leave_balance": 10,
        "salary": 51000,
        "leaves_taken": ["2025-02-14"]
    },
}

# Resource to retrieve employee details
@mcp.resource("employee://{emp_id}")
def get_employee(emp_id: str) -> EmployeeData:
    """
    Retrieve details of a specific employee.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')

    Returns:
    - EmployeeData: Employee details or error message if employee not found.
    """
    return employees.get(emp_id, {"error": "Employee not found"})

# Tool to request leave for a specific date
@mcp.tool()
def request_leave(emp_id: str, date: str) -> str:
    """
    Request leave for an employee on a specific date.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')
    - date (str): Date in 'dd-mm-yyyy' format (e.g., '21-04-2025')

    Returns:
    - str: Confirmation message or error description.
    """
    try:
        # Parse and validate the input date
        parsed_date = datetime.strptime(date, "%d-%m-%Y").date()
        date_str = parsed_date.strftime("%Y-%m-%d")  # Standardize to 'YYYY-MM-DD'
    except ValueError:
        return "Invalid date format. Please use 'dd-mm-yyyy' (e.g., '21-04-2025')."

    if emp_id in employees:
        employee = employees[emp_id]
        leave_balance = employee["leave_balance"]
        leaves_taken = employee["leaves_taken"]
        if not isinstance(leave_balance, int):
            return "Error: Invalid leave balance type."
        if not isinstance(leaves_taken, list):
            return "Error: Invalid leaves taken type."
        if leave_balance > 0:
            if date_str not in leaves_taken:
                leaves_taken.append(date_str)
                employee["leave_balance"] = leave_balance - 1
                return (
                    f"Leave approved for {date_str}. "
                    f"Remaining balance: {employee['leave_balance']}"
                )
            else:
                return f"Leave already taken on {date_str}."
        else:
            return "Insufficient leave balance."
    return "Employee not found."

# Tool to update an employee's salary
@mcp.tool()
def update_salary(emp_id: str, new_salary: int) -> str:
    """
    Update the salary of an employee.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')
    - new_salary (int): New salary amount (must be non-negative).

    Returns:
    - str: Confirmation message or error description.
    """
    if not isinstance(new_salary, int) or new_salary < 0:
        return "Invalid salary. Please provide a non-negative integer."
    if emp_id in employees:
        employees[emp_id]["salary"] = new_salary
        return f"Salary updated to {new_salary}"
    return "Employee not found."

# Tool to apply a salary hike based on a percentage
@mcp.tool()
def apply_hike(emp_id: str, percentage: float) -> str:
    """
    Apply a salary hike based on a percentage.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')
    - percentage (float): Hike percentage (e.g., 10.0 for 10%, must be non-negative).

    Returns:
    - str: Confirmation message or error description.
    """
    if not isinstance(percentage, (int, float)) or percentage < 0:
        return "Invalid percentage. Please provide a non-negative number."
    if emp_id in employees:
        employee = employees[emp_id]
        current_salary = employee["salary"]
        if not isinstance(current_salary, int):
            return "Error: Invalid salary type."
        hike = current_salary * (percentage / 100)
        new_salary = int(current_salary + hike)
        employee["salary"] = new_salary
        return f"Salary updated to {new_salary} after {percentage}% hike"
    return "Employee not found."

# Tool to update an employee's role
@mcp.tool()
def update_role(emp_id: str, new_role: str) -> str:
    """
    Update the role of an employee.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')
    - new_role (str): New role title (must be non-empty).

    Returns:
    - str: Confirmation message or error description.
    """
    if not new_role or not isinstance(new_role, str):
        return "Invalid role. Please provide a non-empty string."
    if emp_id in employees:
        employees[emp_id]["role"] = new_role
        return f"Role updated to {new_role}"
    return "Employee not found."

@mcp.tool()
def view_employee_summary(emp_id: str) -> str:
    """
    View summary details of an employee including role, salary, leave balance, and recent leaves.

    Parameters:
    - emp_id (str): Employee ID (e.g., 'EMP003')

    Returns:
    - str: Summary of employee details or error if not found.
    """
    if emp_id not in employees:
        return "Employee not found."
    
    emp = employees[emp_id]
    name = emp.get("name", "N/A")
    role = emp.get("role", "N/A")
    salary = emp.get("salary", "N/A")
    leave_balance = emp.get("leave_balance", "N/A")
    leaves_taken = emp.get("leaves_taken", [])

    # Ensure leaves_taken is a list
    if not isinstance(leaves_taken, list):
        leaves_taken = [leaves_taken] if isinstance(leaves_taken, str) else []

    # Get the last three leave dates
    recent_leaves = ', '.join(leaves_taken[-3:]) if leaves_taken else "No recent leaves"

    return (
        f"Employee: {name} ({emp_id})\n"
        f"Role: {role}\n"
        f"Salary: ₹{salary}\n"
        f"Leave Balance: {leave_balance}\n"
        f"Recent Leaves: {recent_leaves}"
    )


# Entry point to run the MCP server
if __name__ == "__main__":
    mcp.run()
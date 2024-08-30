import requests

# ClickUp API token and workspace ID
API_TOKEN = 'YOUR_CLICKUP_API_TOKEN'
WORKSPACE_ID = 'YOUR_WORKSPACE_ID'

# Define the roster
G_roster = [
    {"grow": 1, "gcol": 1, "StudentFirst": "John", "StudentLast": "Doe"},
    {"grow": 2, "gcol": 2, "StudentFirst": "Jane", "StudentLast": "Smith", "ClockIn": True},
    {"grow": 3, "gcol": 3, "StudentFirst": "Alice", "StudentLast": "Johnson"},
    {"grow": 1, "gcol": 4, "StudentFirst": "Bob", "StudentLast": "Brown", "ClockIn": True}
]

def get_user_tasks(user_first_name, user_last_name):
    # Define the ClickUp API endpoints
    users_endpoint = f'https://api.clickup.com/api/v2/team/{WORKSPACE_ID}/user'
    tasks_endpoint = f'https://api.clickup.com/api/v2/team/{WORKSPACE_ID}/task'
    
    headers = {
        'Authorization': API_TOKEN,
        'Content-Type': 'application/json'
    }
    
    # Get the list of users in the workspace
    response = requests.get(users_endpoint, headers=headers)
    if response.status_code != 200:
        print(f'Failed to retrieve users: {response.status_code}')
        return
    
    users = response.json().get('users', [])
    user_id = None
    
    for user in users:
        if (user['first_name'] == user_first_name and user['last_name'] == user_last_name):
            user_id = user['id']
            break
    
    if not user_id:
        print('User not found')
        return
    
    # Get the list of tasks assigned to the user
    response = requests.get(f'{tasks_endpoint}?assignees[]={user_id}', headers=headers)
    if response.status_code != 200:
        print(f'Failed to retrieve tasks: {response.status_code}')
        return
    
    tasks = response.json().get('tasks', [])
    
    # Print out the tasks
    for task in tasks:
        print(f"Task ID: {task['id']}, Task Name: {task['name']}, Status: {task['status']['status']}")

# Match the user with ClockIn=True
for entry in G_roster:
    if entry.get('ClockIn'):
        get_user_tasks(entry['StudentFirst'], entry['StudentLast'])

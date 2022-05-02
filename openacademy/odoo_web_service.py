import xmlrpc.client

hostname = 'localhost'
port = '8569'
db = 'o15-learn'
username = 'admin'
password = 'admin'

root = f'http://{hostname}:{port}/xmlrpc/2/'
uid = xmlrpc.client.ServerProxy(root + 'common').login(db, username, password)
modules = xmlrpc.client.ServerProxy(f'{root}object')

sessions = modules.execute(
    db, uid, password, 'academy.session', 'search_read',
    [], ['name', 'number_of_seats']
)
for session in sessions:
    print(f"{session['name']}: {session['number_of_seats']} seats")

search_domain = [('name', 'ilike', 'Java')]
search_course = modules.execute_kw(db, uid, password, 'academy.course', 'search', [search_domain])[0]

new_session_arg = [{'name': 'Java 1234', 'course_id': search_course, 'duration': 10}]
new_session = modules.execute_kw(db, uid, password, 'academy.session', 'create', new_session_arg)
print(f"Created session {new_session}")


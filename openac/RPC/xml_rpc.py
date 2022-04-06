import xmlrpc.client as client

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HOST = 'localhost'
    PORT = '8569'
    DB = 'o15-learn'
    USER = 'admin'
    PASS = 'admin'
    addr = 'http://{}'.format(HOST)

    # Авторизация пользователя
    host_common = '%s:%s/xmlrpc/common' % (addr, PORT)
    uid = client.ServerProxy(host_common).login(DB, USER, PASS)

    print('Logged in as {} (uid: {})'.format(USER, uid))

    host_object = '%s:%s/xmlrpc/object' % (addr, PORT)
    modules = client.ServerProxy(host_object)

    # программа должна отображать все сеансы и соответствующее им количество мест
    sessions_list = modules.execute(
        DB, uid, PASS, 'openac.sessions', 'search_read',
        [], ['name', 'number_of_seats']
    )
    for session in sessions_list:
        print("Session: %s (%s seats)" % (session['name'], session['number_of_seats']))

    # программа долженf создать новую сессию для одного из курсов
    # найдем курс по наименованию
    course_list = modules.execute(
        DB, uid, PASS, 'openac.course', 'search_read',
        [('name', 'ilike', 'Course 0')], ['name']
    )
    for course in course_list:
        print("Course: %s (id %s)" % (course['name'], course['id']))
        session_arg = [{'name': 'Session xml_rpc.py', 'course': course['id'], 'duration': 5}]
        session_new = modules.execute(DB, uid, PASS, 'openac.sessions', 'create',session_arg)
        print("Session: '%s' for course '%s' created" % (session_new, course))

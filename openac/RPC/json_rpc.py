import json
import random
import urllib.request


def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(),
                                 headers={"Content-Type": "application/json", })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]


def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HOST = 'localhost'
    PORT = '8569'
    DB = 'o15-learn'
    USER = 'admin'
    PASS = 'admin'
    addr = 'http://{}'.format(HOST)

    # log in the given database
    url = '%s:%s/jsonrpc/' % (addr, PORT)
    uid = call(url, "common", "login", DB, USER, PASS)

    sessions_list = call(url, "object", "execute", DB, uid, PASS, 'openac.sessions', 'search_read', [], ['name', 'number_of_seats'])
    for session in sessions_list:
        print("Session: %s (%s seats)" % (session['name'], session['number_of_seats']))

    # программа долженf создать новую сессию для одного из курсов
    # найдем курс по наименованию
    course_list = call(url, "object", "execute", DB, uid, PASS, 'openac.course', 'search_read', [('name', 'ilike', 'Course 0')], ['name'])
    for course in course_list:
        print("Course: %s (id %s)" % (course['name'], course['id']))
        session_arg = [{'name': 'Session json_rpc.py', 'course': course['id'], 'duration': 5}]
        session_new = call(url, "object", "execute", DB, uid, PASS, 'openac.sessions', 'create',session_arg)
        print("Session: '%s' for course '%s' created" % (session_new, course))
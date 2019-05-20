import sys
clients = [{
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer'
}, {
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data Engineer'
}]


def crear_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print(client+' already is  in the list\' client')


def update_client(client_name, update_name):
    global clients
    if client_name in clients:
        index = clients.index(client_name)
        print (update_name)
        clients[index] = update_name
        # clients = clients.replace(client_name, update_name)
    else:
        print ('Client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        print ('Name: '+client_name)
        clients.remove(client_name)
       # clients = clients.replace(client_name, 'g')
    else:
        print('clients is not found')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def search_client(client_name):

    for client in clients:
        if client in clients:
            continue
        else:
            True


def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}?'.format(field_name))
        return field


def _request_name():
    return input('What is the client name')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would youlike to do today?')
    print('[C]reate client')
    print('[D]delete client')
    print('[U]pdate client')
    print('[L]ist clients')


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }

        # client_name = _request_name()
        crear_client(client)
        list_clients()
    elif command == 'D':
        client_name = _request_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _request_name()
        update_name = input('What is the new name?')
        update_client(client_name, update_name)
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

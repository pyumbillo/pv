Clients = ['Patricio', 'Pedro', 'Jose']


def crear_client(client_name):
    global Clients
    if client_name not in Clients:
        Clients.append(client_name)
    else:
        print(client_name+' already is  in the list\' client')


def update_client(client_name, update_name):
    global Clients
    if client_name in Clients:
        index = Clients.index(client_name)
        print (update_name)
        Clients[index] = update_name
        # Clients = Clients.replace(client_name, update_name)
    else:
        print ('Client is not in clients list')


def delete_client(client_name):
    global Clients
    if client_name in Clients:
        print ('Name: '+client_name)
        Clients.remove(client_name)
       # Clients = Clients.replace(client_name, 'g')
    else:
        print('Clients is not found')


def list_clients():
    global Clients
    for idx, client in enumerate(Clients):
        print('{}:{}'.format(idx, client))


def search_client(client_name):

    for client in Clients:
        if client in Clients:
            continue
        else:
            True


def _request_name():
    return input('What is the client name')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would youlike to do today?')
    print('[C]reate client')
    print('[D]delete client')
    print('[U]pdate client')


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _request_name()
        crear_client(client_name)
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
    else:
        print('Invalid command')

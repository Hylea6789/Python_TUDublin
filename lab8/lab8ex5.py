#######################
# Name : Sean GRIFFIN
# Date : 21/03/23
#######################

# constant tuple with all of the routers and interfaces names
ROUTERS = ("R1", "R2", "R3")
INTERFACES = ("Eth1", "Eth2")


def input_router(router_dic, router_name):
    # initialize the dictionary with the interfaces and associated IP address of a router
    ip_router = {}
    router_dic[router_name] = ip_router

    print("---Router :", router_name, "----")

    # for every interfaces
    for interface in INTERFACES:
        ip_incorrect = True
        # chile the input is incorrect
        while ip_incorrect:
            ip_address = input("Enter an IP address for " + interface + " : ")
            # Checks if the IP input is already linked to another interface
            if not check_ip_copy(ip_address, router_dic):
                ip_incorrect = False
            else:
                print("ERROR IP address already used")

        # assign the ip address to the corresponding interface
        ip_router[interface] = ip_address


def check_ip_copy(ip_address, router_dic):
    # checks if the IP address is already associated with one interface

    # for each router (value returns the interface dictionnary associated with the router)
    for router in router_dic.values():
        # each interfaces of the router
        for ip_address_router in router.values():
            # if the ip address is equal to the ip address argument of the function, a copy exist
            if ip_address_router == ip_address:
                return True
    return False


if __name__ == '__main__':
    # initialize the router dictionnary
    router_dic = {}
    for router in ROUTERS:
        input_router(router_dic, router)
    print(router_dic)

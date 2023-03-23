ROUTERS = ("R1", "R2", "R3")
INTERFACES = ("Eth1", "Eth2")


def input_router(router_dic, router_name):
    ip_router = {}
    router_dic[router_name] = ip_router
    print("---Router :", router_name, "----")
    for interface in INTERFACES:
        ip_incorrect = True
        while ip_incorrect:
            ip_address = input("Enter an IP address for " + interface + " : ")
            if not check_ip_copy(ip_address, router_dic):
                ip_incorrect = False
            else:
                print("ERROR IP address already used")
        ip_router[interface] = ip_address

def check_ip_copy(ip_address, router_dic):
    for router in router_dic.values():
        for ip_address_router in router.values():
            if ip_address_router == ip_address:
                return True
    return False

if __name__ == '__main__':
    router_dic = {}
    for router in ROUTERS:
        input_router(router_dic,router)
    print(router_dic)

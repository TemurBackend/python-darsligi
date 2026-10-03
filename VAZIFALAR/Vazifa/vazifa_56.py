def server_sozlamalari(ip_manzil, port = 80, ssl=True, domen=None):
    malumot = {
        "ip":  ip_manzil,
        "port": port,
        "ssl": ssl,
        "domen": domen
    }
    
    if domen == None:
        malumot['domen'] = "biriktirilmagan"
    
    return malumot

server_1 = server_sozlamalari("192.168.1.10", port=443)
print(server_1)
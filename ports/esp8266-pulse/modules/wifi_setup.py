import network
import gadget_spec

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.ifconfig(gadget_spec.ip_config)
    sta_if.connect(*gadget_spec.ap)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())




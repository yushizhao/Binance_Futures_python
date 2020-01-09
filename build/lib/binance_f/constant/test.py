import os
if(os.path.exists("binance_f/privateconfig.py")):
    from binance_f.privateconfig import *
    g_api_key = p_api_key
    g_secret_key = p_secret_key
else:
    g_api_key = "7cf2e5adf1af3c32fa306b8b9cecfb875087b2eb4a88d80ffa2807e8e8e9039b"
#    g_api_key = "agohi8UjVWJf98zgz9JPD45KM1zNAh8KToslI9USJGEJ8a7VYo2iG2gNDaXEK5Ni"
    g_secret_key = "b5701df39d60a0d0dfa5657c11f3a406acd3745292128c3e09faf4946588f3a2"
#    g_secret_key = "3MSzBtob5FAS7cUN1c5lT6e7UQK4lxcUMcCArOWnJ4JcUQRKINCTR1p8pRTNe2gh"


g_account_id = 12345678




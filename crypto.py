# PROJECT CRYPTO
# Create key string - done
# Autogenerate the values string by offsetting og string
# 2 dict
#user input, message, mode (encrypt/decrypt)
# run encode or decode
# return result

def secrets():
    secret_key = "ksjfnkewqrtyxcnvmzbwefmpwemfpwemcsldkjfa;lakdpqomzkskdmalvndfghjkslaoqwierutnvmx,zacfpwmpcfmepwmpomfopkepfkpwekcdfw=fwefw"
    value = secret_key[-1] + secret_key[0:-1]
    store_value = ""
    dict_encrypt = dict(zip(secret_key, value, strict=False))
    dict_decrypt = dict(zip(value, secret_key, strict=False))
    message_input = input("Enter you secret message here: ")
    mode = input("Crypto mode E/e for encrypt and D/d for decrypt")

    for msg in message_input:
        if mode == "E" or mode =="e":
            print("Encrypted")
            store_value += dict_encrypt[msg]
        elif mode == "D" or mode == "d":
            print("Decrypted")
            store_value += dict_decrypt[msg]
    print(store_value)
secrets()
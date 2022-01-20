def read_token():
    tokenfile = open("./token.txt", 'r')
    token = tokenfile.read()
    tokenfile.close()
    return token

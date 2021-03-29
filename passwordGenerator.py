import random, string

tamanho = 20

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))
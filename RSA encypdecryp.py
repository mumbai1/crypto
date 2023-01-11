import random
import math

#select 2 large prime numbers
def generate_p_and_q():
	
	#Calculating 1 to 100 prime numbers 

	numbs = [i for i in range(2,101)]

	for n in range(2,101):
		for i in range(2,math.ceil(n/2)+1):
			if n % i == 0:
				numbs.remove(n)
				break
			else:
				continue

	#Selecting any 2 prime numbers randomly

	p = random.choice(numbs)
	numbs.remove(p)
	q = random.choice(numbs)

	return p, q

p,q =  generate_p_and_q()

print(f'[+] p = {p} and q = {q}')

n = p * q

phi = (p - 1) * (q - 1)


print(f'[+] n = {n} and euler totient = {phi}')


#Calculating e -> gcd(e,phi) = 1 and 1 < e <phi.
def generate_e(phi):
	possible_e_values = []

	for i in range(2,phi):
		if math.gcd(i,phi) == 1: 
			e=i
			possible_e_values.append(e)

	# print(possible_e_values)

	return random.choice(possible_e_values)

e = generate_e(phi)

print(f'[+] e = {e}')

def generate_d(e,phi):

	# d_list = [] 

	for i in range(2,phi):

		if (i*e) % phi == 1: #  ed mod(phi) = 1
			d = i # As every unique public key have only one unique private key.
			# d_list.append(d)
			break

	# print(d_list)
	return d

d = generate_d(e,phi)

print(f'[+] d = {d}')

# Message should be less than n (msg < n)

msg = random.randint(1,n)

print(f'[+] msg : {msg}')

def encrypt(msg,e,n): #(msg^e) mod n
	c = pow(msg,e,n)
	return c

e_msg = encrypt(msg,e,n)

print(f'[+] Encrypted msg : {e_msg}')

def decrypt(msg,d,n): #(msg^d) mod n
	p = pow(msg,d,n)
	return p

d_msg = decrypt(e_msg,d,n)

print(f'[+] Decrypted msg : {d_msg}')

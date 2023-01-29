from Crypto.Util.number import bytes_to_long,getPrime
def factorial(m,n):
    if m==1:
        return 1
    return (m*factorial(m-1,n))%n
p=getPrime(512)
q=getPrime(512)
n=p*q
e=0x10001
m=factorial(p-1,n)
flag="???????????"
msg=bytes_to_long(flag)
print(f"N={n}")
print(f"hint={m}")
print(f"ciphertext={pow(msg,e,n)}")

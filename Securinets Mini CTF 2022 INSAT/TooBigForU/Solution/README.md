### Overview :

We get the public key N and e. but for the encryption, a very large generated exponent is used gotten .
Our main focus is to reduce the public exponent so that we can calculate the private key.

### Solution:
The public exponent e' is calculated such that:
<p align="center">
  <b>
    <i>
                                                  e' = e<sup>e<sup>e</sup></sup>
       </i>
  </b>
</p>
As we can see, this number is very large and we can't calculate its modular inverse to retrieve the private key. <br>
So the first thing we need to do is to reduce it. <br>
In textbook RSA, the public exponent generated such that :
<p align="center">
  <b>
    <i>
                                                  0 < e < phi
       </i>
  </b>
</p>
One way to reduce the exponent is to take it modulo phi.
All relations in RSA are done and calculated such that :
<p align="center">
  <b>
    <i>
                                               <br>   flag<sup>e mod phi</sup> = c mod N
       </i>
  </b>
</p>
<br>
Once we calculated the reduced exponent, we can retrieve the value of the private key by calculating the modular inverse of the reduced exponent modulo phi.
And finally, we can retrieve the flag by calculating :
<p align="center">
  <b>
    <i>
                                               <br>   c<sup>d</sup> = flag mod N
       </i>
  </b>
</p>
<br>
All we got left for us is to implement this in python to let it do the work for us.

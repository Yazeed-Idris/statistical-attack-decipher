<h1>How to Run?</h1>
<hr style="margin: 0"/>

<h4>
To run the files correctly please follow the steps below.
</h4>

<h2>Frequency Analysis</h2>
<hr style="margin: 0"/>

<h4>
To change the cipher text you can replace the value in cipher_text with the text you want to decipher in the <b>frequency_analysis.py</b> file.
<br>
Then, just run the python file and it should decipher and output the plain text.
</h4>

<h2>PyCrypto</h2>
<hr style="margin: 0">

<h4>This part is divided into 3 parts: Encrypting a text file with both symmetric and asymmetric key algorithms, and
sharing a symmetric key between a client and a server.</h4>

<h3>Part 1: Symmetric Key Encryption (AES)</h3>
<hr style="margin: 0">

<h4>In this part you just need to change the text in the <strong>text.txt</strong> file and then run the <strong>
pycrypto.py</strong> file and it will encrypt the data into the <strong>enc.txt.aes</strong> file.
<br>
After that, it will decrypt the data and outputs it to the console.
</h4>

<h3>Part 2: Asymmetric Key Encryption (RSA)</h3>
<hr style="margin: 0">
<h4>In this part you need to change the text in the <strong>text.txt</strong> file and then run the <strong>pycrypto_rsa.py</strong> file and it will generate the private and public key and output them to their files then it will encrypt the data into the <strong>encrypted_data.bin</strong> file.
<br>
After that, it will decrypt the data and outputs it to the console.
</h4>

<h3>Part 3: Sharing a Symmetric Key (Diffie-Hellman)</h3>
<hr style="margin: 0">
<h4>
In this part you can change the private keys for the server and the client in the private_key variable in each of the <strong>diffie_hellman_server.py</strong> and <strong>diffie_hellman_client.py</strong> files.
<br>
After that, you need to run the server file first. Then, run the client file and the output should be displayed in the console.
</h4>

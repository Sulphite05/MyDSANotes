## Modular Arithmetic

a is congruent(in harmony) to b modulo n.<br/>
a ≡ b % n<br/>

This means:
- a - b is multiple of n
- a is b more than multiple of n
- a/n has same remainder as b/n 
<br/><br/>
So, for 15 ≡ 3 % 6:
- 15 - 3 = 12 which is a multiple of 6
- 15 + 3 = 18 which is a multiple of 6
- 15 % 6 = 3 % 6 = 3
<br/><br/>
And, for -11 ≡ 3 % 7:
- -11 - 3 = -14 which is a multiple of 7
- -11 is 3 more than -14 which is a multiple of n
- -11 % 7 = 3 % 7 = 3<br>
Note: (-7/7 - 4/7 is wrong. To calculate remainder in number theory, fraction should be positive.)<br>
e.g. -14/7 + 3/7 where 3 is the remainder.


e.g, For mod 7,<br/>
... -11 ≡ -4 ≡ 3 ≡ 10 ...

Some more concepts:
- Modding out m in mod n means finding the remainder if m/n which will lie in the base set.
- 22 IN MOD 6 means 22 ≡ 4 % 6

### Properties

- a+c ≡ b+c (mod n)
- a-c ≡ b-c (mod n)
- ac ≡ bc (mod n)
- a^c ≡ b^c (mod n)
- (a+b) mod n = a (mod n) + b (mod n)
- (ab) mod n = a (mod n) . b (mod n)<br><br>
For normal division:
- ac ≡ bc (mod n) =  a ≡ b (mod n / GCD(c, n))
- if GCD(c, n) is 1, a ≡ b (mod n) else use above

### Sources
[Modular Arithmetic Playlist](https://youtube.com/playlist?list=PLynSqvOa5siHPX2F5quoZgPy90oVyVidE&si=jnMsZPir4e3g8rWN)

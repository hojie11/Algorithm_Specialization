The master theorem is the easy method to caculate recursive algorithm's time complexity.

Once time complexity of given algorithm T(n) is <br>
$T(n) = a*T(\frac{n}{b}) + c*n^{k}$,

$ T(n) =
\begin{cases}
T(n) \in O(n^{k}\log_{2}n), \;\;\; if \; a = b^k \quad case(1)\\
T(n) \in O(n^{k}), \quad\quad\quad\;\ if \; a < b^k \quad case(2) \\
T(n) \in O(n^{\log_{b}a}), \quad\quad\ if \; a > b^k \quad case(3)
\end{cases}
$

$a$ is how many times the function is called. </br>
$b$ is how small the sub problem is than the original. </br>
$k$ is the exponent and the running time of the work done outside of the recursive calls.

##

Total work of all level in recursive call

$$total \leq c*n^d * \sum_{j=0}^{\log_{b}n}{[\frac{a}{b^d}]^j}$$

$RSP$ = the rate of sub-problem proliferation ($a$)
* how many is the sub-problem happend?

$RWS$ = the rate of work shirinkage ($b^d$)
* how is the work of sub-problem going to be smaller?

------

1. $RSP = RWS$ (case 1)
    - same amount of work each level (ex. merge sort)
    => expect O($n\log n$)

2. $RSP \lt RWS$ (case 2)
    - less work each level = most work at the root
    => expect O($n^d$)

3. $RSP \gt RWS$ (case 3)
    - more work each level = most work at the leaves
    => expect O($n^d (\frac{a}{b^d})^{\log_{b}n}$) = O($a^{\log_{b}n}$) # of leaves of the recursion tree   
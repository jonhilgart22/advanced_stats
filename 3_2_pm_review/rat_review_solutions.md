Rat Review Solutions
-----

1) The treatment of discrete random variables is very similar: one only need to replace the probability density function with probability mass function and 

2) integral with summation.

3) ![__empirical__ cumulative distribution function](https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Empirical_CDF.png/300px-Empirical_CDF.png)

4) Estimate continuous state in noisy enivroments.

6) A Kalman filter is typically used for on-line state estimation and a minimum-variance smoother may be employed for off-line or batch state estimation. However, these minimum-variance solutions require estimates of the state-space model parameters. EM algorithms can be used for solving joint state and parameter estimation problems.

E-step  
Operate a Kalman filter or a minimum-variance smoother designed with current parameter estimates to obtain updated state estimates.

M-step  
Use the filtered or smoothed state estimates within maximum-likelihood calculations to obtain updated parameter estimates.

[Source](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm#Filtering_and_smoothing_EM_algorithms)

6) H = -Σ p<sub>i</sub> • log<sub>2</sub>p<sub>i</sub>

7) https://en.wikipedia.org/wiki/Toki_Pona  
Way less less. The entropy is always less (or equal) than the logarithm of the alphabet size.

 

[Estimated Entropy of English](https://arxiv.org/pdf/0911.2284.pdf)

------

P(raining | Yes,Yes,Yes) = Prior(raining) * P(Yes,Yes,Yes | raining) / P(Yes, Yes, Yes)

P(Yes,Yes,Yes) = P(raining) * P(Yes,Yes,Yes | raining) + P(not-raining) * P(Yes,Yes,Yes | not-raining)   
= (0.25*(2/3)^3) + (0.75*(1/3)^3 )
= (0.25*(8/27)) + (0.75*(1/27))  

P(raining | Yes,Yes,Yes) = 0.25*(8/27) / ( 0.25*8/27 + 0.75*1/27 ) = 8 / ( 8 + 3 ) = 8/11

Bonus points if you notice that you don't need a calculator since all the 27's cancel out and you can multiply top and bottom by 4:

But honestly, you're going to Seattle, so the answer should always be: "YES, I'm bringing an umbrella!"
(yeah yeah, unless your friends mess with you ALL the time ;)

[Source](https://www.glassdoor.com/Interview/You-re-about-to-get-on-a-plane-to-Seattle-You-want-to-know-if-you-should-bring-an-umbrella-You-call-3-random-friends-of-y-QTN_519262.htm)
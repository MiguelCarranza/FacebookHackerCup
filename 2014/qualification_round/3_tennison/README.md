# Tennison
You may be familiar with the works of Alfred Lord Tennyson, the famous English poet. In this problem we will concern ourselves with Tennison, the less famous English tennis player. As you know, tennis is not so much a game of skill as a game of luck and weather patterns. The goal of tennis is to win K sets before the other player. However, the chance of winning a set is largely dependent on whether or not there is weather.

Tennison plays best when it's sunny, but sometimes of course, it rains. Tennison wins a set with probability ps when it's sunny, and with probability pr when it's raining. The chance that there will be sun for the first set is pi. Luckily for Tennison, whenever he wins a set, the probability that there will be sun increases by pu with probability pw. Unfortunately, when Tennison loses a set, the probability of sun decreases by pd with probability pl. What is the chance that Tennison will be successful in his match?

Rain and sun are the only weather conditions, so P(rain) = 1 - P(sun) at all times. Also, probabilities always stay in the range [0, 1]. If P(sun) would ever be less than 0, it is instead 0. If it would ever be greater than 1, it is instead 1.

## Input
Input begins with an integer T, the number of tennis matches that Tennison plays. For each match, there is a line containing an integer K, followed by the probabilities ps, pr, pi, pu, pw, pd, pl in that order. All of these values are given with exactly three places after the decimal point.

## Output
For each match, output "Case #i: " followed by the probability that Tennison wins the match, rounded to 6 decimal places (quotes for clarity only). It is guaranteed that the output is unaffected by deviations as large as 10-8.

## Constraints
1 ≤ T ≤ 100
1 ≤ K ≤ 100
0 ≤ ps, pr, pi, pu, pw, pd, pl ≤ 1
ps > pr
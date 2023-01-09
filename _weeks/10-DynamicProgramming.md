---
title: "Week 9: Dynamic Programming"
date: 2019-03-14 12:00:00
---

**Week of {{ page.date | date: "%-m/%-d" }}**

# Mandatory videos 

## Tuesday

### Solving edit distance with Dynamic Programming:

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/811482/sp/81148200/embedIframeJs/uiconf_id/27551951/partner_id/811482?iframeembed=true&playerId=kaltura_player&entry_id=1_wh122oiu&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_uuiuh7g6" width="640" height="396" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>

## Thursday

No videos, we'll just be doing more practice with dynamic programming

# Additional Resources

Dynamic programming is one of the most challenging topics we'll be covering this semester, so here are some additional notes and resources I have assembled.

## General notes

- If you're having trouble with dyanmic programming, start by trying to figure out if the part you're struggling with is formulating a problem recursively, vs. converting a recursive solution into dynamic programming. This will help you better focus you efforts.
- Yes "Dynamic Programming" is a horrible name for this algorithm, in that it doesn't actually describe anything about how it works or what it does. The people who originally came up with it literally just chose this name because it sounded cool.
- A closely related technique, called memoization, works by just storing the results of every call to a function. For example, you might make a dictionary where the keys were arguments to the function and the values where the results of calling the function with those arguments. Every time you went to call the function, you would first see if the set of arguments you were going to call it with were in the dictionary. If they were, you wouldn't call the function and would just use the value from the dictionary. If they weren't there, you would call the function and store the result in the dictionary so you could use it next time.
- Dynamic programming is basically just memoization with better planning. Instead of needing to check whether a given set of arguments is in the dictionary, you would figure out an order in which you could call the function with different arguments to guarantee that any time you would need to make a recursive call, you can instead just look up the value you would have gotten by making that function call. In DP we store the results in a table rather than a dictionary, because due to our planning ahead we know exactly how many they'll be and can figure out a system for storing them logically in the table. Usually, each dimension of the table (e.g. rows, columns, etc.) ends up representing a different argument the function. 

## Steps in DP

1) Figure out how to write a recursive solution to your problem.

  - 1.1. Figure out how to break your problem down into smaller sub-problems
  - 1.2. Figure out your base case (how do you know when you've found the smallest possible subproblem, and what is the answer to it?)
  - 1.3. Figure out your recursion step (what do you have to do to a solution to a smaller version of this problem to make it be a solution to a bigger version of it?)
  - 1.4. Write the code

2) Figure out which values you would need to call your recursive solution on in order to build your way up to an answer to the whole thing. For example, if the input to your function is a number, one likely scenario is that you need to call your recursive function on all numbers between that value and 0 in order to have all of the building blocks you need to solve it for the number you actually care about. If the input is 2 numbers, you might need to solve it for all combinations of values less than each of those numbers. If the input is a sequence, you might need to solve it for sub-sequences of that sequence.

  - 2.1. Make sure there aren't too many of them (this will define the memory complexity of our solution; we generally say there are too many if the memory complexity is exponential (e.g. O(2^n)).
  - 2.2. Since each of these calls probably build on each other, figure out what order you need to know the numbers in so that you always have all the numbers you need by the time you need them.

3) Convert your recursive solution into a dynamic programming solution.

  - 3.1 Replace your base case with building a table and putting whatever value you would have returned for your base case into the position in the table that corresponds to the arguments that trigger your base case. For example, if your base case is that when your input value equals 0 you return the value 10, you would put 10 into the 0th position of DP table.
  - 3.2. Put most of the body of your function inside a loop (sometimes multiple nested loops) that goes through all of the arguments you would have recursively called the function on, in the order that you determined in step 2. If you've got multiple arguments, you probably need a loop for each one.
  - 3.3. Replace any calls to your recursive function with lookups in your DP table. The position in the table that you'll want to look up will be the ones that correspond to the arguments you would have called the recursive function with (usually smaller versions of your loop variables - e.g `i-1`).
  - 3.4. Replace any return statements with storing the value you would have returned in your DP table. Store it in the position corresponding to the arguments you're currently working with (usually the current values of your loop variables)
  - 3.5. Add a final step at the end where you return the value in the spot in your table that corresponds to the actual answer you care about.

## Resources:

### Videos by other people

#### Introductory
- [Introduction to DP using Fibonacci sequence](https://www.youtube.com/watch?v=vYquumk4nWw)
- [Intro using DP and Path finding in a grid](https://www.youtube.com/watch?v=P8Xa2BitN3I)
- [5 steps to solving Dynamic Programming problem](https://www.youtube.com/watch?v=aPQY__2H3tE)

#### Worked examples
- There are some in the course recordings videos for the days we discussed dynamic programming
- [Finding numbers that add up to 16](https://www.youtube.com/watch?v=nqlNzOcnCfs)
- [Maximum sum of a rectangle in a matrix](https://youtu.be/-FgseNO-6Gk?t=67)
- [Egg drop problem](https://youtu.be/iOaRjDT0vjc) ([other students have also recoomended this written guide to the egg drop problem]( https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/)
- [Largest square of ones](https://www.youtube.com/watch?v=FO7VXDfS8Gk)


#### Advanced
- [Principle of optimality](https://www.youtube.com/watch?v=_zE5z-KZGRw) (deeper dive into the theory behind figuring out when you can use DP)

### Written resources

- [Intro to Dynamic Programming](http://20bits.com/article/introduction-to-dynamic-programming)
- [Intro with examples in Python](https://towardsdatascience.com/beginners-guide-to-dynamic-programming-8eff07195667)

### Interactive/animations

- [Animation of Dynamic Programming](http://www.algoanim.ide.sk/index.php?page=showanim&id=49)
- [Example we used in class](https://devosoft.github.io/dynamic-word/dynamic-word)
- [Visualization of DP](https://easyhard.github.io/dpv/)

### Practice problems

- [Minimum number of deletions to convert string to palindrome](https://www.techiedelight.com/find-minimum-number-deletions-convert-string-into-palindrome/) (has a recursive solution if you just want to practice converting from recursive to DP)
- [IDeserve](https://www.ideserve.co.in/#dynamicProgramming/) (also has nice visualizations and explanations of solutions)
- [HackerRank practice problems](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=dynamic-programming) (might require you to make an account)
- [LeetCode practice problems](https://leetcode.com/problemset/all/?search=dynamic%20programming)

# In class: 

Review homework #3, example problems

# Out: 

Lecture review assignment #8

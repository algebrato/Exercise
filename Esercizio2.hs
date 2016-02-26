factorial a | a <=1 = 1
	    | otherwise = a * factorial (a-1)
factorial_bis a | a <= 1 = 1
		| otherwise = a * factorial_bis (a-1) 


main = print $ factorial_bis 4 




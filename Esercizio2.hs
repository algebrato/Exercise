factorial a | a <=1 = 1
	    | otherwise = a * factorial (a-1)

main = print $ factorial 4

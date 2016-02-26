fatt<-function(n)
{
	if(n<=1){return(1)}
	return(n*fatt(n-1))
}
write(fatt(4),stdout())


fattt= function(a)
	if a <= 1 then return 1
	end
	return a*fattt(a-1)
end

print(fattt(4))



quadrato = {x,y}
quadrato.new= function(self,x,y)
	q={}
	q.x=x
	q.y=y
	setmetatable(q, { 
		__tostring = function () return "x: " .. x .. ", y: " .. y end,
	})
	q.area = function(self) return self.x * self.y end
	return q
end

io.write("primo lato:")
a=io.read()
io.write("\nsecondo lato:")
b=io.read()


l = quadrato:new(a,b);

print(l:area())



putrandom = function(a)
	bit.rshift(a,10)
	bit.cast(a)
	return a
end





a=10

for i=0,10,1 do
	putrandom(a)
	print(a)
end
		









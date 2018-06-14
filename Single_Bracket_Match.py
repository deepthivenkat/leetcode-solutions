def bracket_match(text):
  stack,count = 0,0
  for symbol in text:
    if symbol == "(":
      stack+=1
    else:
      if stack: 
        stack-=1
      else:
        count+=1
  if stack<0:
    return -1*stack+count
  elif stack>0:
    return stack+count
  return count
        
test_ip = ["())(", ")))(())",")))","(("]      
print [bracket_match(ip) for ip in test_ip]
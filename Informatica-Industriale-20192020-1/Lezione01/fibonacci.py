def fibonacci(num):
  if(num == 0):
    return 1
  if(num == 1):
    return 1
  return fibonacci(num-1) + fibonacci(num-2)
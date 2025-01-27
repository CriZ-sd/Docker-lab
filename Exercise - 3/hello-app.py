import time 

t_start = time.time()
print('hello ..')
k=0
while k<1000:
  k=k+1
  end_t = time.time()
  if (end_t-t_start)%10 == 0:
    print(f'passed time : {end_t-t_start}')


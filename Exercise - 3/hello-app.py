import time 

t_start = time.time()
print('hello ..')
while True:
  end_t = time.time()
  if (end_t-s_start)%10 == 0:
    print(f'passe time : {end_t-s_time}')


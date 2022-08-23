import logging
import time


#logging.basicConfig(level=logging.DEBUG, filename='iteration.log', format='%(name)s-%(levelname)s-%(message)s')
logging.basicConfig(level=logging.DEBUG, filename='iteration.log', format='%(asctime)s - %(levelname)s - %(message)s')

result = 0

for i in range(1000):
    time.sleep(0.05)
    logging.info(f'current number is {i}')
    result *= i

logging.warning('running finish, but no actions next')


    

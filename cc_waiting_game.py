"""
waiting game
can you wait for a given number of seconds?
"""

import random
import time
from pynput.keyboard import Key, Listener



class waiting_game:
    def __init__(self):
        self.started = False
        self.stopped = False
        self.stop_listening = False


    def on_press(self, key):
        if not self.started and key == Key.enter:
            self.started = True
            self.start_time = time.time()
            print('started\n Press Enter To Stop')
        elif self.started and not self.stopped and key == key.enter:
            print('stopped')
            self.stop_time = time.time()
            self.started = False
            self.stop_listening = True
        
        if self.stop_listening:
            return False

    def get_time_elapsed(self):
        time_elapsed = self.stop_time - self.start_time
        return time_elapsed 
    

    
if __name__ == '__main__':
    # testing waiting game
    waiting_time = random.randint(1,10) 
    print(f'Wait for {waiting_time} seconds, Press Enter to Start')
    game = waiting_game()

    with Listener(on_press = game.on_press) as listener:   
        listener.join()
    
    print(f'you waited for {game.get_time_elapsed()} seconds')

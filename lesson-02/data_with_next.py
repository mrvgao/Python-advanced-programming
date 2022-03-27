
class Data:
    def __init__(self, initialized):
        self.index = 0
        
        for i in initialized: 
            self.update_db(i)
            self.index += 1

    def update_db(self, e):
        print('connect db and update {} with index'.format(e))
    
    def retrieval_db(self, i):
        print("based on {} get data from db".format(i))

    def __next__(self):
        for i in range(self.index):
            yield retrieval_db(i)
        




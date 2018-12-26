class QueueDeal(object):
    """docstring for QueueDeal"""
    def __init__(self, queue):
        self.queue = queue
        self.set_tqueue()

    def set_tqueue(self):
        if not self.queue:
            self.queue = [[],[]]
            return
        self.queue = self.queue.split('|')
        self.queue = [      q.split(',') if q else []    for q in self.queue]

    def queue2str(self):
        queue = self.queue
        queue = [ ','.join(q) if q else '' for q in queue ]
        if queue and len(queue) == 2:
            return '|'.join(queue)
        return '|'

print(1)
queue = '123,14|123,566'
queue = QueueDeal(queue)
print(queue.queue)
print(queue.queue2str())

print(2)
queue = '|123,566'
queue = QueueDeal(queue)
print(queue.queue)
print(queue.queue2str())

print(3)
queue = '123,14|'
queue = QueueDeal(queue)
print(queue.queue)
print(queue.queue2str())

print(4)
queue = '123,14'
queue = QueueDeal(queue)
print(queue.queue)
print(queue.queue2str())

print(5)
queue = ''
queue = QueueDeal(queue)
print(queue.queue)
print(queue.queue2str())

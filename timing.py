import time
import types

def timing(iterable, every_n=None, every_fraction=None):
    """Wraps your iterables to give you automatic timing!
    
    Want to time this loop?
    
      for i in arr:
        # do things
    
    Just write, instead:
    
      for i in timing(arr):
        # do things
        
    Et voilà! Your loop is timed!
    
    Args:
      iterable: the thing you're iterating over
      every_n: an integer saying after how many elements N you'd like to get timing information
      every_fraction: a float (0 <= x <= 1) saying at what fraction progress through the iterable you'd like timing information. Note: if this argument is specified, the iterable must support the len() operation.
    """
    
    if every_fraction != None and isinstance(iterable, types.GeneratorType):
        raise ValueError("Generators and every_fraction timing reports are not possible.")
    
    start_time = time.time()
    times = []
    
    for i, item in enumerate(iterable):
        start_iter_time = time.time()
        
        # The magic line: using a generator lets us run this loop in parallel to the timed loop
        yield item
        
        # Execution returns to this loop when the next element is asked for (i.e. when the timed 
        # loop finishes the iteration)
        end_iter_time = time.time()
        total_iter_time = end_iter_time - start_iter_time
        times.append(total_iter_time)
        
        # Print according to arguments
        do_print = False
        if every_fraction != None and i % int(len(iterable) * every_fraction) == 0:
            do_print = True
        if every_n != None and i % every_n == 0:
            do_print = True
        if every_n == None and every_fraction == None:
            do_print = True
            
        if do_print:
            print("Iteration {0} took {1:.4f}s".format(i, total_iter_time))
        
    end_time = time.time()
    
    # Print out statistics
    total_time = end_time - start_time
    print("Total runtime: {0:.4f}s".format(total_time))
    avg_time = sum(times) / len(times)
    print("Average runtime per loop: {0:.4f}s".format(avg_time))
    min_time = min(times)
    print("Shortest loop: {0:.4f}s".format(min_time))
    max_time = max(times)
    print("Longest loop: {0:.4f}s".format(max_time))
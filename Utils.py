import timeit
import statistics

# CONSTANTS
MILLISECONDS = 1e+3


def execution_time(stmt, ntimes):
    """ Return the execution time (in seconds) of the specified statement with ntimes runs. """
    t = timeit.Timer(stmt=stmt, globals=globals())
    res = t.repeat(repeat=ntimes, number=1)
    return res

def execution_time_ms(stmt, ntimes):
    """ Return the execution time of the specified statement with ntimes runs. """
    res = execution_time(stmt, ntimes)
    res = list(map(lambda x : x * MILLISECONDS, res))
    print("Code  : " + stmt)
    print("Mean  : " + str(statistics.mean(res)))
    print("St    : " + str(statistics.stdev(res)))
    print("Median: " + str(statistics.median(res))
    return res


execution_time_ms("1+1", 1000)

memes = load_memes()
m = memes[0]
f = open(m.url, 'rb')
data = f.read()
f.close()

print(str(len(data)) + ' bytes.')
print(str(len(data)/1024) + ' kb.')

# print(str(len(memes)))
# unique_memes = set(memes)
# print(str(len(unique_memes)))
#memes.sort(key=lambda x : x.datetime)

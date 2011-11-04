from tempfile import mktemp
from time import sleep

logfile = mktemp()
print "tempfile is:",logfile

def log(w):
    f = open(logfile, 'a')
    f.write(w+"\n")
    f.close()
#make sure all tests in this file are dispatched to the same subprocess
def setup():
    log('setup')

def test_timeout():
    log('test_timeout')
    sleep(2)
    log('test_timeout_finished')

# check timeout will not prevent remaining tests dispatched to the same subprocess to continue to run
def test_pass():
    log('test_pass')

def teardown():
    log('teardown')

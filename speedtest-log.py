import datetime
import re
import subprocess

p = subprocess.Popen(['speedtest-cli'], stdout=subprocess.PIPE, 
                                        stderr=subprocess.PIPE)
out, err = p.communicate()

p0down = re.search('Download: ', out).end(0)
p1down = re.search('\n', out[p0down:]).end(0)
p0up = re.search('Upload: ', out).end(0)
p1up = re.search('\n', out[p0up:]).end(0)

ds = out[p0down:p0down+p1down-1]
us = out[p0up:p0up+p1up-1]
#print('download speed..: ' + ds)
#print('upload speed....: ' + us)

log = str(datetime.datetime.now())
log = log + str(ds.split())
log = log + str(us.split())

print log

opened_file = open('speedtest.log', 'a')
opened_file.write("%r\n" %log)
opened_file.close()

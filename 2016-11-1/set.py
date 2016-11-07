s = set(['A','B','C'])
print s
s = set(['A','B','C','C'])
print s
print len(s)
s = set(['Adam','Lisa','Bart','Paul'])
print s
print 'Bill' in s
print  'bart' in s
s = set(['Adam','Lisa','Bart','Paul','adam','bart'])
print 'adam' in s
print  'bart' in s



months = set(['Jan','Feb','Mar','Apil','May','Jun','Jul','Aug','Sem','Oct','Dec','Nov'])
x1 = 'Feb'
x2 = 'Sun'
if x1 in months:
    print 'x1:ok'
else:
    print 'x1:error'

if x2 in months:
    print 'x2:ok'
else:
    print 'x2:error'

s = set(['Adam','Lisa','Bart','Paul'])
for name in s:
    print name


s= [('Adam',95),('Lisa',85),('Bart',59)]
for x in s:
    print x[0] + ':' + str(x[1])


s = set([1,2,3])
s.add(3)
print s
s.add(4)
print s
s.remove(4)
print s


s = set(['Adam','Lisa','Paul'])
L = ['Adam','Lisa','Bart','Paul']
s.add('Bart')
print s
s.remove('Adam')
print s
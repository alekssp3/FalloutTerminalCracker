class Fallout:
  def __init__(self, *params):
	self.passwords = []
	if len(params) > 0:
	  self.passwords = params[0]
	else:
	  self.set()
	self.get()

  def set(self):
	pwd = ' '
	lastLen = 0
	while pwd != '':
	  pwd = raw_input('> ')
	  if lastLen != 0 and len(pwd) != lastLen:
		return
	  lastLen = len(pwd)
	  self.passwords.append(pwd)
	else:
	  return

  def compare(self, str1, str2):
	count = 0
	for i in range(len(str1)):
	  if str1[i] == str2[i]:
		count += 1
	return count

  def analize(self, what=''):
	if what == '':
	  what = self.passwords
	l = len(what)
	for i in range(l):
	  print ('%s' % (what[i]))
	  for j in range(l):
		if i == j:
		  continue
		c = self.compare(what[i], what[j])
		#groupsum += c
		print (' %s %d' % (what[j], c))

  def get(self):
	for i in self.passwords:
	  print('%s' % (i.upper()))

  def solve(self, string=''):
	if string == '':
	  string = raw_input('? ')
	string = string.split(' ')
	others = []
	if len(string) != 2:
	  print('Bad string!')
	  return
	else:
	  if string[0] not in self.passwords:
		print('Not word!')
		self.get()
		return
	  for i in self.passwords:
		if string[0] == i:
		  if int(string[1]) == 0:
			self.passwords.remove(i)
		c = self.compare(string[0], i)
		if c == int(string[1]):
		  others.append(i)
		  self.passwords = others
	  self.analize()

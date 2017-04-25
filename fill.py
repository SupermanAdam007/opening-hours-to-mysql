
def getsql(h, addedDays):
	id = h[0]
	d = int(h[1])
	dleft = 7 - d
	tod = h[2]
	tdo = h[3]
	sqlcomm = ''
	for i in range(1 + addedDays, d + 1 + addedDays):
		sqlcomm += 'INSERT INTO openinghours(id_printer, day, od, do) VALUES ('
		sqlcomm += '\'' + id + '\','
		sqlcomm += '\'' + str(i) + '\','
		sqlcomm += '\'' + tod + '00\','
		sqlcomm += '\'' + tdo + '00\''
		sqlcomm += ');\n'
	print(sqlcomm)
	
	return ''


lastPrinter = 0
lastDay = 0
with open('hours.txt', 'r') as f:
	for line in f:
		if len(line) < 13:
			continue
		h = str.split(str.replace(line, '\n', ''), '-')
		addedDays = 0
		if lastPrinter == int(h[0]):
			addedDays = lastDay
			lastDay += int(h[1])
		else:
			lastDay = int(h[1])
		sql = getsql(h, addedDays)
		lastPrinter = int(h[0])



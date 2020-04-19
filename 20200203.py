txt = ''' 人生得意须尽欢，莫使金樽空对月。 天生我材必有用，千金散尽还复来。 ''' 
linewidth = 20 # 预定的输出宽度 
def lineSplit(line):
    plist = [',', '!', '?', '，', '。', '！', '？'] 
    for p in plist: 
        line = line.replace(p, 'a')
    return line.split('a') 
def linePrint(line):
    global linewidth 
    print(line.center(linewidth))
newlines = lineSplit(txt) 
for newline in newlines: 
    linePrint(newline)

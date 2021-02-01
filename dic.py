stre="hi hello hows . it going . hi well going good "
dic={key: stre.count(key) for key in stre.split()}
print(dic)
key="hi"
msg= 'present' if key in dic else 'notThere'
print(msg,dic[key])
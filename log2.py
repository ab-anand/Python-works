
a = open('ggevent.log','r')
text = a.read()
text_as_list = text.split('\n')


#print(len(text_as_list))
format = ', '.join(text_as_list)
format ='[' +format[:len(format)-1]+']'
file = open('log_to_json.json','w')
file.write(format)

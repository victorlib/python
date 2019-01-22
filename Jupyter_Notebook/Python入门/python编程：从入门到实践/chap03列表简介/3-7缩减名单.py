names = ['wang wu', 'anjaxs', 'zhao liu', 'zhang san', 'li si', 'lao tie']
print(names)
print('现在只能邀请两位嘉宾')
while(len(names) > 2) :
    name = names.pop()
    print('很抱歉,'+name+', 无法让你参加改成宴会。')
print(names)
del names[1]
del names[0]
print(names)


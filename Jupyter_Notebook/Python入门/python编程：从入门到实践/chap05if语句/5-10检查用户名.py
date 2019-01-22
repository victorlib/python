current_users = ['anjaxs', 'chen', 'jia', 'admin', 'programmer']
new_users = ['Chen', 'JIA', 'sheng', 'jack']
for user in new_users:
    if user.lower() not in current_users:
        print(user + ' can be use.')
    else:
        print(user + ' have been occupied')
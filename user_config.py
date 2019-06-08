import shelve

# This stores the information about the user
def _send_(user_info):
  data_ap = []
  data = [user_info]
  data_ap.append(data)
  file_ = shelve.open('mydata.dat')
  file_['data'] = data_ap
  file_.close()

  # This prints the information about the user
  user_ = input('Type [Y] to open: ')
  if user_ == 'Y' or user_ == 'y':
    file_ = shelve.open('mydata.dat')
    data_ap = file_['data']
    for item in data_ap:
      print('\n' + '--' * 10)
      print(item)
      print('--' * 10)
    file_.close()

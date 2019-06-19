import shelve

GIT_LINK = {'GIT_LINK': 'https://github.com/ARACADERISE/_Tool-Console_'}
TOOL_TYPE = {'type':'Termux'}
AUTHOR = {'author':'ARACADE_RISE'}
VERSION = {'version':'1.0.1'}
START_DATE = {'start_date':'June 4th, 2019, 7pm'}
RELEASE_DATE = {'release_data': None}

def project_info():
  CONVERT = str({'info': [[GIT_LINK], [TOOL_TYPE], [AUTHOR], [VERSION], [START_DATE], [RELEASE_DATE]]})
  return str(CONVERT)



# DATABASE

def DATABASE(port, port_info):
  try:
    info = ['DATABASE', ['relationship_between_db_and_port']]
    status = {'port': port, 'info': port_info, 'project_info': project_info()}

    str(info.append(status))

    _DB_ = shelve.open('DATABASE')
    _DB_['u-file'] = str(info)
    _DB_[''] = str({'db_uses': port, 'db_connects_to': port, 'port_used_by': ['DATABASE'], 'db_type': 'server_db'})

    _DB_.close()

  except:
    print('failed')

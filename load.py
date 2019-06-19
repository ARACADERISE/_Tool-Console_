def load(file_, _info_):

  # Storing data that is loaded in a list
  _loaded_data = [['DATABASE'], ['LOAD_FILES']]

  return "Loading", file_ + ".."
  _loaded_data.append(_info_)
  return "Information Recieved ", _loaded_data

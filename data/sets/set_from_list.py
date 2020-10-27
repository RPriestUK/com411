def observed():
  # define empty set
  Observations = set()
  # loop for 7 input requests
  for count in range(7):
    # Ask user for objects they have observed and add to set
    print("Please enter an observation:")
    Observations.add(input())
  return Observations

def run():
  print("Counting observations...")
  # assign to local set 'seen'
  seen = observed()
  # count number of each instance entered
  for seen_obj in range(0, len(seen), 1):
    print(seen_obj)

run()

from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
#landmark_string joins all of the landmarks together, each with its corresponding letter of the alphabet form landmarkchoices on a new line.
landmark_string=""
stations_under_construction = ['Richmond-Brighouse']
for letter, landmark in landmark_choices.items():
  landmark_string+= "{0} - {1}\n".format(letter,landmark)

def greet():
  #There is no input and return for this function.
  #It only prints welcome message and landmark_string.
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  #This function contains our full program.
  greet()
  new_route()
  goodbye()


def get_start():
  #This function is one of the helper function of the set_start_and_end() function.
  #This function asks about the start point. This letter should be from the landmark_choices. If it is not in this dictionary, then this function will give a feedback and call itself again. So, this function starts over.
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_start()

def get_end():
  #This function is one of the helper function of the set_start_and_end() function.
  #This function asks about the end point. This letter should be from the landmark_choices. If it is not in this dictionary, then this function will give a feedback and call itself again. So, this function starts over.
  end_point_letter = input("Ok, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point

  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    get_end()


def set_start_and_end(start_point, end_point):
  #This function is setter of start and end point.
  #It has two helper function which are get_start() and get_end()
  #If the given start_point is different from None, it asks for us to change the desired parameters which are origin, destination or both.
  if start_point is not None:
    change_point=input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      end_point = get_end()
    else:
      #If the input is given as wrong, the function will be called again. So, it will ask the same question again!
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point,end_point)

  else:
    #If the start point is given as None, then both start_point and end_point will be asked to the user.
    start_point=get_start()
    end_point=get_end()

  return start_point,end_point

def show_landmarks():
  #When the user asks the system again and again for new route, maybe user wants to see again the whole landmarks. This is the explanation of the existance of this function.
  see_landmarks=input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == 'y':
    print(landmark_string)


def new_route(start_point = None, end_point = None):
  #Firstly, it calls the setter function of start and end point. So, user can easily use this program.
  start_point, end_point = set_start_and_end(start_point, end_point)
  #By using get_route function, shortest path between the two point is founded.
  shortest_route = get_route(start_point, end_point)
  #return type of get_route is not user friendly. Visualization of route is slightly changed. 
  if shortest_route is not None:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  
  #If the user wants to see another route, this is for it.
  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    #also, program will asks if landmarks are needed.
    show_landmarks()
    new_route(start_point, end_point)


def get_route(start_point, end_point):
  #There can be more than one start_stations.
  #Because input is given as local point. and this local point can be close to two or more metro stations. So, we need to consider this situation. For this purpose, we use start_stations and end_stations. Then, we found different routes for these different stations by using loop.
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      #If there is any metro in construction, the metro graph should be equal to return value of the function of get_active_stations. But, if the stations_under_construction list is empty. Then, there is no change needed.
      metro_system = get_active_stations() if stations_under_construction else vc_metro

      if len(stations_under_construction)>0:
        #If there is a metro that is under construction, we need to check that is there any suitable path by using DFS algorithm.
        #If there is not any appropriate path, function will return None.
        possible_route = dfs(metro_system, start_station, end_station)
        if not possible_route:
          return None
        
      route = bfs(metro_system, start_station, end_station)
      if route is not None:
        routes.append(route)
    #After the loop , we get the all routes. But, user needs to the shortest path. By using min function, we can get easily the shortest path.
    shortest_route = min(routes, key=len)
    return shortest_route

def goodbye():
  print("Thanks for using SkyRoute!")

def get_active_stations():
  #Some metro's sometimes can not be used because of construction. Metros which are in construction is given in stations_under_construction list. So, we need to create a new appropriate metro graph.
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_station in vc_metro.items():
      if current_station != station_under_construction:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        #If this station is under construction, there shouldn't be any valid way.
        updated_metro[current_station] = set([])
    return updated_metro


skyroute()
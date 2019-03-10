from sense_hat import SenseHat
import urllib.request, json
import time

sense = SenseHat()

#comment to append to file
start = {'likes':[]}
with open('data.json', 'w') as f:
            json.dump(start, f)



#tinder functie
run = True
while run:
    #get data from randomuser.me API
    with urllib.request.urlopen("https://randomuser.me/api/") as url:
        data = json.loads(url.read().decode())
        name = data['results'][0]['name']

    #show message on LED matrix 
    sense.show_message(name['first'] )#+' '+ name['last'])
    #like
    event = sense.stick.wait_for_event()
    if event.direction == 'left' and event.action == 'pressed':
        print('Like')
        with open('data.json') as f:
            data2 = json.load(f)

        data2["likes"].append(name)

        with open('data.json', 'w') as f:
            json.dump(data2, f)

    #dislike
    if event.direction == 'right' and event.action == 'pressed':
        print('dislike')

            
    #SHUTDOWN
    if event.direction == 'down' and event.action == 'pressed':
        print('stop')
        sense.clear()
        run = False

    #wait for stick release
    sense.stick.wait_for_event()
        
    

You need to change googlemap API key with a new one to work the app, the current key is expired 
# RoadSense : Specially Designed for kerala roads
>>Vidya academy of science and technology thrissur

Roadsense is an intelligent pothole detector which could help in obtaining the conditions of road ahead.
This could help drivers get a clear view of what is the quality of road ahead.The system uses Less human effort and it will guarantee safety and comfort to different road users.

  - Inteligent Alert
  - Advance route 
  - Real-time 
  
  Roadsense can also help officials monitor road condition in areas. As a result necessary actions can be taken by officials where quality of road is poor

# New Features in development!

  - Dashboard for the admin with heat  map of the road pothole
  - Improving predication accuracy
  - App for user with mapbox map service


Currently the system provide accuracy of *98%* 

### App developed for data collection
<img src="https://github.com/nikhilpsathyanathan/roadSense/blob/master/Screenshots/img1.jpg" width="50%" height="50%">

### Pothole mapped
<img src="https://github.com/nikhilpsathyanathan/roadSense/blob/master/Screenshots/img2.png" width="50%" height="50%">


### Tech

RoadSense uses a number of open source projects to work properly:

* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framewok
* [Flask] - The Python micro framework for building web applications
* [Andoid] - Android Open Source Project 

And of course RoadSense itself is open source  [roadSense]

### Installation

Install the dependencies  and start the server.

```sh
$ cd roadSense
$ pip3 install -r requirements.txt
$ python main.py

$ python -m http.server 8080 --bind 127.0.0.1  // for heat map only
```



### Development

Want to contribute? Great!



Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8080
```

### Todo

 - Admin panel
 - User android app
 - combine 2 apps and 
 - used json response as file in app, instead of getting live data from server(for testing purposes)
 ### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)




   [roadSense]: <https://github.com/nikhilpsathyanathan/roadSense>
   [git-repo-url]: <https://github.com/nikhilpsathyanathan/roadSense.git>
   [node.js]: <http://nodejs.org>

By Nikhil

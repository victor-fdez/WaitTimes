# Wait Times

**We have started working on a project that we believe might be a commercial success among the border crossers of the United States, Mexico region.**

The idea, is to create a mobile application that can use the onboard sensors of a smartphone (gyroscope, GPS, accelerometer) to compile information about the position and movement of the car. This information will be sent to a server, where calculations will be done on the data. After the calculations are done, the server will respond with quasi real-time information of the state of traffic in the brdige border crossings.

**The information of the bridge border crossing will be:**

+ Estimated wait time for crossing in one particular direction.
+ Length of the queue.
+ Estimated position of the quickest lane for further optimization.
+ Historical information, visualized in graphs of previous years in the same day, this to make scheduling easier.

*As a target market myself, I have been in need of the information mentioned above. I make my decisions on going back to Mexico based on the line, it affects my life directly and I would appreciate a tool like this very much.*

###How we are going to do it

+ Set up a server that can make all the calculations necessary.
+ Develop and Android and iPhone app that can harness all the information from the onboard sensors at lowest battery consumption possible.

###Server

+ The user authenticates with the server after creating an account.
+ The server obtains coordinates and position information of the users, by receiving a file.
+ The server will utilize the position information to determine where in the map is the car
+ The server will use the information to also determine at what pace has the car been moving along the course of the bridge.
+ The server will use some data to determine the extent of the queue is with respect to the finishing line.
+ The server will send back to the application results of the calculations.
+ Estimated wait times.
+ Length of queue
+ The server will store the time information of all users but not their locations at that particular time to generate reports and historical time queue data.


# Senior Design Spring 2024 Lab Notebook
Group: Tyler Hirsch, Bryson Maedge, Nolan Opalski  
NetId: &nbsp;thirsch3, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bmaedge2, &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nolanfo2   
TA: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Angquan Yu

## Februrary 22nd, 2024 (Design Document Due Date)
We finalized our <a href="https://github.com/THirsch62/ECE-445/blob/main/Design%20Document.pdf">Design Document</a>, referencing the <a href="https://courses.engr.illinois.edu/ece445/documents/grading_rubrics/DD_evalsheet.pdf">evaluation sheet</a> to make sure that we met all the requirements.

## Februrary 21st, 2024
We met today to revise our Design Document and started CAD modeling. We determined how much 3D printing would cost us and also placed an Amazon order through ECE Illinois for all parts we need to start our initial testing.
<br><br>
Here is the start of what our panels will look like:
![Screenshot](readme_images/Panel.png)
The dimensions are 10"x10"x1".
<br><br>
Here is our purchase order:
![Screenshot](readme_images/purchase_order.png)

## February 20th, 2024
We finished a rough draft of our Design Document and reviewed it with our TA. We determined that our graphics should be more detailed and our verification steps should be more objective.

## February 19th 2024
We started a rough draft of our Design Document. We plan to work on it tonight and tomorrow. This way, we'll have a good outline before meeting with our TA so we can get any help if needed.

## February 18th 2024
Sent emails asking for discounts/sponsored free parts to:
- DFRobots (Servos)
- RaspberryPi (RaspberryPi4 and camera module)
- Siebel Center for Design (3-D printing)

## February 12th 2024
We discussed parts required for initial testing:
* Servos
* RaspberryPi 4
* Camera
* Frame to mount servos to
* Panel to attach to servos and test folding mechanism

We put together a shopping list with amazon links to stuff we need to purchase for testing so we can discuss purchasing procedure with our TA tomorrow. We also need to discuss the procedure for getting CAD models 3-D printed as our frame and panels will most likely be 3-D printed.

## February 9th 2024 (Team Contract Due Date)
We discussed guidelines, goals and expectations today. Following that discussion, we put together our <a href="https://github.com/THirsch62/ECE-445/blob/main/ECE445_Team_48_Contract.pdf">Team Contract</a> and submitted on Canvas.

## February 8th 2024 (Project Proposal Due Date)
We collaborated over discord to make revisions in accordance to feedback provided by our Ta.  
<a href="https://github.com/THirsch62/ECE-445/blob/main/Project%20Proposal.pdf">Project Proposal</a> was submitted by Nolan on Canvas.
<br><br>
Started <a href="https://github.com/THirsch62/ECE-445/tree/main/python_code">python code</a> for image recognition:
* Import dataset from MNIST
* Isolate and extract part of data we need (training images and labels for: tshirts, pullovers, trousers)
* Train CNN on extracted data (model predicts with 97.7% accuracy on test dataset)
* Save trained model to sdcard
* Load trained model into memory
* Function to accept image and output predicted classification

Miscellaneous code:
* Created general layout for future functions
* TODO: Function to normalize image from camera. Will consist of cropping image to just clothing item and resizing image to 28x28 pixels
* TODO: Set up basic servo control function. Input parameter will be int corresponding to panel to fold. Function will execute folding for that panel
* TODO: Figure out folding pattern/series of ints to pass to servo control function. Need 3 foloding patterns for all clothing types

## February 7th 2024 (First TA meeting)
We met with our TA (Angquan Yu) at 4pm. Recieved feedback on current status of our project Proposal.  
Feedback summary:  
* Needs to be more detailed
* Clarified that PCB will be part of servo subsystem in our physical system  

![Screenshot](readme_images/Block_Diagram.jpg)
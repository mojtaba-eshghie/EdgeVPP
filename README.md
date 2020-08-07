## An Edge Deployment Demo for Vector Packet Processing (VPP)

### Technologies used:
- Docker
- VPP's properiatory high-bandwidth memory interface


### Logical view of deployment
![VPP Deployment](https://raw.githubusercontent.com/mojtaba-eshghie/EdgeVPP/master/src/vpp-edge-deployment.PNG)

### Usage
You must have Docker installed. Besides, add the docker to sudoers on linux. Then, issue the following commands (note that during the setup any stopped or dangling docker image will be deleted):

    python3 startup.py

After successful running of the above command you can log into the router's CLI using following:

    docker exec -it router_a bash
    docker exec -it router_b bash

After attaching to the router_a/router_b containers, use the `vppctl` command to log in to the VPP CLI.
The routers can ping each others using the following command:

    ping da01::2


Feel free to open issues if you have any questions.
By @mojtaba-eshghie
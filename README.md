## Distributed pi calculation
### How to run
In the project directory run the command:

    python src\monte_carlo_pi_calculation.py

Ray will provide printed instructions to aid you in connecting multiple machines to your cluster! 
If you wish to create your cluster through the command line, the command which will achieve this is:
    
    ray start --head


The Flask frontend will be hosted at: 

    http://127.0.0.1:5000/ 

while the ray dashboard can be found at:
    
    http://127.0.0.1:8265/
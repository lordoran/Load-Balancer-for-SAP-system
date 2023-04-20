# Load Balancer for SAP systems

This code provides a load balancer for SAP systems. The load balancer ensures that the load is distributed evenly among the available SAP systems, preventing any one system from becoming overloaded.
Dependencies

## This code requires the following Python packages to be installed:

    requests
    json

### Usage

To use the load balancer, simply run the balance_load() function. This function will choose the SAP system with the lowest load and send a request to that system. If no SAP system is available (i.e. all systems are currently processing the maximum number of requests), the function will return None.

You can customize the list of SAP systems by modifying the sisteme variable in the code. Each system in the list should be a dictionary with the following keys:

    id_sistem: A unique identifier for the system
    base_url: The base URL of the system's API endpoint
    max_concurrent_requests: The maximum number of requests that the system can process concurrently
    current_requests: The current number of requests that the system is processing
    last_request_time: The timestamp of the last request that was sent to the system
    load_limit: The maximum load that the system can handle before becoming overloaded
    timeout: The maximum time (in seconds) that the load balancer will wait for a response from the system before timing out

### Example

Here's an example of how to use the load balancer:

'''python

import time
from load_balancer import balance_load

for i in range(10):
    response = balance_load()
    if response is not None:
        print(f"Request {i} succeeded with status code {response.status_code}")
    else:
        print("No SAP systems are currently available")
    time.sleep(1)

In this example, we call the balance_load() function 10 times, waiting 1 second between each call. If a system is available, the function will print the status code of the response. If no system is available, the function will print a message indicating that no SAP systems are currently available.
Credits


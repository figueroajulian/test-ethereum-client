<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/337518/184757509-5ac8a259-659a-42dd-a51c-cd093a41a0ad.png">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/337518/184757473-5d70ac41-4afd-42f6-ab7b-5338ae09b2fb.png">
    <img alt="Nethermind" src="https://user-images.githubusercontent.com/337518/184757473-5d70ac41-4afd-42f6-ab7b-5338ae09b2fb.png" height="64">
  </picture>
</p>

# Automation testing for Nethermind Eth client.

This projects serves as a demonstration of automation testing for the performance and the api of Sedge services using Nethermind as Ethereum client.

## Requirements to run the tests.
To run this project, one need:

* Python 3.x, Pytest. (Integration suite)
* Locust (Performance suite)

You can install all the needs running:

```
pip -q install -r requirements.txt
```

### To run the integration tests, execute the following command:
```
pytest --template=html1/index.html --report=./reports/integration_tests_report.html
```
### To run the performance tests:

#### Through the GUI
```

locust --config locust.conf

```

This starts a local web interface (http://localhost:8089) that allows you to configure the test. You can specify the number of users to simulate, the hatch rate, and the target host. Once you have configured the test, click the "Start swarming" button to begin.

`Hatch rate`: This refers to the rate at which new simulated users are spawned during the load test. For example, if you set a hatch rate of 10 users per second, Locust will add 10 new users to the test every second until the desired number of users is reached.

`Host`: This is the URL of the application or API that you want to test. You should enter the complete URL, including the protocol (HTTP or HTTPS) and the domain name or IP address.

`Number of users`: This refers to the total number of simulated users that will be used during the load test. This value should be adjusted based on your testing needs and the capabilities of your system.

#### Without GUI (headless mode)
```

locust -f test/performance/eth_block_load.py --headless -u (users) 100 -r (spawn-rate) 5 -t (run-time) 30

```

------------------------------------------------------------------------------------------------------------------------
## Performance results

#### Session v1
- time: ≈10'
- scope: spawn of five users per second till 1000 users.
- service involved: [eth-block-by-number](https://docs.nethermind.io/nethermind/ethereum-client/json-rpc/eth#eth_getblockbynumber)

Request Statistics:

The test was executed using the HTTP POST method on the "/" endpoint.
A total of 754,159 requests were made, and no failures were encountered, indicating a successful test execution.
The average response time for the requests was 576 milliseconds, with a minimum of 129 milliseconds and a maximum of 2599 milliseconds.
The average size of the responses was 5221 bytes.
The service handled an average of 1223.9 requests per second, demonstrating its ability to handle a significant workload effectively.

Response Time Statistics:

The response time statistics provide a distribution of response times for the tested service.
For the HTTP POST requests to the "/" endpoint, the response time percentiles indicate the time taken for a specific percentage of requests to be completed.
The 50th percentile (median) response time is 530 milliseconds, indicating that half of the requests were completed within this time frame.
The response time gradually increases as the percentile increases, with the 99th percentile indicating the response time experienced by only 1% of the requests.
The maximum response time recorded during the test was 2600 milliseconds, representing the longest duration observed.


```
Analysis
- Performance: The service demonstrated good overall performance, handling a large number of requests without any failures. The average response time of 576 milliseconds indicates a reasonably fast response.
- Scalability: The service achieved an average throughput of 1223.9 requests per second, suggesting its ability to scale and handle high levels of concurrent requests effectively.
- Response Time Distribution: The response time percentiles provide insights into the distribution of response times. The majority of requests completed within 1.2 seconds (95th percentile), while only a small percentage experienced longer response times.

In conclusion, the performance test results demonstrate that the tested service performs well under the given workload. The service handles a large number of requests with satisfactory response times and shows scalability potential. However, continuous monitoring and periodic performance evaluations can help identify and address any performance concerns that may arise as the service evolves
```

![image](https://github.com/figueroajulian/test-ethereum-client/assets/50703828/3dc84dfd-9cf6-4574-8fd6-736ae112c690)


#### Session v2
- time:  ≈10'
- scope: spawn of 500 users per second till 10000 users.
- service involved: [eth-block-by-number](https://docs.nethermind.io/nethermind/ethereum-client/json-rpc/eth#eth_getblockbynumber)

Request Statistics:

The test was executed using the HTTP POST method on the "/" endpoint.
A total of 422,631 requests were made, out of which 27,322 requests resulted in failures. The failure rate stands at 6.46% of the total requests.
The average response time for the successful requests was 17,151 milliseconds, with a minimum response time of 143 milliseconds and a maximum response time of 93,141 milliseconds.
The average size of the responses was 4,585 bytes.
The service handled an average of 522 requests per second, indicating its ability to process a moderate workload.

Response Time Statistics:

The response time statistics provide insights into the distribution of response times for the tested service.
For the HTTP POST requests to the "/" endpoint, the response time percentiles indicate the time taken for a specific percentage of requests to be completed.
The 50th percentile (median) response time is 22,000 milliseconds, meaning that half of the successful requests completed within this time frame.
The response time gradually increases as the percentile increases, with the 99th percentile indicating the response time experienced by only 1% of the requests.
The maximum response time recorded during the test was 93,000 milliseconds, representing the longest duration observed.

Failures Statistics:

The failures statistics provide information about the occurrences and types of failures encountered during the test.
In this case, all the failures were related to the "Failed to get block by number" error, and it occurred 27,322 times.


```
Analysis
- Performance: The test results indicate several areas for improvement in terms of performance. The average response time of 17,151 milliseconds is significantly higher than the previous test, suggesting potential performance bottlenecks under higher user loads.
- Failures: The occurrence of 27,322 failures, all related to the "Failed to get block by number" error, should be investigated and resolved to ensure the stability and reliability of the service.
- Scalability: The service showed limitations in handling the increased load of up to 10,000 users, as indicated by the higher failure rate and longer response times.
- Response Time Distribution: The response time percentiles provide insights into the distribution of response times. It is evident that a significant portion of requests experienced high response times, impacting the overall user experience.

Potential Improvements:

- Performance Optimization: Identifying and addressing performance bottlenecks to improve response times, such as optimizing database queries or optimizing resource utilization.
- Error Handling: Investigating and resolving the errors to reduce the number of failures and improve the stability of the service.
- Load Testing: Conducting further load testing with higher user loads, gradually increasing the load to identify the service's maximum capacity and any performance degradation points.
- Scalability Testing: Assessing the service's scalability by simulating a higher number of concurrent users to determine its ability to handle larger workloads.

In conclusion, the performance test results indicate the need for performance optimization and addressing the identified failures. The service experienced higher response times and failure rates under the increased load of up to 10,000 users. By implementing performance improvements and resolving the identified issues, the service can enhance its performance, reliability, and scalability, ensuring a better user experience.
```

![image](https://github.com/figueroajulian/test-ethereum-client/assets/50703828/35c217c3-c433-421d-8dec-4c2172ac740b)


### Comparission between session v1 and v2.

![total_requests_per_second_1687276687](https://github.com/figueroajulian/test-ethereum-client/assets/50703828/0f0754f5-4d9a-47b2-871d-784bd813db00)



## Documentation
* [LOCUST-DOCUMENTATION](https://locust.io/)
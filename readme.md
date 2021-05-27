# CS4740 Spring 2021 Repo
### All code authored by Brooks Eason
___
### What is CS4740?
CS4740 at UVA is a class focused broadly on cloud computing. We discussed its use cases, technologies, and specific applications.
This class exclusively used AWS as the cloud provider, so there will be AWS specific files like `lambda.py`, which is used by AWS Lambda (AWS' implementation of FaaS).
___
### Note Regarding Repo Architecture
Over the course of the semester we had 6 Programming Assignments, PA[1-6]. However, PA1 was just introduction to cloud computing, so there was nothing to push there.
___
### Note Regarding Hard-Coded IP Adresses
In many of the files in this repo, there may be lines of code like:
```python
""" Something like this or similar"""
sample_api_call = requests.get("http://1.222.333.444:5000/API/version/response", payload)
```
For our purposes, we did not need to set up a persistent endpoint for vm interaction in the cloud, so the hard coded IPs are calls to the vm's IP I was using at the time.


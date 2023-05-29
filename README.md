# lopt_api


## Getting started

To make it easy for you to get started with GitHub, here's a list of recommended next steps.

create a repository where you want to set this code and then go in this repo and then clone the code
```
mkdir new_repo
cd new_repo
git clone https://github.com/cosmo-gb/lopt_api.git
```

## Use this code

The code is in the repo src/. It is made of 3 scripts: api_post.py, find_solution.py and test_api.py.

### Build the API

With api_post.py, you can build the REST API exposing an endpoint /productionplan that accepts a POST
 of which the body contains a payload. To activate the API, you can use your favorite IDE and run api_post.py
or from the terminal inside src/ do
```
python api_post.py
```
This activates the API.

### Test the API

Then with test_api.py, you can post your data (payload) and obtain a result (response). 
You can run this script as previously. By default, it runs for the payload1 file, 
you can change this by changing f=1 line 35.
The url obtained when you run api_post.py needs to be set to the url in test_api.py (line 37)
By running test_api.py, you automatically save the results in a response_to_payload***.json file

### Compute the power

Finally the script find_solution computes the optimal power of each source



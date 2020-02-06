

let data = fetch ('https://secure.toronto.ca/webwizard/ws/requests.json?service_code=CSROSC-14&jurisdiction_id=toronto.ca')
    .then ((request) => request.json())
    .then ((data) => {return data});

console.log (data);
/s2019-10

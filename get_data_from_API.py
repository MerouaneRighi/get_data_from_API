import requests
data={"latitude":36.737232,
        "longitude":3.086472,
        "month":9,
        "year":2022,
        "annual":"false",
        "method":15,
        "shafaq":"general",

    }
params ={"page":2}
#req =requests.post(url="https://reqres.in/api/pages?2",data=data)
#req=requests.put(url="https://reqres.in/api/users/597",data=data)
#req =requests.get(url="https://reqres.in/api/users",params=params)
req = requests.get(url="http://api.aladhan.com/v1/calendar",params=data)
date =req.json()['data'][0]["timings"]
print(date)
for i in date:
    print("|___________________________|")
    print("|#{0}:|{1}|".format(i,date[i]))
    print("|___________________________|")
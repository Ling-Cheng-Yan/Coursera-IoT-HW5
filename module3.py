import http.client
conn = http.client.HTTPConnection("www.uci.edu")
conn.request("GET", "/")
r1 = conn.getresponse()
data = r1.read()
data = str(data)
data = list(data)

for i in range(len(data)):
    if i + 1 < len(data):
        if (data[i] + data[i+1] == "\\" + "n"):
            print(data[i].replace("\\", ""), data[i+1].replace("n", ""))
        else:
            print(data[i], end="")

conn.close()


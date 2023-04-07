/*
ISP - Internet service provider
Data can be transmitted between devices through routers

IP - Internet Protocol, a set of protocol programmed into the computers.
each computer has an unique IP address. Every piece of data sent from computers to another will contain the receiving and the return address.

TCP - Transmission Control Protocol, another set of protocol, computers adhere to.
80 - HTTP
443 - HTTPS
The interger is a port number, which TCP will always add to the address as such, IP address:port number, this distinguishes the type of data, ie. Email, Website, Video conference...
TCP and IP do transmissions by sending a piece of data in smaller packets, with each numbered.
When a router drops a piece of packet when it's busy(no memory left to store the data), the receiving end can request for that specific packet again from the return end.
The data packets sent between devices may traverse multiple routers, and can traverse in different route.

DNS - Domain Named System
A collection of servers that convert domain name into IP addresses and vice versa.
Inside of these servers contains sort of key-value pair (domain name : IP addresses), in data struct like hash tables...

URL (Uniform Resource Locator) is used to identify a resource on the web, HTTP requests sent to the server that hosts the resource will include the URL.

Server - a piece of software, which tends to run on big, expensive devices.
It's purpose receive requests and processes it, looking up the resource identified by the URL and returning it to the client in the form of an HTTP response.
*/

/*
HTTP(S) - Hyper Text Transfer Protocol (Secure)
https://www.example.com/file.htlm(path)
https://www.example.com/folder/file.html
www is called a host name, while example.com is called the fully qualified domain name.
the https at the beginning specifies the protocol the computer should use when accessing data from that website.
protocol:
GET /search?q=cat HTTP1.1
Host: www.google.com
...
POST
...

HTTP response:
HTTP/ 1.1(version of HTTP) 200 OK
Content-Type: text/html
Set-Cookie: session=value
...
Status code: 200 OK
301 Moved Permemnently
(when type-in addresses without www. for eg, the browser will receive this code together with the new address, and it will automatically redirect user to the url.)
404 Not Found
403 Forbidden
401 Unauthorised

When logged in as an user, the server can send a response to set a Cookie which is specific to a computer,
hence within the same session, everytime the user access private information(eg. each different emails), the GET request will send the cookie to the server:
GET /HTTP/1.1
HOST: gmail.com
Cookie: session=value
...
*/




// HTML - Hyper Text Markup Language
// CSS - Cascading Style Sheets
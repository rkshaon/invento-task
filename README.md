# INVENTO TASK

## Authentication
### Sign Up
End point: `BASE-URL/register` \
Method: `POST` \
Data body: `{
    "name": "Rezaul Karim Shaon",
    "email": "rkshaon.ist@gmail.com",
    "username": "rkshaon",
    "password": "rkshaon"
}`

### Sign In
End point: `BASE-URL/login` \
Method: `POST` \
Data body: `{
    "credential": "rkshaon.ist@gmail.com",
    "password": "rkshaon"
}`

### Sign Out
End point: `BASE-URL/login` \
Method: `POST`

## Short URL
### Create short URL
End point: `BASE-URL/create` \
Method: `POST` \
Data body: `{
    "url": "https://www.linkedin.com/in/rkshaon/",
    "expiry": "300",
    "custom": "chilp.it",
    "private": "true"
}` \
Note 1: `expiry is optional, custom url is optional, private is optional.` \
Note 2: **For using expiry feature and private link feature - log in is required!**

### Create short URL
End point: `BASE-URL/retrive` \
Method: `POST` \
Data body: `{
    "short_url": "http://chilp.it/403980e"
}`

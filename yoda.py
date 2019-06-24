import requests

response = requests.post("https://yodish.p.rapidapi.com/yoda.json?text=Master+Obiwan+has+lost+a+planet.",
  headers={
    "X-RapidAPI-Host": "yodish.p.rapidapi.com",
    "X-RapidAPI-Key": "3e9285d1a1msha8ca1b76cd28939p1900ccjsnb44fa5224005",
    "Content-Type": "application/x-www-form-urlencoded"
  }
)

print(response)
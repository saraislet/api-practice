# API Practice Exercise

This is a short exercise (~30-90 minutes) to practice and build confidence in building a basic server-side API app.

## Data

In `data.py` you'll find a dictionary of dictionaries, called `users`.

In `users`, the key is an ID (`int`), and the value is a `user` dictionary. Each `user` dictionary has keys `name` and `token`.

## Exercise

Write a Flask server with the following characteristics:
1. A `/users` route that returns the entire `users` dictionary in `json` format.
  1. *Bonus:* Allow `GET` requests to this route with the `user_id` parameter to return a dictionary for a single, specified user in `json` format.
1. A `/users/:id` route that returns a dictionary for a single, specified user in `json` format.
1. If a `user_id` is requested that is not in the data, the server should respond with a 404 error.
  1. *Bonus:* Build a custom 404 response using Flask.

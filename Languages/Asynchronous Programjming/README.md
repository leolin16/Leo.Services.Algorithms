# Asynchronous Processing

Delegating sub tasks to another actor(Thread/Device) without waiting for response,shen sub tasks finish, will call back to a function to handle the result

Best suited for IO intensive tasks like:

- Database reads/writes
- Web Servie calls
- Copying, downloading, uploading data

## typescript

https://github.com/johnpapa/typescript-async
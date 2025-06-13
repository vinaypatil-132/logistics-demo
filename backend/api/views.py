from django.http import JsonResponse

def trip_list(request):
    data = {
        "trips": [
            {"id": 1, "destination": "Bangalore", "driver": "Vinay"},
            {"id": 2, "destination": "Mumbai", "driver": "Ravi"}
        ]
    }
    return JsonResponse(data)


# def home(request):
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Logistics Demo</title>
#         <style>
#             body { font-family: Arial, sans-serif; padding: 20px; }
#             button { padding: 10px 20px; font-size: 16px; }
#             #result { margin-top: 20px; }
#         </style>
#     </head>
#     <body>
#         <h1>Welcome to the Logistics Demo Website!</h1>
#         <button onclick="fetchTrips()">Load Trips</button>
#         <div id="result"></div>

#         <script>
#             function fetchTrips() {
#                 fetch('/trips/')
#                 .then(response => response.json())
#                 .then(data => {
#                     let trips = data.trips.map(t => `<li>ID: ${t.id}, Destination: ${t.destination}, Driver: ${t.driver}</li>`).join('');
#                     document.getElementById('result').innerHTML = `<ul>${trips}</ul>`;
#                 })
#                 .catch(err => {
#                     document.getElementById('result').innerHTML = 'Error fetching trips!';
#                     console.error(err);
#                 });
#             }
#         </script>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_content)

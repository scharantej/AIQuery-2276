## Flask Application Design

### HTML Files

- **index.html**: This file will serve as the homepage of the application, containing the input fields and the submit button.

```html
<!-- index.html -->

<h1>Serial Number and Attachment Query</h1>

<form action="/query" method="post">
  <label for="serial_numbers">Serial Numbers:</label>
  <input type="text" id="serial_numbers" name="serial_numbers" required>

  <label for="attachment_names">Attachment Names:</label>
  <input type="text" id="attachment_names" name="attachment_names" required>

  <input type="submit" value="Query">
</form>
```

- **results.html**: This file will display the results of the query, including the AI response.

```html
<!-- results.html -->

<h1>Query Results</h1>

{% if query_result %}
  <p>{{ query_result }}</p>
{% else %}
  <p>No results found.</p>
{% endif %}
```

### Routes

- **query**: This route will handle the query request from the homepage. It will extract the serial numbers and attachment names from the request form, pass them to the AI, and display the response in the `results.html` file.

```python
@app.route("/query", methods=["POST"])
def query():
  serial_numbers = request.form.get("serial_numbers").split(",")
  attachment_names = request.form.get("attachment_names").split(",")

  # Pass serial numbers and attachment names to AI for processing...
  ai_response = query_ai(serial_numbers, attachment_names)

  return render_template("results.html", query_result=ai_response)
```

- **static**: This route will serve the static files, such as the CSS and JavaScript files needed for the Bootstrap frontend.

```python
@app.route("/static/<path:path>")
def static_files(path):
  return send_from_directory("static", path)
```
# Softcom Proof-of-Concept Task

A simple API that aggregates search results from the following APIs.

* [National Library of Medicine](http://collections.nlm.nih.gov/web_service.html)
* [arXiv](http://arxiv.org/help/api/index)

## API Usage
Make a call to the `/search` endpoint,

``https://castle-black.herokuapp.com/api/v1/search``

### Request Parameters
* `query` - term to search for

### Response
Every valid call to the API returns JSON, with properties,
* `query` - the string value passed to the API request
* `result` - a JSON Array containing the actual results of the API call. Each element in the array is a JSON object, with properties `url` and `title`.
    * `url` is the resource identifier of the document.
    * `title` is the title/name of the document.

### Example
``https://castle-black.herokuapp.com/api/v1/search/?query=artificial+neural+networks``


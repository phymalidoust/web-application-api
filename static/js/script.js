const form = document.querySelector('form');
// Add event listener for form submission
form.addEventListener('submit', (event) => {
	event.preventDefault(); // prevent the default form submission behavior
	
	const fileInput1 = document.querySelector('#json-file-1');
	const file1 = fileInput1.files[0]; // get the first selected file
	
	const fileInput2 = document.querySelector('#json-file-2');
	const file2 = fileInput2.files[0]; // get the second selected file
	
	const formData = new FormData();
	formData.append('json-file-1', file1); // add the first file to the form data
	formData.append('json-file-2', file2); // add the second file to the form data
	
	// Send POST request to /upload endpoint
	
	// const URL = '/http://localhost:8000/';
	const URL = '/upload';
	// const URL = '/http://127.0.0.1:5000';
	fetch(URL, {
		method: 'POST',
		body: formData
	})
	.then(response => response.json())
	.then(data => {
		// handle the response from the server
		console.log(data);
	})
	.catch(error => {
		console.error(error);
	});
});

function handleFormSubmit(event) {
  event.preventDefault();
  var form = event.target;
  var data = new FormData(form);
  $.ajax({
    url: form.action,
    method: form.method,
    data: data,
    processData: false,
    contentType: false,
    success: function(response) {
      console.log(response);
      alert(response.message);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.error(textStatus, errorThrown);
      alert('An error occurred while uploading the files. Please try again later.');
    }
  });
}
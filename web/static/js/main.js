
async function deleteImage(id) {
    const token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    
    const result = await fetch(`http://localhost:8000/home/${id}`, {
        method: "DELETE",
        headers: {
            'X-CSRFToken': token
        }
    });
    
    if(result.status === 204){
        location.reload();
    }
    
}

function togglePasswordInput(file_id='') {
    const uploadForm = document.getElementById('uploadForm');
    const passwordForm = document.getElementById("passwordForm");

    if(passwordForm.style.display === 'none'){
        passwordForm.style.display = 'block';
        uploadForm.style.display = 'none';
        document.getElementById('file_id').value = file_id
    } else {
        passwordForm.style.display = 'none';
        uploadForm.style.display = 'block';
    }
}

async function generateLink() {
    const token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    const file_id = document.getElementById('file_id').value;
    const password = document.getElementById('pwd').value;
    
    const response = await fetch(`http://localhost:8000/api/create-link`, {
        method: "POST",
        headers: {
            'X-CSRFToken': token,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({file_id, password})
    });
    
    if(response.status === 201){
        const result = await response.json();
        const protocol = location.protocol + '//' + window.location.host + '/'
        document.getElementById("card-link").innerHTML = protocol + result.data.link
        document.getElementById("card-link").href = protocol + result.data.link
        document.getElementById("card-pwd").innerHTML = result.data.password
        document.getElementById("card").style.display = 'block'

        togglePasswordInput()
    }
}

async function uploadFile(e) {
    e.preventDefault();
    const formData = new FormData();
    const fileField = document.querySelector('input[type="file"]');
    const token = document.querySelector("input[name=csrfmiddlewaretoken]").value;

    formData.append("files_to_upload", fileField.files[0]);

    const result = await fetch('http://localhost:8000/api/upload', {
        method: "POST",
        headers: {
            'X-CSRFToken': token
        },
        body: formData
    })

    if(result.status === 201){
        location.reload();
    }
}

document.getElementById("uploadForm").addEventListener("submit", function(event) {
    uploadFile(event);
})
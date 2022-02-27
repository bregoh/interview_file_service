
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
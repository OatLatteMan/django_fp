function confirmDeleteForm(event, form) {
    event.preventDefault();  // Stop default form submission

    Swal.fire({
        title: 'Are you sure?',
        text: "This action cannot be undone!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();  // Submit the form only if confirmed
        }
    });
}

function confirmEditForm(event, form) {
    event.preventDefault();  // Stop the form from immediately submitting

    Swal.fire({
        title: 'Edit this item?',
        text: "You'll be taken to the edit form.",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#aaa',
        confirmButtonText: 'Yes, proceed'
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();  // Submit the form if user confirms
        }
    });
}


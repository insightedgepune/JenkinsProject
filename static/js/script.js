function validateForm() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let course = document.getElementById("course").value;
    let feedback = document.getElementById("feedback").value.trim();

    if (name === "") {
        alert("Please enter student name.");
        return false;
    }

    if (email === "") {
        alert("Please enter email address.");
        return false;
    }

    if (course === "") {
        alert("Please select course.");
        return false;
    }

    if (feedback === "") {
        alert("Please enter feedback.");
        return false;
    }

    return true;
}

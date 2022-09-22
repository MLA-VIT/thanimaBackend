var backendUrl = 'http://localhost:8000';
var submissions = {};

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

if(getCookie('token') == "") {
    window.location.replace(`http://${window.location.host}/`);
  }

function renderContestDiv(event) {
    var output =
        `<div class="panel panel-warning">
        <div class="panel-heading">
            <h3>${event.name} | ${event.subname}</h3>
        </div>`;
    if (event.prize_reveal) {
        output += `
        <div class="well well-sm">Prizes Worth:<br><span class="badge">1st</span> ${event.prize_1}<br><span
                class="badge">2nd</span> ${event.prize_2}<br><span class="badge">3rd</span> ${event.prize_3}</div>`;
    }
    var deadline = new Date(event.deadline);
    output +=
        `<div class="panel-body">
        ${event.rules}<br><br>
        ${event.judging_criteria}
        </div>
        <div class="panel-footer">Last date for submission: ${deadline}</div>`;
    if (submissions[event.id]) {//already submitted
        output += `<div class="alert alert-success" id="uploaded-${event.id}"><strong><a href="${submissions[event.id]}" style="text-decoration:none;" target="_blank">View your submission</a></strong></div>`;
    } else if (deadline < Date.now()) {//deadline passed
        output +=
            `<div class="panel-footer">
                <div class="alert alert-danger">Submission Closed.</div>
                </div>`;
    } else {//can submit
        if (event.file_submission) {
            output +=
                `<div class="alert alert-success" id="upload-${event.id}">
            <strong>Upload Image:</strong> (Maximum File Size 3MB)</div>
            <input type="file" name="file" id="file-${event.id}">
            <button onclick="submitFile(${event.id})" id="file-upload">Upload File</button>`;
        } else {
            output +=
                `<div class="alert alert-warning"><strong>Upload your video in Google Drive (without any restriction - Edit the permission to "Anyone with the link can view") and paste the link below. Only the first link uploaded will be considered. So please be careful while uploading.</strong></div>
            <div id="upload-${event.id}">
            <div class="alert alert-success"><strong>Upload Video Link</strong></div>
            <input type="text" name="file" id="file-${event.id}">
            <button type="submit" onclick="submitLink(${event.id})" value="Upload Video Link">Upload Video Link</button></div>`;
        }
        output += `<div class="alert alert-success" id="uploaded-${event.id}" style="display:none;"><strong><a href="" style="text-decoration:none;" target="_blank">View your submission</a></strong></div>`;
    }
    output += `</div>`;
    return output;
}

function submitLink(eventId) {
    var link = document.getElementById(`file-${eventId}`).value;
    const submitRequest = {
        'file': link,
        'event_id': eventId
    };
    fetch(`${backendUrl}/api/events/submit/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${getCookie('token')}`
        },
        'body': JSON.stringify(submitRequest)
    })
        .then((response) => response.json())
        .then((result) => {
            console.log(result);
            if (result.status == 200) {
                document.getElementById(`upload-${eventId}`).style = 'display: none;';
                document.getElementById(`uploaded-${eventId}`).style = 'display: block;';
                document.getElementById(`uploaded-${eventId}`).innerHTML = `<strong><a href="${submissions[eventId].file}" style="text-decoration:none;">View your submission</a></strong>`;
            } else {
                alert(result.message);
            }
        })
        .catch((err) => console.error(err));
}

function submitFile(eventId) {
    var file = document.getElementById(`file-${eventId}`).files[0];
    let formData = new FormData();
    formData.append("file", file);
    formData.append("event_id", eventId);

    fetch(`${backendUrl}/api/events/submit/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${getCookie('token')}`
        },
        'body': formData
    })
        .then((response) => response.json())
        .then((result) => {
            console.log(result);
            if (result.status == 200) {
                document.getElementById(`upload-${eventId}`).style = 'display: none;';
                document.getElementById(`uploaded-${eventId}`).style = 'display: block;';
                document.getElementById(`uploaded-${eventId}`).innerHTML = `<strong><a href="${submissions[eventId].file}" style="text-decoration:none;">View your submission</a></strong>`;
            } else {
                alert(result.message);
            }
        })

}

function loadProfile() {
    fetch(`${backendUrl}/api/events/profile/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${getCookie('token')}`
        }
    })
        .then((response) => response.json())
        .then((response) => {
            console.log(response);
            for (const submission of response.data.submissions) {
                submissions[submission.event] = submission;
            }
            for (const event of response.data.events) {
                var element = renderContestDiv(event);
                var contestsElement = document.getElementById('contests');
                contestsElement.innerHTML += element;
            }
        })
        .catch((err) => {
            console.error(err);
        })
}

function deleteCookie(name) {
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

function logout() {
    deleteCookie('token');
    window.location.replace(backendUrl);
}

loadProfile();
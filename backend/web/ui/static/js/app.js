function error_alert(msg, form_id) {
    $(form_id +' #show_alert').addClass("show");
    $(form_id +' #show_alert #content').html(msg);

}

function user_register() {
    let user_data = {
        email: $("#user_registration #email").val(),
        password: $("#user_registration #password").val(),
        confirm_password: $("#user_registration #password2").val(),
    };
    if (user_data["confirm_password"] != user_data["password"]) {
        error_alert("Passwords do not match.", "#user_registration")
    } else {
        $.ajax({
            type: "POST",
            url: "/user",
            data: JSON.stringify({"email": user_data["email"], "password": user_data["password"]}),
            success: function (response, textStatus) {
                if (textStatus == "success") {
                    window.location = '/';
                } else {
                    let response_msg = jQuery.parseJSON(response.responseText)
                    error_alert(response_msg['msg'], "#user_registration")
                }
            },
            error: function (response) {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'], "#user_registration")

            },
            contentType: "application/json",
            dataType: "json",
        });
    }
}

function user_login() {
    let user_data = {
        email: $("#user_login #email").val(),
        password: $("#user_login #password").val(),
    };
    $.ajax({
        type: "POST",
        url: "/login",
        data: JSON.stringify({"email": user_data["email"], "password": user_data["password"]}),
        success: function (response, textStatus) {
            if (textStatus == "success") {
                window.location = '/';
            } else {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'], "#user_login")
            }
        },
        error: function (response) {
            let response_msg = jQuery.parseJSON(response.responseText)
            error_alert(response_msg['msg'], "#user_login")

        },
        contentType: "application/json",
        dataType: "json",
    });
}

function add_new_todo(todo_status_id) {
    let form_id = "#form_" + todo_status_id
    $(form_id).trigger("reset");
    var modal_id = "#modal_" + todo_status_id
    $(form_id).removeClass('was-validated')
    $(modal_id + " #submit_values").attr("onclick", "insert_new_todo(\"" + form_id + "\"," + "\"" + todo_status_id + "\")")
    $(modal_id + " #add_todo_modal").attr("onclick", "close_modal_window(\"" + modal_id + "\")")
    $(modal_id).modal('show')
}

function close_modal_window(modal_id){
    $(modal_id).modal('hide');
}

function insert_new_todo(form_id, todo_status_id) {
    let data = {
        "title": $(form_id + " input[name=title]").val(),
        "description": $(form_id + " #" + todo_status_id + "_description").val(),
        "priority": $(form_id + " #" + todo_status_id + "_priority").val(),
        "image": $(form_id + " input[name=image]").val(),
        "status": todo_status_id
    }
    $.ajax({
        type: "POST",
        url: "/todo",
        data: JSON.stringify(data),
        success: function (response, textStatus) {
            if (textStatus == "success") {
                window.location = '/';
            } else {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'], form_id)
            }
        },
        error: function (response) {
            let response_msg = jQuery.parseJSON(response.responseText)
            error_alert(response_msg['msg'], form_id)

        },
        contentType: "application/json",
        dataType: "json",
    });
}

function delete_todo(todo_id) {
    let form_id = "#todo_" + todo_id;
    $.ajax({
        type: "DELETE",
        url: "/todo/"+todo_id,
        success: function (response, textStatus) {
            if (textStatus == "success") {
                window.location = '/';
            } else {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'], form_id)
            }
        },
        error: function (response) {
            let response_msg = jQuery.parseJSON(response.responseText)
            error_alert(response_msg['msg'], form_id)

        },
    });
}

function update_todo(todo_id) {
    let form_id = "#form_todo_" + todo_id
    $(form_id).trigger("reset");
    let modal_id = "#todo_modal_" + todo_id
    $(form_id).removeClass('was-validated')
    $(form_id + " input[name=title]").val(todo_info.title)
    $(form_id + " #todo_description").val(todo_info.description)
    $(form_id + " #todo_priority").val(todo_info.priority)
    $(form_id + " #todo_status").val(todo_info.status)
    $(modal_id + " #submit_values").attr("onclick", "update_new_todo(\"" + form_id + "\"," + "\"" + modal_id + "\")")
    $(modal_id + " #add_todo_modal").attr("onclick", "close_modal_window(\"" + modal_id + "\")")
    $(modal_id).modal('show')
}

function update_todo_item(data){
    // <script>alert(document.cookie);</script>
    todo_info.title = data["title"]
    todo_info.description = data["description"]
    todo_info.priority = data["priority"]
    todo_info.status = data["status"]
    $("#div_todo_title").html(data["title"])
    $("#div_todo_description").html(data["description"])
}

function update_new_todo(form_id, modal_id) {
    let data = {
        "title": $(form_id + " input[name=title]").val(),
        "description": $(form_id + " #todo_description").val(),
        "priority": $(form_id + " #todo_priority").val(),
        "image": $(form_id + " input[name=image]").val(),
        "status": $(form_id + " #todo_status").val()
    }
    $.ajax({
        type: "PUT",
        url: "/todo/" + todo_info.id,
        data: JSON.stringify(data),
        success: function (response, textStatus) {
            if (textStatus == "success") {
                update_todo_item(data)
                $(modal_id).modal('hide')
            } else {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'], form_id)
            }
        },
        error: function (response) {
            let response_msg = jQuery.parseJSON(response.responseText)
            error_alert(response_msg['msg'], form_id)

        },
        contentType: "application/json",
        dataType: "json",
    });
}

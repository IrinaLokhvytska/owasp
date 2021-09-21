function error_alert(msg, form_id) {
    $(form_id +' #show_alert').addClass("show");
    $(form_id +' #show_alert #content').html(msg);

}

function user_register() {
    let user_data = new FormData();
    let email = $("#user_registration input[name=email]").val()
    let password = $("#user_registration input[name=password]").val()
    let password2 = $("#user_registration input[name=password2]").val()
    user_data.append("email", email);
    user_data.append("password", password);
    user_data.append("password2", password2);
    if (password != password2) {
        error_alert("Passwords do not match.", "#user_registration")
    } else {
        $.ajax({
            type: "POST",
            url: "/user",
            data: user_data,
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
            contentType: false,
            mimeType: "multipart/form-data",
            processData: false,
        });
    }
}

function user_login() {
    let user_data = new FormData();
    let email = $("#user_login input[name=email]").val()
    let password = $("#user_login input[name=password]").val()
    user_data.append("email", email);
    user_data.append("password", password);
    $.ajax({
        type: "POST",
        url: "/login",
        data: user_data,
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
        contentType: false,
        mimeType: "multipart/form-data",
        processData: false,
    });
}

function add_new_todo(todo_status_id) {
    let form_id = "#form_" + todo_status_id
    $(form_id).trigger("reset");
    var modal_id = "#modal_" + todo_status_id
    $(form_id).removeClass('was-validated')
    $(modal_id + " #submit_values").attr("onclick", "insert_new_todo(\"" + form_id + "\"," + todo_status_id + ")")
    $(modal_id + " #add_todo_modal").attr("onclick", "close_modal_window(\"" + modal_id + "\")")
    $(modal_id).modal('show')
}

function close_modal_window(modal_id){
    $(modal_id).modal('hide');
}

function insert_new_todo(form_id, todo_status_id) {
    let data = {
        "title": $(form_id + " input[name=title]").val(),
        "description": $(form_id + " input[name=description]").val(),
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
    $(form_id + " input[name=description]").val(todo_info.description)
    $(form_id + " #todo_priority").val(todo_info.priority)
    $(form_id + " #todo_status").val(todo_info.status)
    $(modal_id + " #submit_values").attr("onclick", "update_new_todo(\"" + form_id + "\")")
    $(modal_id + " #add_todo_modal").attr("onclick", "close_modal_window(\"" + modal_id + "\")")
    $(modal_id).modal('show')
}

function update_new_todo(form_id) {
    let data = {
        "title": $(form_id + " input[name=title]").val(),
        "description": $(form_id + " input[name=description]").val(),
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

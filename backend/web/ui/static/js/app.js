function error_alert(msg, form_id) {
    console.error(msg)
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

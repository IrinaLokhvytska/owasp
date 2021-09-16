function warning_alert(msg) {
    $('#show_alert #content').html(msg);
    $('#show_alert #alert_body').removeClass();
    $('#show_alert #alert_body').addClass("alert alert-warning");

}
function success_alert(msg) {
    $('#show_alert #content').html(msg);
    $('#show_alert #alert_body').removeClass();
    $('#show_alert #alert_body').addClass("alert alert-success");

}
function error_alert(msg) {
    $('#show_alert #content').html(msg);
    $('#show_alert #alert_body').removeClass();
    $('#show_alert #alert_body').addClass("alert alert-danger");

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
        error_alert("Passwords do not match.")
    } else {
        $.ajax({
            type: "POST",
            url: "/user",
            data: user_data,
            success: function (response) {
                let response_msg = jQuery.parseJSON(response.responseText)
                if (response_msg['answer'] == "success") {
                    console.log(response_msg['answer'])
                } else {
                    error_alert(response_msg['msg'])
                }
            },
            error: function (response) {
                let response_msg = jQuery.parseJSON(response.responseText)
                error_alert(response_msg['msg'])
    
            },
            contentType: false,
            mimeType: "multipart/form-data",
            processData: false,
        });
    }
}
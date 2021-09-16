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
    let user_data = {
        email: $("#email").val(),
        password: $("#password").val(),
        confirm_password: $("#password2").val(),
    };
    if (user_data["confirm_password"] != user_data["password"]) {
        error_alert("Passwords do not match.")
    } else {
        $.ajax({
            type: "POST",
            url: "/user",
            data: JSON.stringify({"email": user_data["email"], "password": user_data["password"]}),
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
            contentType: "application/json",
            dataType: "json",
        });
    }
}